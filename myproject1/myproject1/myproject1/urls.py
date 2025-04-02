from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('myapp.urls')),  # Подключаем myapp.urls
=======
    path('books/', include('books.urls')),
    path('', include('myapp.urls')),
>>>>>>> c77578be2fabf2f90dc0eb5a02a40d917e2fc77b
]

# Подключаем обработку media файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
