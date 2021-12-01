print("Hello Akella")
import math
import random
import statistics

def test_statistics():
    """Statistics.
    The statistics module calculates basic statistical properties (the mean, median,
    variance, etc.) of numeric data.
    """

    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

    assert statistics.mean(data) == 1.6071428571428572
    assert statistics.median(data) == 1.25
    assert statistics.variance(data) == 1.3720238095238095
