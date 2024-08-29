from django import forms
from django.contrib.auth.models import User
from accounts.models import dados_pessoais

class UserModelForms(forms.ModelForm):
    class Meta: 
        model = dados_pessoais
        fields = "__all__"


        