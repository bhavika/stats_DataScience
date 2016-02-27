from __future__ import division


def vector_add(v, w):
    """vectorwise component addition"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]


def vector_sum(vectors):
    return reduce(vector_add, vectors)


def scalar_multiply(c,v):
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v,w))


def sum_of_squares(v):
    return dot(v,v)


def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return  num_rows, num_cols


def get_row(A,i):
    return A[i]


def get_column(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """
    :param num_rows: number of rows required
    :param num_cols: number of columns required
    :param entry_fn: function for each (i,j)
    :return: num_rows x num_cols matrix whose (i,j)th entry is entry_fn(i,j)
    """
    return [[entry_fn(i,j) for j in range(num_cols)]
            for i in range(num_rows)]


def is_diagonal(i, j):
    """
     returns 1 for the diagonals, 0 everywhere else
    """
    return 1 if i == j else 0


def matrix_add(A, B):
    if shape(A) != shape(B):
        raise ArithmeticError("Cannot add matrices with different shapes.")
    num_rows, num_cols = shape(A)

    def entry_fn(i, j): return A[i][j] + B[i][j]

    return make_matrix(num_rows, num_cols, entry_fn)

