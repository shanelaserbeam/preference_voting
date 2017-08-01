1. create method to accept a preference schedule
2. create method to generate random schedules
  * based on number of candidates
  * max vote/min vote
  * total number of votes
  * with m places for n candidates n > m
  * maximum number of columns (vote types)

3. create vote counting methods
  * Majority Rule/plurality
  * single runoff
  * repeated runoff
  * point-wise (borda count)
  * pair-wise comparisons
4. ability to print schedules
5. ability to run a single test or multiple tests
6. identify ties and use a tie breaker system

Callable as
ps1 = PreferenceSchedule()
ps1.generate_schedule(num_cands=5, num_cols=4)

future:
specify candidate names
plotting (maybe with borda counts)
other selection criteria
