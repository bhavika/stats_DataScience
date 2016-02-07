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

