def is_subset_sum(set, total_sum):

    length_set = len(set)

    subset = [[x for x in range(length_set + 1)]
              for y in range(total_sum + 1)]        # Two-dimensional array

    for numb in range(0, length_set + 1):  # if sum is 0, true is returned
        subset[0][numb] = True

    # If sum isn't 0 and set is empty, the answer is false
    for numb in range(1, total_sum + 1):
        subset[numb][0] = False

    # Fill the table in botton up manner
    for i in range(1, total_sum + 1):
        for j in range(1, length_set + 1):
            subset[i][j] = subset[i][j - 1]

            if(i >= set[j - 1]):
                # Divide in two subproblems.
                subset[i][j] = subset[i][j] or subset[i - set[j - 1]][j - 1]

    return subset[total_sum][length_set]

def call_is_subset_sum(vecs_and_sums):
    for i in range(0, len(vecs_and_sums), 2):
        if(is_subset_sum(vecs_and_sums[i], vecs_and_sums[i + 1]) == True):
            print("Subset with sum '" +
                  str(vecs_and_sums[i + 1]) + "' was found: " + str(vecs_and_sums[i]))
        else:
            print("Sum '" + str(vecs_and_sums[i + 1]) +
                  "' not found:" + str(vecs_and_sums[i]))