from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)

    @property
    def as_string(self):
        return str(self)

    def __str__(self):
        return self.title + ' by ' + self.author
