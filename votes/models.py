from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


class Election(models.Model):
    name = models.CharField(max_length=100)
    open = models.DateTimeField(null=True, blank=True)
    # `close` can be set to a time in the future, to schedule the election to close, or can be set to
    # timezone.now() when the election is manually closed. If null, and current time is past `open`,
    # then the election is open.
    close = models.DateTimeField(null=True, blank=True)
    candidates = models.ManyToManyField('books.Book', blank=True)
    winner = models.ForeignKey('books.Book', null=True, blank=True, related_name='election_won')

    @property
    def is_closed(self):
        # True for any election which closed in the past
        return self.close is not None and self.close <= timezone.now()

    @property
    def is_open(self):
        # True for any election which opened in the past AND has not yet closed.
        # False for any future election
        return self.open is not None and self.open <= timezone.now() and (self.close is None or self.close > timezone.now())

    @property
    def not_opened(self):
        return not (self.is_open or self.is_closed)

    def __str__(self):
        return self.name


class Ballot(models.Model):
    election = models.ForeignKey(Election)
    selections = JSONField()  # Should store a list of candidate IDs, in order from most-preferred to least-preferred
