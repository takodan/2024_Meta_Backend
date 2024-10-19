
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.request_info, name = "request_info"),
    path('menu/<item>/<price>', views.menu, name = "menu"),
    path('qryMenu/', views.qryMenu, name = "qryMenu"),
]