import math
import matplotlib.pyplot as plt
import collections as c
import random
from __future__ import division


def uniform_cdf(x):
    """ returns the probabiltiy that a uniform random variable is <=x """
    if x < 0: return 0
    elif x < 1: return x
    else: return 1


# A normal distribution is the classic bell curve-shaped distribution and determined by two parameters.
# The mean (mu) indicates where the bell is centered and the standard deviation (sigma) indicates how wide it is.

def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2* math.pi)
    return (math.exp(-(x-mu) ** 2)/2/sigma ** 2)/ (sqrt_two_pi * sigma)


def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x-mu) / math.sqrt(2)/sigma)) / 2


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""
    #if not standard, compute standard and rescale

    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z)/2
        mid_p = normal_cdf(mid_z)

        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z


def bernoulli_trail(p):
    return 1 if random.random() < p else 0


def binomial(n,p):
    return sum(bernoulli_trail(p) for _ in range(n))


def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]
    histogram = c.Counter(data)

    plt.bar([x-0.4 for x in histogram.keys()],
           [v / num_points for v in histogram.values()],
           0.8, color='0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1-p))

    #use a line chart to show the normal approximation
    xs = range(min(data), max(data)+1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i-0.5, mu, sigma)
         for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial distribution vs. Normal approximation")