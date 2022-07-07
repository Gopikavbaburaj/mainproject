"""Reward_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from Rewrd_Management_App import customer_urls, admin_urls, shop_urls, employee_urls
from Rewrd_Management_App.views import IndexView, Customer_reg, Login, Shop_registration

urlpatterns = [
    path('customer/', customer_urls.urls()),
    path('admin/', admin_urls.urls()),
    path('shop/', shop_urls.urls()),
    path('employee/', employee_urls.urls()),

    path('', IndexView.as_view()),
    path('shop_reg',Shop_registration.as_view()),
    path('register',Customer_reg.as_view()),
    path('login',Login.as_view())


]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
