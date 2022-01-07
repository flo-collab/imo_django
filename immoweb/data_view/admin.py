from django.contrib import admin

# Register your models here.
from data_view.models import Ville
class Filter(admin.ModelAdmin):
    list_display = [field.name for field in Ville._meta.get_fields()]

admin.site.register(Ville,Filter)