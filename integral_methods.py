import warnings

import sympy as sp
from scipy import optimize

from functions import *
from runge import runge_rule


def left_rectangles(i, parameters):
    f = funcs[i - 1]
    m = -1
    return rectangles(f, m, parameters)


def right_rectangles(i, parameters):
    f = funcs[i - 1]
    m = 1
    return rectangles(f, m, parameters)


def middle_rectangles(i, parameters):
    f = funcs[i - 1]
    m = 0
    return rectangles(f, m, parameters)


def rectangles(f, m, parameters):
    a = parameters[0]
    b = parameters[1]
    e = parameters[2]
    n = 4
    h = float((b - a) / n)
    a = initial_a(a, h, m)
    i1 = rectangle_sum(a, h, n, f)
    while True:
        n *= 2
        a = parameters[0]
        h = float((b - a) / n)
        a = initial_a(a, h, m)
        i2 = rectangle_sum(a, h, n, f)
        if runge_rule(i1, i2, 2, e) or n > 2 ** 32:
            return i2, n
        else:
            i1 = i2


def initial_a(a, h, m):
    if m < 0:
        return a
    if m > 0:
        return a + h
    return a + h / 2


def rectangle_sum(a, h, n, f):
    res = 0
    for i in range(n):
        x = a + h * i
        res += f(x)
    return res * h


def trapezoid(i, parameters):
    f = funcs[i - 1]
    a = parameters[0]
    b = parameters[1]
    e = parameters[2]
    n = 4
    h = float((b - a) / n)
    i1 = trapezoid_sum(a, h, n, f)
    while True:
        n *= 2
        h = float((b - a) / n)
        i2 = trapezoid_sum(a, h, n, f)
        if runge_rule(i1, i2, 2, e) or n > 2 ** 32:
            break
        i1 = i2
    return i2, n


def trapezoid_sum(a, h, n, f):
    s = 0
    for i in range(1, n):
        s += f(a + h * i)
    return h * ((f(a) + f(a + h * n)) / 2 + s)


def simpson(i, parameters):
    f = funcs[i - 1]
    a = parameters[0]
    b = parameters[1]
    e = parameters[2]
    n = 4
    i1 = simpson_sum(a, b, n, f)
    while True:
        n *= 2
        i2 = simpson_sum(a, b, n, f)
        if runge_rule(i1, i2, 4, e) or n > 2 ** 32:
            break
    return i2, n


def simpson_sum(a, b, n, f):
    h = float((b - a) / n)
    s = f(a) + f(b)
    for i in range(1, n):
        y = f(a + h * i)
        s += 4 * y if i % 2 == 1 else 2 * y
    return s * h / 3


def converges(i, a, b):
    f = funcs[i - 1]
    x = sp.symbols('x')
    sf = f(x)
    if abs(sp.limit(sf, x, a)) == sp.oo:
        return False, True, a
    if abs(sp.limit(sf, x, b)) == sp.oo:
        return False, True, b
    with warnings.catch_warnings(action="ignore"):
        m1 = round(optimize.fmin(lambda t: -f(t), a, disp=0)[0])
        m2 = round(optimize.fmin(lambda t: -f(t), b, disp=0)[0])
    if a <= m1 <= b:
        if abs(sp.limit(sf, x, m1)) == sp.oo:
            return False, False, m1
    if a <= m2 <= b:
        if abs(sp.limit(sf, x, m2)) == sp.oo:
            return False, False, m2
    return True, ':)'


funcs = [f1, f2, f3, f4, f5]
