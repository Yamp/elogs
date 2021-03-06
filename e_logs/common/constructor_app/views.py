import os
import shutil
import hashlib
import json
from datetime import timedelta

from proxy.views import proxy_view
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.http import JsonResponse, HttpResponse

from e_logs.core.journals_git import VersionControl
from e_logs.core.utils.loggers import err_logger
from e_logs.core.utils.webutils import current_date
from e_logs.business_logic.dictionaries.models import EquipmentDict
from e_logs.common.all_journals_app.models import Shift, Equipment, Month, Year, Journal
from e_logs.common.all_journals_app.services.journal_builder import JournalBuilder


@csrf_exempt
def constructor_proxy(request, path):
    remoteurl = 'http://localhost:3000/' + path
    return proxy_view(request, remoteurl)


class ConstructorJournalAPI(View):
    def get(self, request):
        plant = request.GET.get("plant", None)
        journal = request.GET.get("journal", None)
        version = request.GET.get("version", None)
        current_path = os.path.dirname(__file__)
        filepath = os.path.abspath(
            os.path.join(current_path, f"../../../resources/journals/{plant}/{journal}/v{version}.jrn"))
        with open(filepath, "r") as f:
            data = f.read()
        return HttpResponse(data, content_type="application/json")

    def post(self, request):
        journal = json.loads(request.body)
        current_path = os.path.dirname(__file__)
        filepath = os.path.abspath(
            os.path.join(current_path, f"../../../resources/temp/{journal['name']}"))
        with open(filepath, "w") as f:
            json.dump(journal, f)

        hasher = hashlib.md5()
        hasher.update(json.dumps(journal).encode())

        journal_hash = hasher.hexdigest()
        filepath_w_hash = os.path.abspath(
            os.path.join(current_path, f"../../../resources/temp/{journal_hash}.jrn"))
        os.rename(filepath, filepath_w_hash)

        return JsonResponse({"hash": journal_hash})


class ConstructorAlterJournalAPI(View):
    with cache.lock("alter_journal"):
        def post(self, request):
            hash = request.POST.get('hash', None)
            plant = request.POST.get('plant', None)
            journal_name = request.POST.get('journal_name', None)

            git = VersionControl()
            journal = Journal.objects.get(plant__name=plant, name=journal_name)
            version = git.version_of(journal) + 1

            shutil.copy(f'resources/temp/{hash}.jrn',
                        f'resources/journals/{plant}/{journal.name}/v{version}.jrn')

            git.commit(journal)

            journal = JournalBuilder(f'resources/temp/{hash}.jrn', journal.plant.name, version, journal.type)
            journal.create()

            return JsonResponse({"status": 1})


class ConstructorUploadAPI(View):
    def post(self, request):
        with cache.lock("load_journal"):
            hash = request.POST.get('hash', None)
            plant = request.POST.get('plant', None)
            type = request.POST.get('type', None)
            number_of_shifts = request.POST.get('number_of_shifts', None)
            if number_of_shifts:
                number_of_shifts = int(number_of_shifts)

            if not hash or not plant:
                return JsonResponse({"status": 2, "message": "Couldnt upload without hash or plant"})

            journal = JournalBuilder(file=f'resources/temp/{hash}.jrn', plant_name=plant, type=type, version=1)
            new_journal = journal.create()
            try:
                os.makedirs(f'resources/journals/{plant}/{new_journal.name}/')
            except:
                pass
            shutil.copy(f'resources/temp/{hash}.jrn', f'resources/journals/{plant}/{new_journal.name}/v1.jrn')

            self.add_groups(new_journal, number_of_shifts)

            git = VersionControl()
            git.add(journal)

            return JsonResponse({"status": 1})

    @staticmethod
    def add_groups(journal, shifts_num=None):
        def date_range(start_date, end_date):
            for n in range(int((end_date - start_date).days)):
                yield start_date + timedelta(n)

        now_date = current_date()

        if journal.type == 'shift':
            for shift_date in date_range(now_date - timedelta(days=7), now_date + timedelta(days=7)):
                for shift_order in range(1, shifts_num + 1):
                    shift, created = Shift.objects.get_or_create(journal=journal, order=shift_order,
                                                                 date=shift_date)
        elif journal.type == 'year':
            for year in range(2017, current_date().year + 4):
                year, created = Year.objects.get_or_create(year_date=year, journal=journal)

        elif journal.type == 'month':
            for year in range(2017, current_date().year + 4):
                for ind, month in enumerate(['Январь', 'Февраль', 'Март', 'Апрель',
                                             'Май', 'Июнь', 'Июль', 'Август',
                                             'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'], 1):
                    month, created = Month.objects.get_or_create(year_date=year, month_date=month,
                                                                 month_order=ind,
                                                                 journal=journal)

        elif journal.type == 'equipment':
            for equipment in EquipmentDict.objects.filter(plant=journal.plant):
                Equipment.objects.get_or_create(name=equipment.name, journal=journal)
