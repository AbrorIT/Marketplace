from turtle import title
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    decription = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"