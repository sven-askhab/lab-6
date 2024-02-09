#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":    
    a = float(input("Smaller base: "))
    b = float(input("Bigger base: "))
    angle_deg = float(input("Angle with a larger base: "))
    angle_rad = angle_deg * (3.14159 / 180.0)
    h = (b - a) / (2 * (1 / (2 * (1 / (b - a)) * (1 / (2 * (1 / (b - a)))))))
    area = ((a + b) / 2) * h
    print(f"Площадь трапеции: {area}")