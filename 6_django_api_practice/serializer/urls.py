from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.menu_item),
    path('menu/<int:id>', views.single_item),
]