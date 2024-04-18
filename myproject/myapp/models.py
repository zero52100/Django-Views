from django.db import models

class ForeignKeyModel(models.Model):
    name = models.CharField(max_length=100)

class MainModel(models.Model):
    name = models.CharField(max_length=100)
    foreign_key_field = models.ForeignKey(ForeignKeyModel, on_delete=models.CASCADE)
