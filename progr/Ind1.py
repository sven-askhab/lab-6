#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentence = input('Введите предложение: ')
    character = input('Введите символ для поиска: ')

    print(f'Вхождения символа "{character}" в предложении:')
    for index, char in enumerate(sentence):
        if char == character:
            print(character)