from django.urls import path
from . import views

urlpatterns = [
     # path del services
    path('services/', views.services, name="services"),
]
 