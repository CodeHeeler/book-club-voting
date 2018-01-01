from django.test import TestCase
from .helpers import find_winner


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
