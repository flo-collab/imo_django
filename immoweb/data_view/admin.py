from django.contrib import admin
from data_view.models import Ville
from data_view.models import Send_mail

class Filter(admin.ModelAdmin):
    list_display = [field.name for field in Ville._meta.get_fields()]

admin.site.register(Ville,Filter)


@admin.register(Send_mail)
class RequestSend_mail(admin.ModelAdmin):
    list_display =  [field.name for field in Send_mail._meta.get_fields()]
