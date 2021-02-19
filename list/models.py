from django.db import models
from django.urls import reverse


class List(models.Model):
    title = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.title[:50]
