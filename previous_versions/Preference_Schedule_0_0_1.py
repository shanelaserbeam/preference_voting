'''
A module for handling voting by preference schedules.
Includes methods to generate random data and methods to determine winner
based on different counting methodology
'''

import numpy as np

class PreferenceSchedule():
    version = "0.0.1"
    __version__ = version

    def __init__(self):
        self.num_cands = None
        self.candidates = None
        self.ranks = None
        self.schedule = None
        self.number_per_ballot_type = None
        self.ballots = {}

        pass

    def __str__(self):
        pass

    def get_generic_candidates(self, num_cands):
            default_cands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.candidates = np.array(list(default_cands[:num_cands]))
            print "Candidates: ", self.candidates

    def generic_vote(self, num_candidates=5, num_ranks=None, num_ballots=5, \
        min_votes = 1, max_votes = 10):
        if num_ranks == None:  #uses number of candidates as number of ranks by default
            num_ranks = num_candidates
        self.get_generic_candidates(num_candidates)
        self.make_ballots(num_ballots, num_ranks, min_votes, max_votes)

    def make_ballots(self, num_ballots, num_ranks, min_votes, max_votes):
        self.ballots = {}

        while len(self.ballots) < num_ballots:
            new_ballot = tuple(np.random.permutation(self.candidates)[:num_ranks])
            if new_ballot not in self.ballots:
                self.ballots[new_ballot] = 0
        self.generate_votes(min_votes, max_votes)

    def print_ballots(self):
        for i in self.ballots:
            print i, self.ballots[i]

    def generate_votes(self, min_votes=1, max_votes=10):
        for i in self.ballots:
            self.ballots[i] = np.random.randint(min_votes,max_votes+1)

    def find_plurality_winner(self):
        count_dict = {i:0 for i in self.candidates}
        for i in self.ballots:
                count_dict[i[0]] += self.ballots[i]
        max_votes = max(count_dict.values())  # maximum value
        winners = [k for k, v in count_dict.items() if v == max_votes] # getting all keys contai
        if len(winners) == 1:
            print "The winner by plurality is", winners[0], "with a vote count of", max_votes
        else:
            for i in winners:
                if i == winners[0]:
                    tie_output = i
                else:
                    tie_output += " and " + i
            print "Its a tie with pluarlity between:", tie_output, "with a count of", max_votes
