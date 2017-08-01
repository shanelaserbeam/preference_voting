import numpy as np

class PreferenceSchedule():
    __version__ = "0.0.1"

    def __init__(self):
        self.num_cands = None
        self.candidates = None
        self.ranks = None
        self.schedule = None
        self.number_per_ballot_type = None

        pass

    def __str__(self):
        pass

    def get_generic_candidates(self, num_cands):
            default_cands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.candidates = np.array(list(default_cands[:num_cands]))
            print self.candidates

    def generic_vote(self, num_candidates=5, num_ranks=None, num_ballots=5):
        if num_ranks == None:  #uses number of candidates as number of ranks by default
            num_ranks = num_candidates
        self.get_generic_candidates(num_candidates)

    def get_ballots(self, num_ballots):
        pass
