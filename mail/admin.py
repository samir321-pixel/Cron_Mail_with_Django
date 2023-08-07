from django.contrib import admin
from .models import *


class Employee_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]
    filter_horizontal = ()
    list_filter = [field.name for field in Employee._meta.fields]
    fieldsets = ()


class EmailTemplate_Admin(admin.ModelAdmin):
    list_display = [field.name for field in EmailTemplate._meta.fields]
    filter_horizontal = ()
    list_filter = [field.name for field in EmailTemplate._meta.fields]
    fieldsets = ()


class Event_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]
    filter_horizontal = ()
    list_filter = [field.name for field in Event._meta.fields]
    fieldsets = ()


class EmailLog_Admin(admin.ModelAdmin):
    list_display = [field.name for field in EmailLog._meta.fields]
    filter_horizontal = ()
    list_filter = [field.name for field in EmailLog._meta.fields]
    fieldsets = ()


admin.site.register(Employee, Employee_Admin)
admin.site.register(Event, Event_Admin)
admin.site.register(EmailTemplate, EmailTemplate_Admin)
admin.site.register(EmailLog, EmailLog_Admin)
