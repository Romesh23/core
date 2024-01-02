from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def recepi(request):
    if request.method=="POST":
            data=request.POST
            recipe_name=data.get("recipe_name")
            recipe_description=data.get("recipe_description")
            recipe_pic=request.FILES.get("recipe_pic")

            print(recipe_name)
            print(recipe_description)
            print(recipe_pic)

            Recipe.objects.create(
                  recipe_name=recipe_name,
                  recipe_description=recipe_description,
                  recipe_pic=recipe_pic
            )
            
            return redirect("/recepi/")
    queryset=Recipe.objects.all()
    context={"recepi":queryset}
    return render(request,"recepi.html",context)

def update_recepi(request,id):
       queryset=Recipe.objects.get(id=id)
       if request.method=="POST":
            data=request.POST

            recipe_name=data.get("recipe_name")
            recipe_description=data.get("recipe_description")
            recipe_pic=request.FILES.get("recipe_pic")

            queryset.recipe_name=recipe_name
            queryset.recipe_description=recipe_description
            
            if queryset.recipe_pic:
                  queryset.recipe_pic=recipe_pic
            
            queryset.save()
            return redirect("/recepi/")

       context={"recepi":queryset}
       return render(request,"update_recepi.html",context)


def delete_recepi(request,id):
     queryset=Recipe.objects.get(id=id)
     queryset.delete()
     return redirect("/recepi/")
      