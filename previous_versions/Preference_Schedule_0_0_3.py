'''
A module for handling voting by preference schedules.
Includes methods to generate random data and methods to determine winner
based on different counting methodology
'''

import numpy as np

class PreferenceSchedule(object):
    '''
    A class to intialize and run prefrence schedule voting
    '''
    version = "0.0.3"
    __version__ = version

    def __init__(self):
        '''
        initializes a PreferenceSchedule instance

        TODO
        ------------------------------
        create a way to initalize with a numpy array or dictionary
        '''
        self.num_cands = None
        self.candidates = None
        self.ranks = None
        self.schedule = None
        self.number_per_ballot_type = None
        self.ballots = {}

        pass

    def __str__(self):
        '''
        prints out a representation of the preference schedule, by calling a print method

        Parameters:
        ------------------------------------
        None

        Returns:
        ------------------------------------
        None
        '''
        pass
    def print_ballots_table(self):
        '''
        Prints out the ballots in a vertical table format

        Parameters:
        -----------------------------------------------
        None

        Returns:
        -------------------------------------
        None
        {Prints out the table}

        '''
        max_col_width = self._get_max_column_width()
        max_ballot_length = max([len(b) for b in self.ballots])
        for i in xrange(max_ballot_length):
            output = "cand " + str(i+1) + " "*(max_col_width-len(str(i+1))+1)
            for b in self.ballots:
                output += " | " + b[i] + " "*(max_col_width - len(b[i]))
            output += " |"
            print output
        vote_output = "votes " + " "*(max_col_width)
        for b in self.ballots:
            vote_output += " | " + str(self.ballots[b]) \
                    + " "*(max_col_width - len(str(self.ballots[b])))
        vote_output += " |"
        print "="*len(vote_output)
        print vote_output

    def get_generic_candidates(self, num_cands=5):
        '''
        Generates a set of generic candidates based on the number of candidates called.
        Defaults to using letters to represent candidates.

        Parameters:
        -----------------------------------------------
        num_cands : number of generic candidates (default 5)

        Returns:
        -------------------------------------
        None

        '''
        default_cands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.candidates = np.array(list(default_cands[:num_cands]))
        print "Candidates: ", self.candidates

    def generic_vote(self, num_candidates=5, num_ranks=None, num_ballots=5, \
        min_votes = 1, max_votes = 10):
        '''
        Generates a random voting scenario for candidates

        Parameters:
        -----------------------------------------------
        num_candidates : int
            number of candidates to generate (default = 5)

        num_ranks : int
            number of ranks per ballot, if not specified defaults to the number of candidates

        num_ballots : int
            number of different ballots to generate.  (default = 5)

        min_votes : int
            minimum number of votes a ballot could recieve (default = 1)

        max_votes : int
            maximum number of votes a ballot could recieve (default = 10)

        Returns:
        --------------------------------------
        None

        TODO:
        ---------------------------------------
        Implement a way of selecting the number of voters
        '''

        if num_ranks == None:  #uses number of candidates as number of ranks by default
            num_ranks = num_candidates
        self.get_generic_candidates(num_candidates)
        self._make_ballots(num_ballots, num_ranks, min_votes, max_votes)

    def _make_ballots(self, num_ballots, num_ranks, min_votes, max_votes):
        '''
        creates ballots for current setup, called internally

        Parameters:
        -------------------------------------
        num_ranks : int
            number of ranks per ballot, if not specified defaults to the number of candidates

        num_ballots : int
            number of different ballots to generate.  (default = 5)

        min_votes : int
            minimum number of votes a ballot could recieve (default = 1)

        max_votes : int
            maximum number of votes a ballot could recieve (default = 10)

        Returns:
        ----------------------------------
        None
        '''
        self.ballots = {}

        while len(self.ballots) < num_ballots:
            new_ballot = tuple(np.random.permutation(self.candidates)[:num_ranks])
            if new_ballot not in self.ballots:
                self.ballots[new_ballot] = 0
        self.generate_random_votes(min_votes, max_votes)

    def print_ballots(self):
        '''
        Prints out the current ballots

        '''
        for i in self.ballots:
            print i, self.ballots[i]

    def generate_random_votes(self, min_votes=1, max_votes=10):
        '''
        Generates votes for current ballots

        Parameters:
        ------------------------------
        min_votes : int
            minimum number of votes a ballot could recieve (default = 1)

        max_votes : int
            maximum number of votes a ballot could recieve (default = 10)

        Returns:
        ---------------------------------
        None
        '''
        for i in self.ballots:
            self.ballots[i] = np.random.randint(min_votes,max_votes+1)

    def get_plurality_winner(self, break_tie=False):
        '''
        Finds the winner by plurality (number of first place votes)

        Parameters:
        ------------------------------
        break_tie : boolean
            if true, will randomly select a winner from those who tied (default = False).
            if false, will report all candidates who got the plurality of the votes.

        Returns:
        -------------------------------
        list
        '''
        count_dict = {i:0 for i in self.candidates}
        for i in self.ballots:
                count_dict[i[0]] += self.ballots[i]
        max_votes = max(count_dict.values())  # maximum value
        winners = [k for k, v in count_dict.items() if v == max_votes] # getting all keys contai
        if break_tie:
            return [winners[np.random.randint(len(winners))]]
        else:
            return winners


    def report_winner(self, method="plurality", report_tie = True, break_tie=False, \
                        break_method="random"):
        '''
        Reports the winner given due to the chosen method.

        Parameters:
        ------------------------------------
        method : str or list (TBI)
            which method to use to select winner (default = "plurality")

        report_tie : boolean
            if True, will report whether or not a tie has happened

        break_tie : boolean
            if true, will randomly select a winner from those who tied (default = False).
            if false, will report all candidates who got the plurality of the votes.

        break_method : string
            method to break the tie. (default = "random")
            if random, the method will randomly select a winner from the possible winners

        Returns:
        -------------------------------
        None

        TODO:
        ----------------------------------------------
        * allow for a list of methods
        * allow for different methods to break ties (break tie from point by plurality)
        '''
        if method == "plurality":
            winners = self.get_plurality_winner()
            self._format_winner_output(winners, method, report_tie, break_tie)

    @staticmethod
    def _break_tie(winners, break_method="random"):
        '''
        Breaks a tie if it occurs.  (called internally)

        Parameters:
        -----------------------------------
        winners : list
            a list of winners

        break_method : string
            method to break the tie. (default = "random")
            if random, the method will randomly select a winner from the possible winners

        Returns:
        -------------------------------------------
        list of 1 element
        '''
        if break_method == "random":
            tie_winner =  [winners[np.random.randint(len(winners))]]
        return tie_winner

    def _format_winner_output(self, winners, method, report_tie=True, break_tie=False,\
                break_method="random"):
        '''
        makes a print out of the winner

        Parameters:
        ------------------------------------

        winners : list
            list of possible winners

        method : string
            method used to select winner

        report_tie : boolean
            if True, will report whether or not a tie has happened,
            if False, will set break_tie to True to automatically break ties

        break_tie : boolean
            if true, will randomly select a winner from those who tied (default = False).
            if false, will report all candidates who got the plurality of the votes.

        break_method : string
            method to break the tie. (default = "random")
            if random, the method will randomly select a winner from the possible winners

        Returns:
        ----------------------------------------
        None
        '''
        if not report_tie:
            break_tie = True
        if len(winners) > 1 and report_tie:
            print "There was a tie!"

        if len(winners) > 1 and not break_tie:
            for i in winners:
                if i == winners[0]:
                    tie_output = i
                else:
                    tie_output += " and " + i
                    print "Its a tie with", method, "between:", tie_output
        else:
            winners = self._break_tie(winners, break_method)
            print "The winner by", method, "is", winners[0]

    def _get_max_column_width(self):
        '''
        Gets width needed to print out the ballot table in a pretty fashion.
        Based on max width of either the candidate names or vote count

        Parameters:
        -----------------------------------
        None

        Returns:
        -------------------------------------------
        int
        '''
        return max([max([len(c) for c in self.candidates]), \
            max([len(str(self.ballots[b])) for b in self.ballots])])
