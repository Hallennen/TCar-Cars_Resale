from django.db import models

# Create your models here.
class dados_pessoais(models.Model):
    primeiro_nome = models.CharField(max_length= 150, null=False, blank= False) 
    ultimo_nome = models.CharField(max_length= 150, null=False, blank= False)
    data_nascimento = models.DateField(null= False, blank= False) 
    estado = models.CharField(max_length= 70, null=False, blank= False)  
    bairro = models.CharField(max_length= 150, null=False, blank= False) 
    endereço = models.CharField(max_length= 250, null=False, blank= False)
    dd_telefone = models.CharField(max_length= 2, null=False, blank= False )
    telefone = models.CharField(max_length= 10, null=False, blank= False)

    def __str__(self):
        return self.primeiro_nome