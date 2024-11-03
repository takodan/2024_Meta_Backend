from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404


# return all menu item
@api_view()
def menu_item(request):
    item = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(item, many=True)
    return Response(serialized_item.data)

# return menu item by id
@api_view()
def single_item(request, id):
    # item = MenuItem.objects.get(pk=id)
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)