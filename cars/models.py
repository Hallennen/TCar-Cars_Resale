from django.db import models

# Create your models here.
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name = 'Nome da Marca')

    class Meta:
        ordering = ['name']

    def __str__(self) :
        return self.name    
    
class TracaoCar(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    tracao_tipo = models.CharField(null= True, blank= True)

    def __str__(self):
        return self.tracao_tipo


class CorCar(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    cor_name = models.CharField(null= True, blank= True)

    class Meta:
        ordering =['cor_name'] 

    def __str__(self):
        return self.cor_name


class car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200,  verbose_name = "Modelo")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand',  verbose_name = "Marca")
    factory_year = models.IntegerField(blank=True, null=True,  verbose_name = "Ano de Fabricação")
    model_year = models.IntegerField(blank=True, null=True,  verbose_name = "Ano do Modelo")
    cor = models.ForeignKey(CorCar, on_delete=models.PROTECT , related_name='car_cor')
    tracao = models.ForeignKey(TracaoCar, on_delete=models.PROTECT, related_name='car_tracao', verbose_name= 'Tração')
    plate = models.CharField(max_length=10, blank=True, null=True,  verbose_name = "Placa")
    value = models.FloatField(blank=True, null=True,  verbose_name = "Valor")
    photo = models.ImageField(upload_to= 'cars/', blank=True, null=True,  verbose_name = "Foto")
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model   
    

class CarInvetory(models.Model):
    id = models.AutoField(primary_key=True)
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'



