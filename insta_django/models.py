from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length=1024)
    filename = models.CharField(max_length=1024)
    file = models.BinaryField()

