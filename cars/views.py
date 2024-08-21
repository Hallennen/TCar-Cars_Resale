from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from cars import models
from cars import forms
from django.views import View
from django.views.generic import ListView , CreateView


# Create your views here.


class CarListView(ListView):
    model = models.car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains = search)
        return cars




class NewCarView(View):

    def get(self,request):
            form_new_car = forms.CarModelform()
            return render(request, 'new_car.html', {'form': form_new_car})


    def post(self, request):
        form_new_car = forms.CarModelform(request.POST, request.FILES)
        if form_new_car.is_valid():
            form_new_car.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'form': form_new_car})



class NewCarCreateView(CreateView):
    model = models.car
    template_name = 'new_car.html'
    success_url = '/car_list/'
    form_class = forms.CarModelform
    