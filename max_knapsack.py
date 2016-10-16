def max_knapsack(cap, weight, value, n):
    if n == 0 or cap == 0:
        return 0
    if (weight[n - 1] > cap):
        return max_knapsack(cap, weight, value, n - 1)
    else:
        return max(value[n - 1] + max_knapsack(cap - weight[n - 1], weight, value, n - 1),
                   max_knapsack(cap, weight, value, n - 1))

def call_max_knapsack(cap, weight, value, n):
    answer = max_knapsack(cap, weight, value, n)
    return "Maximum total value in the knapsack: " + str(answer)