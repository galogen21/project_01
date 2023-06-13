# -*- coding: utf-8 -*-
"""Homework 2.3 lvl_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iGEbhqZptlw6o4wOOLtrN4TjRnrxNKQK
"""

# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
  numbrs = {1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'}
  try:
    num_word = numbrs[number]
    return num_word
  except KeyError:
    print(None)

switch_it_up(int(input()))