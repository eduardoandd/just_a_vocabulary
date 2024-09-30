from django.db import models

class Vocabulary(models.Model):
    id= models.AutoField(primary_key=True)
    word= models.CharField(max_length=200)
    translation= models.CharField(max_length=200)
    total_hits= models.IntegerField()
    total_errors=models.IntegerField()
