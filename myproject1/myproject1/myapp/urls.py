from django.urls import path
from .views import home, pavel_page

urlpatterns = [
    path('', home, name='home'),  
    path('pavel/', pavel_page, name='pavel_page'),  
]
