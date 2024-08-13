from django.contrib import admin
from cars.models import car , Brand

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

admin.site.register(car, CarAdmin)

class BrandCar(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Brand, BrandCar)