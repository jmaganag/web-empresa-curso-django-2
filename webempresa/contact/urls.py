from django.urls import path
from . import views

urlpatterns = [
     # path del Contact
    path('', views.contact, name="contact"),
    ]
