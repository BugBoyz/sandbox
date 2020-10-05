from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    author = models.CharField(max_length=25)
    date = models.DateField()
    tags = models.CharField(max_length=30)


class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=32)


"""
pep8 

DRF - django rest framework
"""