"""build_djangoP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from pages.views import index_view, contact_view, about_view, blog_view, elements_view, facilities_view, main_view, property_view, sing_blog_view

urlpatterns = [
    path('', index_view, name='index'),
    path('index/', index_view, name='index'),
    path('contact/', contact_view, name='contact'),
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('blog/', blog_view, name='blog'),
    path('elements/', elements_view, name='elements'),
    path('facilities/', facilities_view, name='facilities'),
    path('sing_blog/', sing_blog_view, name='sing_blog'),
    path('admin/', blog_view, name='blog'),
    path('property/', property_view, name='property'),   
]