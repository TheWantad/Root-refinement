import os
import sys
from function import *


# Ввод данных
a =  (-3)
b =  (-1)
Epsilon = 0.001
a,b = float(a),float(b)

x = sp.symbols('t')
equation = x**3-3*x**2+9*x-10
#equation = x**3-6*x-8
#equation = x**3-3*x**2+9*x-8
#equation = x**2+4*x+4
#equation = x**3-3*x**2+9*x-10
#equation = x*2**x-1

dont_touch(a,b)


intervall(a,b,Epsilon)

chord(a,b,Epsilon)

tangent(a,b,Epsilon)

combined(a,b,Epsilon)

Iteration(a,b,Epsilon)

