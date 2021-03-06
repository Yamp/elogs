from django.contrib import admin
from e_logs.common.feedback_app.models import *


class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    verbose_name_plural = 'Обратная связь для разработчиков'
    list_display = ['theme', 'plant', 'url', 'username']


admin.site.register(Feedback, FeedbackAdmin)
