from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  age = models.IntegerField(null = True)
  DOB = models.DateField(null = True)
  city = models.CharField(max_length=255, null = True)