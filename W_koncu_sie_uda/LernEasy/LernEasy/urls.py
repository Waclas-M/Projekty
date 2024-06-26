"""
URL configuration for LernEasy project.

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
from django.contrib.auth import views as auth_views
from django.urls import path , include
from users import views as user_views
from fiszki import views as fiszki_views
from Profile import views as Profile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WelcomeSite.urls')),
    path('rejestracja/', user_views.register, name='register'),
    path('Zacznij_Się_Uczyć/', fiszki_views.fiszkiapp, name='app_fiszki'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',  auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('Profile', Profile_views.profile_tem, name="Profile")
]
