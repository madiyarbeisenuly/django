from django.urls import path
from . import views  # Импортируем views

urlpatterns = [
    path('', views.home_view, name='home'),  # Открывает home.html
    path('pavel/', views.pavel_view, name='pavel'),  # Открывает Pavel.html
]
