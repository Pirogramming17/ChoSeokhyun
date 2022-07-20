from django.contrib import admin
from django.urls import path
from . import views

appname='posts'
urlpatterns = [
    path('', views.index,name='home'),
]