from django.urls import path 

from . import views

app_name = "reviews"

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('review/<int:id>', views.detail, name="detail"),
]