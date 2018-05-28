from django.shortcuts import render
from utils.deep_dict import deep_dict

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from utils.deep_dict import deep_dict
from datetime import time

# Create your views here.
from django.template import loader

# from common.all_journals_app.models import JournalPage
from common.all_journals_app.services.context_creator import get_common_context



@login_required
def index(request):
    context = get_common_context(journal_name="electrolysis_technical_report_4_degree")
    template = loader.get_template('common.html')

    left_table = deep_dict()

    left_table.title = "Крекс Шпекс"
    left_table.name = "tables/left_table.html"

    context.tables = [left_table]
    return HttpResponse(template.render(context, request))
