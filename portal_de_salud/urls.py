"""
URL configuration for portal_de_salud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from portal_de_salud import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from portal_de_salud.views import contact_view



urlpatterns=[
path('admin/',admin.site.urls),
path('busqueda_medicacion/',views.busqueda_medicacion),
path('buscar/',views.buscar),
path('',views.home, name="Home"),
path('servicios/',views.servicios),
path('contact/', contact_view, name='contact'),
path('contacto/', contact_view, name='contacto'),
path('profesionales/',views.profesionales),]
urlpatterns += staticfiles_urlpatterns()
