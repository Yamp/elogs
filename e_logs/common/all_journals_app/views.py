from os import walk
import json

from datetime import date, datetime

from django.db import transaction
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.template import loader, TemplateDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


from e_logs.common.all_journals_app.models import Cell, Shift
from e_logs.core.utils.webutils import process_json_view, logged
from e_logs.common.all_journals_app.services.context_creator import get_common_context
from e_logs.core.utils.loggers import stdout_logger
from e_logs.common.messages_app.services import messages
from e_logs.core.models import Setting


class JournalView(LoginRequiredMixin, View):
    """ Common view for a journal. Inherit from this class when creating your own journal view """

    @logged
    def get(self, request, plant, name):
        print('journal_name = {}'.format(name))
        stdout_logger.debug('JournalView: name = {}'.format(name))

        page = Shift.objects.filter(name=name).first()
        page_type = page.type if page else 'shift'
        stdout_logger.debug(f'JournalView: page_type: {page_type}')
        context = self.get_context(request=request, name=name, page_type=page_type)
        context.journal_title = Setting.objects.get(name='verbose_name', journal=name).value

        templates_dir = 'e_logs/common/all_journals_app/templates/tables/{}/{}'.format(plant, name)
        tables_paths = []
        stdout_logger.debug('JournalView.get(): before file walk')
        for (dirpath, dirnames, filenames) in walk(templates_dir):
            tables_paths.extend(
                ['tables/{}/{}/'.format(plant, name) + f for f in filenames if f.endswith(".html")]
            )
        stdout_logger.debug('JournalView.get(): after file walk')
        context.tables_paths = tables_paths

        template = loader.get_template('common.html')
        stdout_logger.debug('JournalView.get(): before render')
        rendered_template = template.render(context, request)
        stdout_logger.debug('JournalView.get(): before response')

        return HttpResponse(rendered_template)

    @logged
    def get_context(self, request, name, page_type):
        return get_common_context(name, request, page_type)


class ShihtaJournalView(JournalView):
    """ View of report_income_outcome_schieht journal """
    @logged
    def get_context(self, request, name, page_type):
        context = super().get_context(request, name, page_type)

        context.months = dict(zip(
            ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        ))
        context.plan_or_fact = ['plan', 'fact']
        context.date_year = datetime.now().year
        context.cur_month = list(context.months.keys())[date.today().month-1]
        return context


class MetalsJournalView(JournalView):
    """ View of metals_compute journal """

    @logged
    def get_context(self, request, name, page_type):
        from e_logs.common.all_journals_app.fields_descriptions.fields_info import fields_info_desc
        context = super().get_context(request, name, page_type)

        context.sgok_table.columns = [
            "ЗГОК, ВМТ",
            "Арт-ий, ВМТ",
            "Усть-ТАЛ, ВМТ",
            "Кара<wbr>гайлы, ВМТ",
            "Верх-Бер, ВМТ",
            "Бело<wbr>усовка, ВМТ",
            "Жез<wbr>кент, ВМТ",
            "Ер Тай, ВМТ",
            "Н.Широ<wbr>кинский, ВМТ",
            "Лесо<wbr>сиб, ВМТ",
            "Алтын-Топкан, ВМТ",
            "итого ВМТ",
            "ИТОГО СМТ",
            "выданно огарка, ВМТ",
            "потери, ВМТ",
            "огарка переданно, ВМТ",
            "ЦЕХ, ВМТ",
            "Лента, ВМТ",
            "потеря бункеров ОВЦО, ВМТ",
            "лента итого, ВМТ",
            "откло<wbr>нение"
        ]

        context.sgok_table.fields = fields_info_desc.metals_compute.sgok_table.keys()
        context.gof_table.fields = fields_info_desc.metals_compute.gof_table.keys()
        context.avg_month_table.fields = fields_info_desc.metals_compute.avg_month_table.keys()
        return context


@csrf_exempt
@process_json_view(auth_required=False)
@logged
def change_table(request):
    # tn = request.POST['table_name']
    # jp = request.POST['journal_page']

    # page = JournalPage.objects.get(id=int(jp))

    # employee = request.user.employee
    # page.employee_set.add(employee)

    # Cell.objects.filter(table_name=tn, journal_page=page).delete()

    # for field_name in request.POST:
    #     values = request.POST.getlist(field_name)
    #     with transaction.atomic():
    #         for i, val in enumerate(values):
    #             Cell(journal_page=page, value=val, index=i, field_name=field_name, table_name=tn).save()

    return {"status": 1}


@csrf_exempt
@process_json_view(auth_required=False)
@logged
def get_fields_descriptions(request):
    from e_logs.common.all_journals_app.fields_descriptions.fields_info import fields_info_desc
    return fields_info_desc


@logged
def permission_denied(request, exception, template_name='errors/403.html'):
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        return HttpResponseForbidden('<h1>403 Forbidden</h1>', content_type='text/html')
    return HttpResponseForbidden(
        template.render(request=request, context={'exception': str(exception)}))


@csrf_exempt
@logged
def save_cell(request):
    cell = json.loads(request.body)['cell']
    value = json.loads(request.body)['value']

    Cell.objects.update_or_create(**cell ,defaults = {"value":value, "responsible":request.user.employee})

    page = Shift.objects.get(id=int(cell['group_id']))
    employee = request.user.employee
    page.employee_set.add(employee)

    return JsonResponse({"status": 1})
