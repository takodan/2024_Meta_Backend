from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def request_info(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['add_header'] = "wah"

    content = f"""
        </br>Path: {path}
        </br>Address: {address}
        </br>Scheme: {scheme}
        </br>Method: {method}
        </br>User agent: {user_agent}
        </br>Path info: {path_info}
        </br>
        </br> Response Headers: {response.headers}
    """
    
    return HttpResponse(content, content_type='text/html', charset='utf-8')


def menu(request, item, price):
    content = f"Item: {item} Price: {price}"
    return HttpResponse(content, content_type='text/html', charset='utf-8')

def qryMenu(request): 
    item = request.GET['item'] 
    price = request.GET['price']
    content = f"Item: {item} Price: {price}"
    return HttpResponse(content, content_type='text/html', charset='utf-8') 