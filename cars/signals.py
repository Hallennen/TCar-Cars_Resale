from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import car, CarInvetory
import smtplib,  email.message
from django.db.models import Sum

def car_invetory_update():
    car_count = car.objects.all().count()
    car_value = car.objects.aggregate(
            total_value= Sum('value')         
        )['total_value']
    
    CarInvetory.objects.create(
        cars_count = car_count,
        cars_value = car_value
    )


@receiver(pre_save,sender=car)
def pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = f'''{instance.model} - {instance.brand} ano {instance.factory_year}, é um veiculo de consumo baixo por kilometragem, excelente para uso na cidade para passeios.
                Oportunidade única para aquisição, pelo valor de R$ {instance.value} 
            '''



# se acrescentar o created no parametro, verifica se é criação ou update

@receiver(post_save,sender= car)
def car_post_save(sender, created, instance, **kwargs):
    car_invetory_update()
    # try:
    #     if created:
    #         corpo_email= f"""
    #         <h1> Um novo carro foi cadastrado na sua revenda. </h1> 
    #         <p> O veiculo: <strong>{instance.model}</strong> foi cadastrado.  </p>
    #         <p> Marca: <strong>{instance.brand}</strong></p>
    #         <p> Placa: <strong>{instance.plate}</strong></p>
    #         <p> Valor: <strong>{instance.value}</strong></p>

    #         """

    #         message = email.message.Message()
    #         message["Subject"] = "Novo cadastro - TCAR"
    #         message["From"] = "hallennenm@gmail.com"
    #         message["To"] = "hallennen.marinho3@gmail.com"
    #         password = "yryfxqhznnwnaatk"
    #         message.add_header('Content-Type', 'text/html')
    #         message.set_payload(corpo_email)
            
    #         # creates SMTP session
    #         s = smtplib.SMTP('smtp.gmail.com', 587)
    #         # start TLS for security
    #         s.starttls()
    #         # Authentication
    #         s.login(message["From"], password)
    #         # sending the mail
    #         s.sendmail(message["From"], message["To"], message.as_string().encode('utf-8'))
    #         # terminating the session
    #         s.quit()

    #         print('email enviado para:' , message["To"] )
    # except:
    #     print('NÃO foi possivel enviar o email!')




@receiver(post_delete,sender= car)
def delete_car_invetory(sender, instance, **kwargs):
    car_invetory_update()
