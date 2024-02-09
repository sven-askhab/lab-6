#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sent = input('Введите предложение: ')

    mod_sent = ''
    for i, char in enumerate(sent):
        if (i + 1) % 2 == 0 or char.lower() != 'о':
            mod_sent += char

    print('Измененное предложение:', mod_sent)