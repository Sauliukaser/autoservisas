from django.contrib import admin
from .models import Paslaugos, UzsakymoEilute, Uzsakymas, Automobilis, AutomobiliuModeliai

class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ("id", "cliet", "car_model_id", "number_plate","vin_code")
    search_fields = ("number_plate","vin_code")
    list_filter = ('cliet',"car_model_id__modelis" )
class PaslaugosAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

class UzsakymasInstanceInline(admin.TabularInline):
    model = UzsakymoEilute
    extra = 0
    can_delete = False
class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ("car_id", "date")
    inlines = [UzsakymasInstanceInline]

# Register your models here.
admin.site.register(Paslaugos,PaslaugosAdmin)
admin.site.register(UzsakymoEilute)
admin.site.register(Uzsakymas,UzsakymasAdmin)
admin.site.register(Automobilis,AutomobilisAdmin)
admin.site.register(AutomobiliuModeliai)
