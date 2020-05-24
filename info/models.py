from django.db import models
import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date


class User(AbstractUser):
    @property
    def is_doctor(self):
        if hasattr(self, 'doctor'):
            return True
        return False

    @property
    def is_patient(self):
        if hasattr(self, 'patient'):
            return True
        return False



sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class Hospital(models.Model):
    """docstring for Hospital"""
    name =  models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    class_id = models.ForeignKey(Hospital, on_delete=models.CASCADE, default=1)
    USN = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    DOB = models.DateField(default='1998-01-01')

    def __str__(self):
        return self.name


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(primary_key=True, max_length=100)
    doctorassigned = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    DOB = models.DateField(default='1998-01-01')

    def __str__(self):
        return self.name