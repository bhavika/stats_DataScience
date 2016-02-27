import math
from collections import Counter
import matplotlib.pyplot as plt
from linear_algebra import make_matrix, shape, get_column
from statistics import correlation


def bucketize(point, bucket_size):
    """floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point/bucket_size)


def make_histogram(points, bucket_size):
    return Counter(bucketize(points, bucket_size) for point in points)


def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()


def correlation_matrix(data):
    """
    :param data:
    :return: num_columns x num_columns matrix whose (i,j)th entry is the
    correlation between columns i and j of data
    """
    _, num_columns = shape(data)

    def matrix_entry(i, j):
        return correlation(get_column(data, i), get_column(data, j))

    return make_matrix(num_columns, num_columns, matrix_entry)
