import sys


def matrix_chain_order(arr, n):

    # One extra row and one extra column are allocated in matrix
    matrix = [[0 for x in range(n)] for x in range(n)]

    # Cost is zero when multiplying one matrix.
    for i in range(1, n):
        matrix[i][i] = 0

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            matrix[i][j] = sys.maxsize
            for k in range(i, j):

                # q = cost/scalar multiplications
                q = matrix[i][k] + matrix[k + 1][j] + \
                    arr[i - 1] * arr[k] * arr[j]
                if q < matrix[i][j]:
                    matrix[i][j] = q

    return matrix[1][n - 1]


def call_matrix_chain_order(arr):

    print("Minimum number of multiplications is " +
          str(matrix_chain_order(arr, len(arr))))
