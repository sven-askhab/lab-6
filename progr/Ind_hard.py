#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Value of x? "))
    n = int(input("Value of n? "))
    
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)
    
    if n == 0:
        print("Illegal value of n", file=sys.stderr)
        exit(1)
    
    a = x
    result, k = a, 1
    
    while math.fabs(a) > EPS:
        a *= (-1) * (x ** 2) / (4 * (k + 1) * (k + n + 1))
        result += a
        k += 1
    
    print(f"J({n})({x}) = {((x / 2) ** n) * result}")