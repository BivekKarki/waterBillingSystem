from django.contrib import admin
from django.urls import path

from home import views
from home.views import homeview

app_name = "home"

urlpatterns = [
    path('', homeview, name='home-page'),
]