from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from e_logs.core.utils.deep_dict import deep_dict

# Create your views here.
from django.template import loader

from e_logs.common.all_journals_app.models import JournalPage
from e_logs.common.all_journals_app.services.context_creator import get_common_context


@login_required
def index(request):
    context = get_common_context(journal_name="concentrate_report_journal", request=request)
    context.journal_title = 'Журнал рапортов о проделанной работе по складам концентратов';

    big_table = deep_dict()
    small_table = deep_dict()
    upper_table = deep_dict()
    lower_table = deep_dict()

    big_table.name = 'concentrate_report_tables/big_table.html'

    small_table.name = 'concentrate_report_tables/small_table.html'

    upper_table.name = 'concentrate_report_tables/upper_table.html'

    lower_table.name = 'concentrate_report_tables/lower_table.html'

    context.tables = [upper_table, big_table, small_table]

    template = loader.get_template('common.html')
    return HttpResponse(template.render(context.get_dict(), request))


@login_required
def tpp(request):
    context = get_common_context(journal_name="concentrate_report_journal", request=request)
    context.journal_title = 'Журнал рапортов о проделанной работе по складам концентратов';

    big_table = deep_dict()
    small_table = deep_dict()
    upper_table = deep_dict()
    lower_table = deep_dict()

    big_table.name = 'concentrate_report_tables/big_table.html'

    small_table.name = 'concentrate_report_tables/small_table.html'

    upper_table.name = 'concentrate_report_tables/upper_table.html'

    lower_table.name = 'concentrate_report_tables/lower_table.html'

    context.tables = [upper_table, big_table, small_table, lower_table]

    template = loader.get_template('common.html')
    return HttpResponse(template.render(context.get_dict(), request))
