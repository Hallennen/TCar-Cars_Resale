from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars import views
from accounts.views import register_view, login_view, logout_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_views, name='logout'),
    path('cars/', views.cars_views, name='cars_list'),
    path('new_car/', views.new_car_view, name= 'new_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
