# meu_projeto/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('db.urls')),  # Incluindo as rotas do app
]
