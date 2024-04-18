from django.db import models

class ForeignKeyModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)   
      
class MainModel(models.Model):
    name = models.CharField(max_length=100)
    foreign_key_field = models.ForeignKey(ForeignKeyModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      
