from django import forms
from django.contrib.auth.hashers import make_password  
from accounts.models import *

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)  
    
    def create_insight(self):
        insight = Insights.objects.create(
            errors_count=0,
            hit_count=0
        )
        return insight
    
    def save(self):
        insights = self.create_insight()
        user = User(
            username=self.cleaned_data['username'],
            id_insights=insights  
        )
        user.password = make_password(self.cleaned_data['password'])  
        user.save()
        return user
