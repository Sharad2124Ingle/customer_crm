from django.db import models
from django.contrib.auth.models import User
from django import forms
#from .models import Record

# Create your models here.
class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=10) # we dont do any math on this field, so no need of numfield
    vehicle = models.CharField(max_length=15) 
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=6) # we dont do any math on this field, so no need of numfield
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return(f"{self.first_name} {self.last_name}")
    #return self.user.username




