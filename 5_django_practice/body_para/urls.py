from django.urls import path 
from . import views

urlpatterns = [
    path('showform/', views.showform, name = "showform"),
    path("getform/", views.getform, name='getform'),
]