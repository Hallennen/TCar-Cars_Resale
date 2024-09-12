from typing import Any
from cars import models
from cars import forms
from django.views.generic import ListView , CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = models.car
    template_name = 'new_car.html'
    success_url = '/cars/'
    form_class = forms.CarModelform


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewBrandCreateView(CreateView):
    model = models.Brand
    template_name = 'new_brand.html'
    success_url = '/new_car/'
    form_class = forms.CarBrandForm

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCorCreateView(CreateView):
    model= models.Cor
    template_name = 'new_cor.html'
    success_url = '/new_car/'
    form_class = forms.Corform






class CarDetailView(DetailView):
    model = models.car
    template_name = 'car_detail.html'




@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = models.car
    form_class = forms.CarModelUpdateForm
    template_name = 'car_update.html'
    success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('detail_car', kwargs= {'pk': self.object.pk})
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = models.car
    template_name = 'delete_car.html'
    success_url = '/cars/'