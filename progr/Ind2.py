#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sent = input('Введите предложение: ')

    found = False
    for i in range(len(sent) - 1):
        if sent[i] == sent[i + 1]:
            print(f'Первая одинаковая пара {i + 1} и {i + 2}')
            found = True
            break

    if not found:
        print('В предложении нет пары одинаковых соседних символов.')