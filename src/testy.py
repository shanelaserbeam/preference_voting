from Preference_Schedule import PreferenceSchedule

ps1 = PreferenceSchedule()



ps1.generic_vote(num_ballots = 12, num_candidates=5, num_ranks=5)

# print PreferenceSchedule.__version__
# ps1.print_ballots()

print "*"*5
ps1.find_plurality_winner()
