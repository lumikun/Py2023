# 1. Min, Avg, Max
import statistics
from statistics import median


def get_min_avg_max(seq):
    return (min(seq), statistics.mean(seq), max(seq))


# TODO fix median behaviour to fit the task
def get_min_med_max(seq):
    return (min(seq), median(seq), max(seq))


print(get_min_avg_max([1, 2, 3, 4, 5, 6, 7, 9]))
print(get_min_med_max([1, 2, 3, 2, 7, 6, 7, 9]))
