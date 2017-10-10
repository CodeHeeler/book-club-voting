from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author
