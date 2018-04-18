from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class Media(models.Model):
    name = models.CharField(max_length=50, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=50, blank=True)
    review = models.TextField()
    ch = [(1 , 1), (2 , 2) , (3 , 3) , (4 , 4) , (5 ,5 )]
    ratings = models.PositiveSmallIntegerField(choices=ch , default=1)

    def __str__(self):
        return self.name
