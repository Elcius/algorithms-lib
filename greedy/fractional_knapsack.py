class Item:
    def __init__(self, v, w):
        self.value = v
        self.weight = w

def fractional_knapsack(W, items_list, n):

    # Sorting Item on basis of ration
    new_items_list = sorted(items_list, key=lambda item: item.weight)

    cur_weight = 0   # Current weight in knapsack
    final_value = 0.0    # Result

    for i in range(n):  # Looping through all Items

        # If adding Item won't overflow, add it completely
        if(cur_weight + new_items_list[i].weight <= W):
            cur_weight += new_items_list[i].weight
            final_value += new_items_list[i].value

        # If we can't add current Item, add fractional part of it
        else:
            remain = W - cur_weight
            final_value += new_items_list[i].value * \
                (remain / new_items_list[i].weight)
            break

    return final_value

def call_fractional_knapsack(W, items_list, n):
    final_value = fractional_knapsack(W, items_list, n)
    return ("Final value is: " + str(final_value))