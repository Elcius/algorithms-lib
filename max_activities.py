def max_activities(s, f):
    answer = []
    n = len(f)
    # The first activity is always selected
    i = 0
    answer.append(i),
    for j in range(n):
        # If this activity has start time greater than or equal to the finish
        # time of previously selected activity, then select it
        if s[j] >= f[i]:
            answer.append(i),
            i = j
    return answer


def call_max_activities(s, f):
    answer = max_activities(s, f)
    print("The following activties were selected:")
    for x in range(len(answer)):
        print(answer[x])