import json
from datetime import timedelta

from cacheops import cached_view_as
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from functional import seq

from e_logs.common.all_journals_app.models import Cell, Plant, Measurement
from e_logs.core.utils.deep_dict import DeepDict
from e_logs.core.utils.webutils import process_json_view


@login_required
def add_measurement(request):
    if request.method == 'POST':
        req = json.loads(request.body)

        if hasattr(req, 'id'):
            measurement = req['id']
        else:
            measurement = Measurement.objects.create(type="measurement", time=timezone.now(),
                                                     name="fractional_anal",
                                                     plant=Plant.objects.get(name="furnace")).id

        for m_value in req['cinder']['masses']:
            Cell.objects.create(table_name="measurements", field_name='cinder_mass',
                                index=0, value=m_value, group_id=measurement).cache()
        for m_value in req['cinder']['min_sizes']:
            Cell.objects.create(table_name="measurements", field_name='cinder_size',
                                index=0, value=m_value, group_id=measurement).cache()
        for m_value in req['schieht']['masses']:
            Cell.objects.create(table_name="measurements", field_name='schieht_mass',
                                index=0, value=m_value, group_id=measurement).cache()
        for m_value in req['schieht']['min_sizes']:
            Cell.objects.create(table_name="measurements", field_name='schieht_size',
                                index=0, value=m_value, group_id=measurement).cache()

        return HttpResponse(status=201)
    return HttpResponse(status=405)


@cached_view_as(Cell, Measurement)
@process_json_view(auth_required=False)
def granularity_object(request):
    res = DeepDict()

    def set_data(staff, future):
        nonlocal res
        branch = res['data'][measurement.id + future][staff]
        branch['time'] = (measurement.time + timedelta(days=700)).timestamp()
        branch['masses'] = [round(float(m.value), 2) for m in
                            Cell.objects.select_related('field')
                                .filter(field__name=staff + "_mass", group=measurement).cache()]
        branch['min_sizes'] = [round(float(m.value), 2) for m in
                               Cell.objects.select_related('field')
                                   .filter(field__name=staff + "_size", group=measurement).cache()]

    for measurement in Measurement.objects.all()[:2]:
        set_data('cinder', future=100)
        set_data('schieht', future=100)

    for measurement in Measurement.objects.all():
        set_data('cinder', future=0)
        set_data('schieht', future=0)

    return res


@cached_view_as(Cell.objects.filter(field__name='cinder_mass'),
                Cell.objects.filter(field__name='cinder_size'),
                Cell.objects.filter(field__name='schieht_mass'),
                Cell.objects.filter(field__name='schieht_size'))
@process_json_view(auth_required=False)
def granularity_graphs(request):
    def get_cell(name):
        return list(Cell.objects.filter(field__name=name).cache())

    def get_mean(masses, sizes):
        msum = sum(masses)
        if msum == 0:
            return 0

        mass_parts = [m / msum for m in masses]
        sizes = sizes + [sizes[-1]]
        middles = [(sizes[i] + sizes[i + 1]) / 2 for i in range(len(sizes) - 1)]
        res = [float(mas) * float(mid) for mas, mid in zip(mass_parts, middles)]
        return sum(res)

    cinders = []
    schieht = []

    cinder_masses = get_cell("cinder_mass")
    cinder_sizes = get_cell("cinder_size")
    schieht_masses = get_cell("schieht_mass")
    schieht_sizes = get_cell("schieht_size")

    for measurement in Measurement.objects.all():
        def process(x):
            return seq(x).where(lambda y: y.group == measurement).map(
                lambda z: float(z.value)).to_list()

        masses = process(cinder_masses)
        min_sizes = process(cinder_sizes)
        cinders.append([measurement.time.timestamp(), get_mean(masses, min_sizes)])

        masses = process(schieht_masses)
        min_sizes = process(schieht_sizes)
        schieht.append([measurement.time.timestamp(), get_mean(masses, min_sizes)])

    res = DeepDict()
    res['data']['cinder'] = cinders
    res['data']['schieht'] = schieht

    return res
