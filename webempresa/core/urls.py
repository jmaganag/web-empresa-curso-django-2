from django.urls import path
from . import views

urlpatterns = [
     # path del Core
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    #path('services/', views.services, name="services"),
    path('store/', views.store, name="store"),
    ]
