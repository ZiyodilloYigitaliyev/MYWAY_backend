from django.contrib import admin
from .models import *


@admin.register(AutoTestResult)
class AutoTestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'trueAnswer', 'falseAnswer', 'fullAnswer', 'created')

@admin.register(AutoTestQuestionse)
class AutoTestResultAdmin(admin.ModelAdmin):
    list_display = ('questionID', 'question','trueAnswer', )
