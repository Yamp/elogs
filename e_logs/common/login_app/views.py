import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import views, authenticate, login, logout
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from e_logs.common.all_journals_app.fields_descriptions.fields_info import fields_info_desc
from e_logs.common.messages_app.models import Message

from utils.deep_dict import deep_dict
from utils.errors import AccessError
from utils.webutils import process_json_view, generate_csrf, model_to_dict, set_cookie


@process_json_view(auth_required=False)
def login_auth(request):
    username = request.POST.get('username') or ''
    password = request.POST.get('password') or ''

    user = authenticate(username=username, password=password)
    if user is not None and user.is_active and user.employee is not None:
        login(request, user)
        response = redirect(request.GET.get('next') or '/')
    else:
        return login_page(request, error='Неверное имя пользователя или пароль!')

    return response


@process_json_view(auth_required=False)
def logout_view(request):
    logout(request)
    return login_page(request, error=None)


def login_page(request, error=None):
    context = {'error': error, 'next': '?next=' + (request.GET.get('next') or '/')}

    template = loader.get_template('login.html')
    response = HttpResponse(template.render(context, request))

    return response


@process_json_view(auth_required=False)
def get_messages(request):
    res = deep_dict()
    res['messages'] = {}
    for m in Message.objects.filter(is_read=False):
        res['messages'][m.id] = model_to_dict(m)
    return res


@process_json_view(auth_required=False)
def read_message(request):

    print(request.POST)
    msg_id = json.loads(request.POST.get('ids[]')) or 0
    print(msg_id)
    msg = Message.objects.get(id=int(msg_id))
    if msg.addressee == request.user.employee:
        msg.is_read = True
        msg.save()
    else:
        raise AccessError(message="Попытка отметиь чужое сообщение как прочитанное")

    return {"status": 0}