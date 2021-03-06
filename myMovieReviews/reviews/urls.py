from django.urls import path 

from . import views

app_name = "reviews"

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('search', views.search, name="search"),
    path('review/<int:id>', views.detail, name="detail"),
    path('modify/<int:id>', views.modify, name="modify"),
    path('delete/<int:id>', views.delete, name="delete"),
]