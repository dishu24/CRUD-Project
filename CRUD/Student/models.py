from tkinter import Widget
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100 , null=False, blank=False)
    email = models.EmailField(max_length=100,unique=True, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)