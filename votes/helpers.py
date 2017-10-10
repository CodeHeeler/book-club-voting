from .models import Ballot


def gather_ballots(election):
    """
    For a given election, gets all Ballot objects which relate and returns a vote set
    """
    ballots = Ballot.objects.filter(election=election)
    vote_set = []
    for ballot in ballots:
        vote_set.append(ballot.selections)
    return vote_set


def find_winner(vote_set, number_of_candidates):
    """
    Takes one parameter, which is a list of lists. Each sublist is one person's votes, in order.
    Example:
        Options are A, B, C, D, and E.
        Voter 1 ranks choices as A > B > C > D > E
        Voter 2 ranks choices as B > A > E
        Voter 3 ranks choices as A > C > D
        Voter 4 ranks choices as C > B > A > D > E
        Voter 5 ranks choices as C > A > E > D
        This input will look like:
        [
            [A, B, C, D, E],
            [B, A, E],
            [A, C, D],
            [C, B, A, D, E],
            [C, A, E, D]
        ]
    Using the Borda Count system (https://en.wikipedia.org/wiki/Borda_count), score each option and
    return a list containing all options which tied for first place.
    """

    # Tally points
    result_set = {}
    for ballot in vote_set:
        current_value = number_of_candidates - 1
        for vote in ballot:
            if vote in result_set:
                result_set[vote] += current_value
            else:
                result_set[vote] = current_value
            current_value -= 1

    # Identify winner(s)
    winning_score = max(result_set.values())
    return [candidate for candidate, value in result_set.items() if value == winning_score]
