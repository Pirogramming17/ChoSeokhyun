from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

appname='posts'
urlpatterns = [
    path('', views.ideaHome,name='idea_home'),
    path('idea_create', views.ideaCreate, name="idea_create"),
    path('idea_post/<int:id>', views.ideaDetail, name="idea_detail"),
    path('idea_update/<int:id>', views.ideaUpdate, name="idea_update"),
    path('dev_home', views.devHome,name='dev_home'),
    path('dev_create', views.devCreate, name="dev_create"),
    path('dev_post/<int:id>', views.devDetail, name="dev_detail"),
    path('dev_update/<int:id>', views.devUpdate, name="dev_update"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)