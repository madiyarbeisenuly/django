from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def pavel_page(request):
    return render(request, "Pavel.html")