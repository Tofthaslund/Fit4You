from django.db import models
from datetime import date


class Blog(models.Model):
    author = ('Fit 4 You')
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(default=date.today)
    image = models.ImageField(default='noimage2.png')

    def __str__(self):
        return self.title
