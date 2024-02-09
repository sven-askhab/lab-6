#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sent1 = input('Введите первое предложение: ').split(' ')
    sent2 = input('Введите второе предложение: ').split(' ')

    for word in set(sent1):  
        if word in sent2:
            print(f"{word} входит во второе предложение")
        else:
            print(f"{word} не входит во второе предложение")