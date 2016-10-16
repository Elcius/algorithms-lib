# some_file.py
import sys
sys.path.insert(0, 'greedy')

# Algoritmos gulosos
# Samuel
from shortest_path import shortest_path, call_shortest_path
from colored_graphs import colored_graphs, call_colored_graphs
# Elcius
from max_activities import max_activities, call_max_activities
from fractional_knapsack import Item, fractional_knapsack, call_fractional_knapsack
# Victor

sys.path.insert(0, 'dynamic')
# Algoritmos dinamicos
# Samuel
from lcs import lcs, call_lcs
from max_knapsack import max_knapsack, call_max_knapsack
from edit_distance import edit_distance, call_edit_distance
# Elcius
from is_subset_sum import is_subset_sum, call_is_subset_sum
from matrix_chain_order import matrix_chain_order, call_matrix_chain_order
from binomial_coefficient import binomial_coefficient, call_binomial_coefficient
# Victor
