# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Cuisine(models.Model):
    name = models.CharField(max_length=120)


    def __unicode__(self):
        return "{} - {}".format(self.name, self.id)

class Food(models.Model):
    genre_dict = {
        "Çorbalar": "Ç", "Yemek": "Y",
        "Atıştırmalık" : "A", "Salata": "S", "Tatlı": "T"
    }
    GENRE_CHOICES = [(code, label) for label, code in genre_dict.items()]
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    recipes = models.TextField()
    genre = models.CharField(max_length=80, blank=True, choices=GENRE_CHOICES)
    preparation_time = models.CharField(max_length=30)
    cover = models.ImageField( upload_to = "cover_imgs", blank = True )
    top = models.IntegerField(default=0)
    cuisine = models.ForeignKey('Cuisine', on_delete=models.CASCADE, blank=True)

    def __unicode__(self):
        return "{} - {}".format(self.title, self.id)



    def get_cat_name(self):
        for key in self.genre_dict:
            if self.genre_dict[key] == self.genre:
                return key

def add_cat_names(request):
    return{"categories":Food.genre_dict.keys()}

class Comment (models.Model):
    title = models.CharField(max_length=80)
    user=models.CharField(max_length=250)
    body = models.TextField(blank=True)
    food= models.ForeignKey('Food', on_delete=models.CASCADE, blank=True,related_name="comments")
    rating = models.IntegerField(blank=True)
    def __str__(self):
        return self.user