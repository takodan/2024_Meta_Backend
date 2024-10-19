from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def showform(request): 
    return render(request, "form.html") 

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 