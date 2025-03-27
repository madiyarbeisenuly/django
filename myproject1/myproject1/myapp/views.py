from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def pavel_view(request):
    return render(request, 'Pavel.html')  # Убедись, что файл называется именно так!
