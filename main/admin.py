# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Food, Cuisine,Comment

class FoodAdmin(admin.ModelAdmin):
    model = Food
    list_display = ["title", "id"]

admin.site.register(Food,FoodAdmin)

class CuisineAdmin(admin.ModelAdmin):
  model = Cuisine
  list_display = ['id', 'name']

admin.site.register(Cuisine, CuisineAdmin)

class CommentAdmin(admin.ModelAdmin):
  model = Comment
  list_display = ['user','title', 'rating', 'food']

admin.site.register(Comment, CommentAdmin)

