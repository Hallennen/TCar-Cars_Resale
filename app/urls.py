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
    path('cars/', views.CarListView.as_view(), name='cars_list'),
    path('new_car/', views.NewCarCreateView.as_view(), name= 'new_car'),
    path('new_brand/', views.NewBrandCreateView.as_view(), name= 'new_brand'),
    path('new_cor/', views.NewCorCreateView.as_view(), name= 'new_cor'),
    path('car/detail/<int:pk>/', views.CarDetailView.as_view(), name='detail_car'),
    path('car/detail/<int:pk>/update/', views.CarUpdateView.as_view(), name='update_car'),
    path('car/detail/<int:pk>/delete/', views.CarDeleteView.as_view(), name='delete_car'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
