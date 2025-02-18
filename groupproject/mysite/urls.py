"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from registration import views as register_view
from login import views as login_view
from main import views as main_view
from api import views as api_view
from map import views as map_view
from challenge import views as challenge_view
from quiz import views as quiz_view
from challenge import views as challenge_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view.register, name='register'),
    path('login/', login_view.loginPage, name='login'),
    path('home/', main_view.home, name='home'),
    path('admin_api/', api_view.api, name='api'),
    path('', register_view.register, name='register'),
    path('map/', map_view.MapView.as_view(), name='map'),
    path('map/submit/', map_view.submitProcess, name='submitView'),
    path('challenge/', challenge_view.challenge, name='challenge'),
    path('quiz/<int:id>/', quiz_view.quiz, name='quiz'),
    path('challenge/<int:id>/', challenge_view.challenge, name='challenge')
]
