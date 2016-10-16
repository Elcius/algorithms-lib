import algorithms

def test_colored_graphs():
    colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']
    graph_dict = {0: [1, 2, 5], 1: [0, 2, 3, 4], 2: [
        0, 1, 3, 4], 3: [1, 2], 4: [1, 2], 5: [0]}
    algorithms.call_colored_graphs(graph_dict, colors)


def test_shortest_path():
    graph = {0: {1: 2, 3: 2}, 1: {0: 2, 2: 6}, 2: {1: 6}, 3: {0: 0}}
    sp = algorithms.call_shortest_path(graph, 0)


def test_fractional_knapsack():
    W = 50
    items_list = [algorithms.Item(60, 10), algorithms.Item(40, 10), algorithms.Item(50, 30)]

    result = algorithms.call_fractional_knapsack(W, items_list, len(items_list))
    print(result)


def test_max_activities():
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    algorithms.call_max_activities(s, f)


def test_max_knapsack():
    value = [60, 100, 120]
    weight = [10, 20, 30]
    cap = 50
    print algorithms.call_max_knapsack(cap, weight, value, len(value))


def test_edit_distance():
    str1 = "sunday"
    str2 = "saturday"
    algorithms.call_edit_distance(str1, str2)



def test_lcs():
    str1 = "halalkjfa"
    str2 = "jhkfahfljaflkajflkjaflkajlkj"
    algorithms.call_lcs(str1, str2, len(str1), len(str2))

def test_is_subset_sum():
    vecs_and_sums = []
    vecs_and_sums.append([3, 34, 4, 12, 5, 2])
    vecs_and_sums.append(12)
    vecs_and_sums.append([3, 34, 4, 33, 55, 11, 1, 12, 5, 2])
    vecs_and_sums.append(0)
    vecs_and_sums.append([7, 2, 68, 3, 3, 34, 4, 12, 5, 2])
    vecs_and_sums.append(34)
    vecs_and_sums.append([234, 45, 123, 6675, 3, 2])
    vecs_and_sums.append(100)
    vecs_and_sums.append([345, 45, 563, 5, 4, 12, 5, 2])
    vecs_and_sums.append(44)
    vecs_and_sums.append([3, 34, 4, 12, 5, 2])
    vecs_and_sums.append(56)
    vecs_and_sums.append([3, 34, 4, 33, 55, 11, 1, 12, 5, 2])
    vecs_and_sums.append(345)
    vecs_and_sums.append([7, 2, 68, 3, 3, 34, 4, 12, 5, 2])
    vecs_and_sums.append(2)
    vecs_and_sums.append([234, 45, 123, 6675, 3, 34, 5, 2])
    vecs_and_sums.append(6675)
    vecs_and_sums.append([345, 45, 563, 5, 56])
    vecs_and_sums.append(200)
    algorithms.call_is_subset_sum(vecs_and_sums)

def test_matrix_chain_order():
    arr = [1, 2, 9, 7, 3]
    algorithms.call_matrix_chain_order(arr)


def test_binomial_coefficient():
    n = 5
    k = 2
    algorithms.call_binomial_coefficient(n, k)

# Para testar o exemplo dos algoritmos basta retirar o comentário
# test_shortest_path()
# test_colored_graphs()
# test_fractional_knapsack()
# test_max_activities()
# test_lcs()
# test_max_knapsack()
# test_edit_distance()
# test_is_subset_sum()
# test_matrix_chain_order()
# test_binomial_coefficient()