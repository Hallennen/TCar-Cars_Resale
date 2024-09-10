from typing import Any
from django import forms
from cars.models import car, Brand, CorCar
from django.db.models.query import QuerySet

class CarModelform(forms.ModelForm):
        class Meta:
                model = car
                fields = '__all__'


        def clean_value(self):
                value = self.cleaned_data.get('value')
                if value < 6000:
                        self.add_error('value','Valor minimo de R$ 6.000, para cadastro de veiculos.') 
                return value
        

        def clean_model_year(self):
                factory_year = self.cleaned_data.get('factory_year')
                print('fabricação_ano: ', factory_year)
                model_year = self.cleaned_data.get('model_year')
                print('modelo_ano: ', model_year)
                if (model_year - factory_year ) > 1 or (model_year - factory_year) < 0:
                        self.add_error('model_year','Verifique o ano do modelo em relação ao ano de Fabricação')
                return factory_year
                

        def clean_plate(self):
                plate_input = self.cleaned_data.get('plate')
                plates = car.objects.filter(plate = plate_input).values('plate')

                if plates: 
                        self.add_error('plate', 'Ja existe um registro com essa placa, favor verificar.')
                return plate_input
        
        def clean_model(self):
                name_input = self.cleaned_data.get('model')
                name_models = car.objects.filter(model = name_input).values('model')

                if name_models:
                        self.add_error('model', 'Nome do carro ja cadastrado, verifique e altere-o ')
                return name_input
        
class CarModelUpdateForm(forms.ModelForm):
        class Meta:
                model = car
                fields = '__all__'




class CarBrandForm(forms.ModelForm):
        class Meta:
                model = Brand
                fields = '__all__'

        def clean_name(self):
                name = self.cleaned_data.get('name') 
                names_brand = Brand.objects.filter(name= name)
                if names_brand:
                        self.add_error('name', 'Marca já cadastrada')
                return name




class Corform(forms.ModelForm):
        class Meta:
                model = CorCar
                fields = '__all__'
        