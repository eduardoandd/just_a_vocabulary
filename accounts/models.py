from typing import Any
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms



class Insights(models.Model):
    id_insights = models.AutoField(primary_key=True)
    errors_count = models.IntegerField()
    hit_count = models.IntegerField()

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)  
    id_insights = models.ForeignKey(Insights, on_delete=models.PROTECT, related_name='user_insights')
    last_login = models.DateTimeField(null=True, blank=True)  # Adicionando o campo last_login


    