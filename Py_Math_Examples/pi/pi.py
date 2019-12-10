'''Algorithm due to Srinivasa Ramanujan, from http://en.wikipedia.org/wiki/Pi'''

import math

def fact(n):
    if n == 0:
        return 1
    else:
        rec = fact(n-1)
        res = n * rec
        return res

def my_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = fact(4*k) * (1103 + 26390*k)
        den = fact(k)**4 * 396**(4*k)
        term = factor * num / den
        total += term
        if abs(term) < 1e-15: break
        k += 1
    return 1 / total

print(my_pi())

 
