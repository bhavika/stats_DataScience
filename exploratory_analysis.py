import math
from collections import Counter
import matplotlib.pyplot as plt
from linear_algebra import make_matrix, shape, get_column
from statistics import correlation
import random

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


def split_data(data, prob):
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results


def train_test_split(x, y , test_pct):
    data = zip(x, y)
    train, test = split_data(data, 1 - test_pct)
    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test


def precision(tp, fp, tn, fn):
    return tp/(tp+fp)


def recall(tp, fp, tn, fn):
    return tp/(tp+fn)



def f1_score(tp, fp, tn, fn):
    """f1_score is the harmonic mean of precision and recall"""
    p = precision(tp, fp, tn, fn)
    r = recall(tp, fp, tn, fn)

    return 2 * p *r / (p+r)

