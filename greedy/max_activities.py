def max_activities(s , f):
    n = len(f)
    answer = []

    # The first activity is always selected
    i = 0
    answer.append(i),

    # Consider rest of the activities
    for j in xrange(n):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            answer.append(j),
            i = j
    print(answer)
def call_max_activities(s, f):
    answer = max_activities(s, f)
    print(answer)