def runge_rule(i1, i2, k, e):
    return abs(i1 - i2) / (2**k - 1) < e
