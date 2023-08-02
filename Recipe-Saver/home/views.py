from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

peoples = [
        {'name':'ayush','age':18},
        {'name':'yash','age':15},
        {'name':'adi','age':16},
    ]
context = {'people':peoples}

def home(request):
    return render(request ,'index.html',context)

def about(request):
    return render(request, 'about.html',context)

def contact(request):
    return render(request, 'contact.html',context)