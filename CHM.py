import os
import sys
from function import *


# Ввод данных
a =  (-3)
b =  (-1)
Epsilon = 0.001
a,b = float(a),float(b)

dont_touch(a,b)


intervall(a,b,Epsilon)

chord(a,b,Epsilon)

tangent(a,b,Epsilon)

combined(a,b,Epsilon)

Iteration(a,b,Epsilon)

