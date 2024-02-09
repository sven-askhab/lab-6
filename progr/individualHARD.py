#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = (a % b == 0) or (b % a == 0)
    print(result * 1)