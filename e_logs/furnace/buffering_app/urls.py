from e_logs.furnace.buffering_app import views
from django.conf.urls import url

urlpatterns = [
    url('^$', views.index)
]