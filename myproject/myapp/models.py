from django.db import models
from django.utils import timezone

class ForeignKeyModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)  # Manually defined default value
    updated_at = models.DateTimeField(auto_now=True)   

class MainModel(models.Model):
    name = models.CharField(max_length=100)
    foreign_key_field = models.ForeignKey(ForeignKeyModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)  # Manually defined default value
    updated_at = models.DateTimeField(auto_now=True)  
