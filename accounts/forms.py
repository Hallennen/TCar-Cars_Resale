from typing import Any
from django import forms
from django.contrib.auth.models import User
from accounts.models import dados_pessoais

class UserModelForms(forms.ModelForm):
    class Meta: 
        model = dados_pessoais
        fields = "__all__"


    def clean_telefone(self):
        telefone_input = self.cleaned_data.get('telefone')
        telefone = dados_pessoais.objects.filter(telefone = telefone_input).values('telefone')
        if telefone:
            self.add_error('telefone', 'Telefone já cadastrado, favor verifique o número informado')
        
        return telefone_input
    

