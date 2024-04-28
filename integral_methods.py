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
    n = 4
    a = parameters[0]
    b = parameters[1]
    e = parameters[2]
    h = float((b - a) / n)
    a = initial_a(a, h, m)
    i1 = integral_sum(a, h, n, f)
    while True:
        n *= 2
        a = parameters[0]
        h = float((b - a) / n)
        a = initial_a(a, h, m)
        i2 = integral_sum(a, h, n, f)
        if runge_rule(i1, i2, 2, e):
            return i2, n
        else:
            i1 = i2


def initial_a(a, h, m):
    if m < 0:
        return a
    if m > 0:
        return a + h
    return a + h/2


def integral_sum(a, h, n, f):
    res = 0
    for i in range(n):
        x = a + h * i
        res += f(x)
    return res * h


def trapezoid(i, parameters):
    return


def simpson(i, parameters):
    return


funcs = [f1, f2, f3]
