import os

import bloompy


def get_sbf():
    if os.path.isfile('sbf.suffix'):
        sbf = bloompy.ScalableBloomFilter.fromfile('sbf.suffix')
    else:
        sbf = bloompy.ScalableBloomFilter(error_rate=0.001, initial_capacity=10 ** 3)
        sbf.tofile('sbf.suffix')
        sbf.__contains__()
    return sbf
