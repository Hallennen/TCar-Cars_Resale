from django import forms
from cars.models import car

class CarModelform(forms.ModelForm):
        class Meta:
                model = car
                fields = '__all__'


        def clean_value(self):
                value = self.cleaned_data.get('value')
                if value < 6000:
                        self.add_error('value','Valor minimo de R$ 6.000, para cadastro de veiculos.') 
                return value
        



