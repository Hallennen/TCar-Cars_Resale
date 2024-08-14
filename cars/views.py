from django.shortcuts import render
from django.http import HttpResponse
from cars import models

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
       
    
    return render(request,
                  'new_car.html' )
