from Preference_Schedule import PreferenceSchedule

ps1 = PreferenceSchedule()



ps1.generic_vote(num_ballots = 2, num_candidates=5, num_ranks=5, max_votes=1)

# print PreferenceSchedule.__version__
# ps1.print_ballots()

print "*"*5
print ps1.get_plurality_winner()
# print ps1.get_plurality_winner(break_tie=True)
ps1.report_winner()
ps1.report_winner(report_tie=False)
