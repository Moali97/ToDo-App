from django.db import models


class List(models.Model):
    title = models.CharField(max_length=250, default='')
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title[:25]
