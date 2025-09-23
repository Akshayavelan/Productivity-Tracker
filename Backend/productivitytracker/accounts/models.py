from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Profile(AbstractUser):
    ROLE_CHOICES = (
        ('employee','Employee'),
        ('manager','Manager'),
        ('admin','Admin')
    )
    role = models.CharField(max_length=20,choices=ROLE_CHOICES, default='employee')

    def __str__(self):
        return f"{self.username} ({self.role})"
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"