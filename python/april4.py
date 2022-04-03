from sympy import symbols, solve
import math

print(math.trunc(solve((symbols('x')+3)/3 - 4/3)[0]))