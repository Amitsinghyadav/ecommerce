"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path,re_path
from django.views.generic import TemplateView

from .import  views

urlpatterns = [
     path('',views.home_page,name='home'),
     path('about/',views.about_page,name='about'),
     path('contact/',views.contact_page,name='contact'),
       path('login/',views.login_page,name='login'),
         path('register/',views.register_page,name='register'),
         path('bootstrap/',TemplateView.as_view(template_name='bootstrap/example.html'),name=''),
         re_path(r'^products/',include("products.urls",namespace='products')),
         re_path(r'^search/',include("search.urls",namespace='search')),
         re_path(r'^cart/',include("carts.urls",namespace='cart')),
        
       
        path('admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns=urlpatterns+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)