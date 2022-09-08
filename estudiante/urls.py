"""estudiante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from applications.carreras.views import *
from applications.estudiantes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentsView.as_view()),
    path('home/', HomeView.as_view()),
    path('carrers/', CarrersView.as_view()),
    path('carrersByInput/', CarrerViewByInput.as_view()),
    path('students/', StudentsView.as_view()),
    path('add-student/', StudentCreateView.as_view()),
    path('updt-student/<pk>/', StudenteUpdateView.as_view()),
    path('del-student/<pk>/', StudentDeleteView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)
