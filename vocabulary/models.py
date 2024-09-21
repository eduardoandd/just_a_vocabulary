from django.db import models


class Type(models.Model):
    id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Vocabulary(models.Model):
    id= models.AutoField(primary_key=True)
    word= models.CharField(max_length=100)
    translation= models.CharField(max_length=100)
    type=models.ForeignKey(Type,on_delete=models.PROTECT, related_name='vocabulary_type')
    photo=models.ImageField(upload_to='photo/',blank=True,null=True)
    total_hits= models.IntegerField()
    total_errors=models.IntegerField()
    
    def __str__(self):
        return self.word
    
    
    
