"""backend URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from authentication import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='user_login'),
    path('success/', views.user_success, name='user_success'),
    path('user/all/', views.ShowAllUser.as_view(), name='show_user'),
    path('user/search/', views.PhoneSearch.as_view(), name='search_phno'),
    path('user/set_password/', views.reset_password, name='reset_password'),
    path('oauth/', include('social_django.urls', namespace='social')),

]
