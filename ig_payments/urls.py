"""ig_payments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
# from login.views import login 
from core.views import home, profile
from authentication.views import login_django, register_django, logout_django
from payments.views import payment
from pages.views import page_create, page_view

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', login_django, name='login'),
    path('logout/', logout_django, name='logout'),
    path('register/', register_django, name='register'),
    path('profile/', profile, name='profile'),
    path('payment/', payment, name='payment'),
    path('page/create/', page_create, name='page_create'),
    path('page/view/', page_view, name='page_view'),
]
