from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    car = models.CharField(max_length=200)
    car_number = models.CharField(max_length=30, unique=True)
    car_color = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.car_number}) "
