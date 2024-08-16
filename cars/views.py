from django.shortcuts import render, redirect
from django.http import HttpResponse
from cars import models
from cars import forms


# Create your views here.


def cars_views(request):

    cars = models.car.objects.all().order_by('model')

    search= request.GET.get('search')

    if search:
        cars = models.car.objects.filter(model__icontains = search)

    if len(cars) == 0:
        cars = models.car.objects.all()

    
    return render(request,
            'cars.html',
            {'cars': cars}
            )


def new_car_view(request):  
    if request.method == 'POST':
        form_new_car = forms.CarModelform(request.POST, request.FILES)
        if form_new_car.is_valid():
            form_new_car.save()
            return redirect('cars_list')
    else:
        form_new_car = forms.CarModelform()
    

    
    return render(request,
                  'new_car.html',
                  {'form': form_new_car }
                  )



def new_user_view(request):
    # form_user = forms.Login_user()

    return render(request,
                  'new_user.html',
                #   {'form_new_user': form_user },
                  ) 
