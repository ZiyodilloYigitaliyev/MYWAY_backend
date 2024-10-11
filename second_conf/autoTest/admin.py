from django.contrib import admin

from second_conf.autoTest.models import AutoTestResult


@admin.register(AutoTestResult)
class AutoTestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'trueAnswer', 'falseAnswer', 'fullAnswer', 'created')

@admin.register(AutoTestResult)
class AutoTestResultAdmin(admin.ModelAdmin):
    list_display = ('questionID', 'question','trueAnswer', )
