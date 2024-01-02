from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples=[
          {"name": "Alice", "age": 14},
          {"name": "Bob", "age": 35},
          {"name": "Charlie", "age": 16},
          {"name": "David", "age": 30},
          {"name": "Frank", "age": 17},
          {"name": "Grace", "age": 60}

    ]
    return render(request, "home/index.html",context={"page":"django 2023","people": peoples})
def about(request):
    context= {"page":"about"}  
    return render(request,"home/about.html",context)
def contact(request):
    context= {"page":"contact"}
    return render(request,"home/contact.html",context)




