from django.test import TestCase
from django.utils import timezone
from .helpers import find_winner, current_elections
from .models import Election


class VoteCount(TestCase):
    def test_determination_of_winner(self):
        with self.subTest('one winner'):
            winner = find_winner(
                [
                    ['a', 'b', 'c', 'd', 'e'],
                    ['b', 'a', 'e'],
                    ['a', 'c', 'd'],
                    ['c', 'b', 'a', 'd', 'e'],
                    ['c', 'b', 'a', 'e', 'd']
                ], 5
            )
            self.assertIn('a', winner)
            self.assertEqual(1, len(winner))

        with self.subTest('tied winners'):
            winner = find_winner(
                [
                    ['a', 'b', 'c', 'd', 'e'],
                    ['b', 'a', 'c', 'e'],
                    ['a', 'c', 'd'],
                    ['c', 'b', 'a', 'd', 'e'],
                    ['c', 'b', 'a', 'e', 'd']
                ], 5
            )
            self.assertIn('a', winner)
            self.assertIn('c', winner)
            self.assertEqual(2, len(winner))


class CurrentElections(TestCase):
    def test_correct_elections_returned(self):
        # Some dates
        today = timezone.now()
        yesterday = today - timezone.timedelta(days=1)
        tomorrow = today + timezone.timedelta(days=1)
        last_week = today - timezone.timedelta(days=7)
        # Past, closed election
        election = Election(open=last_week, close=yesterday)
        election.save()
        # Currently open election, scheduled end date
        open_election_1 = Election(open=yesterday, close=tomorrow)
        open_election_1.save()
        # Currently open election, no end date
        open_election_2 = Election(open=yesterday)
        open_election_2.save()
        # Not yet open election
        election = Election(open=tomorrow)
        election.save()

        # All elections we created are present in the db
        self.assertEqual(Election.objects.count(), 4)
        result_set = current_elections()
        # Only 2 (the open ones) are in the results, and it's the right 2
        self.assertEqual(result_set.count(), 2)
        self.assertIn(open_election_1, result_set)
        self.assertIn(open_election_2, result_set)
