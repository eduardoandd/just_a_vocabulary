from django.db import models

class Insights(models.Model):
    id_insights=models.AutoField(primary_key=True)
    errors_count=models.IntegerField()
    hit_count=models.IntegerField()

class User(models.Model):
    id_user=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=15)
    id_insights=models.ForeignKey(Insights,on_delete=models.PROTECT, related_name='user_insights')
    

