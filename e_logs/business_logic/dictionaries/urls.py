from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
    path('get_dicts/', DictionariesApi.as_view()),
    path('autocomplete/', AutocompleteAPI.as_view(), name="Фамилия И.О."),
    path('usernames/', UsernamesAPI.as_view(), name="Имена пользователей"),

]
