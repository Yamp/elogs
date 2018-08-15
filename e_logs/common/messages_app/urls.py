from django.urls import path

from e_logs.common.messages_app import views
from e_logs.core.utils.webutils import process_json_view

urlpatterns = [
    path('get/', views.msg_view, name='messages_get'),
    path('read/', views.msg_view, name='messages_read'),
    path('list/', views.MessagesList.as_view(), name='messages_list'),
    path('add_critical/', views.add_critical),
    path('add_comment/', views.add_comment),
    path('update/', views.update),

]
