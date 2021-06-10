import math
from math import floor
t = int(input())
for T in range(t):
    n = int(input())

    val = floor(math.log2(n))
    pwr = pow(2, val)
    print(pwr - 1)
