from django.db import models

# Create your models here.
class Course(models.Model):
    cid = models.CharField(max_length=64,primary_key=True)
    name = models.CharField(max_length=64)
    teacher = models.CharField(max_length=64)