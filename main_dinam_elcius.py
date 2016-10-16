def call_matrix_chain_order():
    arr = [2, 1, 3, 5]
    size = len(arr)

    print("Minimum number of multiplications is " +
          str(matrix_chain_order(arr, size)))

def call_binomial_coeff():

    n = 5
    k = 2
    print("Value of C(%d,%d) is %d" %
          (n, k, lib_dinam_elcius.binomial_coeff(n, k)))


# Calls
call_matrix_chain_order()
call_is_subset_sum()
call_binomial_coeff()
