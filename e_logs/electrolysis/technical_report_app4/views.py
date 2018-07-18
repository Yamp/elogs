# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from e_logs.core.utils.deep_dict import deep_dict
from datetime import time

# Create your views here.
from django.template import loader

# from common.all_journals_app.models import JournalPage
from e_logs.common.all_journals_app.services.context_creator import get_common_context



@login_required
def index(request):
    context = get_common_context(journal_name="electrolysis_technical_report_4_degree", request=request)
    context.journal_title = 'Технологический журнал электролиза 4-й серии'

    template = loader.get_template('common.html')

    left_table = deep_dict()
    right_table = deep_dict()

    left_table.name = "technical_report4_tables/left_table.html"

    right_table.name = "technical_report4_tables/right_table.html"

    context.tables = [left_table, right_table]
    return HttpResponse(template.render(context, request))
