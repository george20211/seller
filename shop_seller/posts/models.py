#from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Trashed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trololo = models.TextField(null=True)

    def __str__(self):
        return self.trololo