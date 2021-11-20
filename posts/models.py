from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model


class District(models.Model):
    dist = models.CharField(max_length=200)

    def __str__(self):
        return self.dist

class State(models.Model):
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.state

class Country(models.Model):
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.country

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    dists = models.ManyToManyField(District, help_text="District of News", blank=True)
    stats = models.ManyToManyField(State, help_text="State of News", blank=False)
    count = models.ManyToManyField(Country, help_text="News Country", blank=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

