
from django.conf.urls import url, include
from django.urls import path

from common.all_journals_app import views

urlpatterns = [
    url('change_table$', views.change_table),
]