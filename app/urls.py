from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.cars_views, name='cars_list'),
    path('new_car/', views.new_car_view, name= 'new_car'),
    path('new_user/', views.new_user_view, name='new_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
