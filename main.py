import numpy as np
import sympy as sp
from sympy.abc import x

f = x**2 - 3*x + 2

limit_value = sp.limit(f, x, 1)
print(limit_value)
