# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from .models import Food, Cuisine, Comment
from .forms import  CommentForm



def index(request):
    foods = Food.objects.all().order_by('-id')[:10]
    top = Food.objects.filter(top=1)
    cuisines = Cuisine.objects.all().order_by('name')[:5]
    context = {"foods": foods,"top":top,"cuisines":cuisines}

    return render(request, "main/index.html", context)

def food_page(request, food_id, title):
    food = get_object_or_404(Food, pk=food_id)

    form_errors = {}
    form_values = {"user": "","title": "", "body": "", "rating": 0}
    if request.POST:
        print("rating=", request.POST["rating"], type(request.POST["rating"]))
        print("comment=", request.POST["yorum"])
        form_values["user"] = request.POST["user"]
        form_values["title"] = request.POST["title"]
        form_values["body"] = request.POST["yorum"]
        form_values["rating"] = int(request.POST["rating"])
        if len(request.POST["title"]) == 0:
            form_errors["title"] = "Başlık yazmalısın"
        if form_values["rating"] == 0:
            form_errors["rating"] = "Yemeği derecelendir"
            if form_values["user"] == 0:
                form_errors["user"] = "Adınızı giriniz"
        if len(form_errors) == 0:
            new_comment = Comment()
            new_comment.user = form_values["user"]
            new_comment.title = form_values["title"]
            new_comment.body = form_values["body"]
            new_comment.food = food
            new_comment.rating = form_values["rating"]
            new_comment.save()

            print("SAVED")

    context = {"food": food }
    return render(request, "main/food.html", context)

def tarif_page(request):
    foods = Food.objects.all()
    context = {"foods": foods}
    return render(request, "main/tarifler.html", context)

def cuisine_page(request, cuisine_id, name):

    cuisine = get_object_or_404(Cuisine, pk=cuisine_id)

    context = {"cuisine": cuisine}
    print(cuisine.food_set.all())
    return render(request, "main/cuisine.html", context)



def cat_page(request, cat):
    cat =cat.capitalize()
    category=Food.genre_dict.get(cat,"")
    food =Food.objects.all().filter(genre=category)
    context={ 'foods': food ,"cat_name":cat}
    return render(request,"main/category.html",context)


def test_forms(request):
    if request.POST:
        form2=CommentForm(request.POST)
        form2.save()
    else:
        form2=CommentForm()
    return render(request, "main/test_forms.html",{'form2': form2})
