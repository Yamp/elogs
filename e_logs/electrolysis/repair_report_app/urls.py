from e_logs.electrolysis.repair_report_app import views
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    url('^$', views.index)
]