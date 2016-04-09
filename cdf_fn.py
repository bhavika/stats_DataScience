import Cdf
"""
CDF : Cumulative distribution functions

"""


def PercentileRank(scores, target_score):
    count = 0
    for score in scores:
        if score <= target_score:
            count += 1
    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank


def Percentile(scores, percentile_rank):
    scores.sort()
    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
            return score


# This CDF function is almost identical to PercentileRank
def Cdf(t, x):
    count = 0.0
    for value in t:
        if value <= x:
            count += 1.0
    prob = count/ len(t)
    return prob


