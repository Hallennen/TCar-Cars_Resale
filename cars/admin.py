from django.contrib import admin
from cars.models import car , Brand, CorCar, TracaoCar

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'plate', 'value')
    search_fields = ('model', 'brand')

admin.site.register(car, CarAdmin)

class BrandCar(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Brand, BrandCar)

class Cor_admin(admin.ModelAdmin):
    list_display = ('id', 'cor_name')

admin.site.register(CorCar, Cor_admin)


class Tracao(admin.ModelAdmin):
    list_display = ('id', 'tracao_tipo')

admin.site.register(TracaoCar, Tracao)