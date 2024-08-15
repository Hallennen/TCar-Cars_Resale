from django import forms
from cars.models import Brand, car

class CarForm(forms.Form):
        model = forms.CharField(max_length=10)
        brand = forms.ModelChoiceField(Brand.objects.all())
        factory_year = forms.IntegerField()
        model_year = forms.IntegerField()
        plate = forms.CharField(max_length=10)
        value = forms.FloatField()
        photo = forms.ImageField()
        
    



