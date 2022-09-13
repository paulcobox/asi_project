from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Project(models.Model):

  name = models.CharField(max_length=200)
  district = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=6, decimal_places=2)

  
  def __str__(self):
    return self.name




class Search(models.Model):

  name = models.CharField(max_length=200)
  author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)

  
  def __str__(self):
    return self.name