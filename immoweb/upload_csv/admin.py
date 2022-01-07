from django.contrib import admin
from upload_csv.models import Bien
# Register your models here.



class Filter(admin.ModelAdmin):
    list_disp = [field.name for field in Bien._meta.get_fields()]
    list_disp.remove('id_lot')
    print('la liste est !',list_disp)
    list_display =list_disp
    # ('nb_piece', 'prix_m2_TTC', 'surface')
    list_filter = ('departement',)
    #list_filter = ('exterieur','balcony','garden','parking')


admin.site.register(Bien, Filter)
# admin.site.register(Bien)

