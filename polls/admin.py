from django.contrib import admin

from .models import Question,Choice

class AdminChoice(admin.ModelAdmin):
    list_display = ['id', 'question', 'choice_text', 'votes']
admin.site.register(Question)
admin.site.register(Choice, AdminChoice)