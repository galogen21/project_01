# -*- coding: utf-8 -*-
"""Homework 2.1 lvl 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xbDO8ZC0cSU7YQnKgGw04N7OSDgBKMBs
"""

# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
  year = {1: 'Январь',
          2: 'Февраль',
          3: 'Март',
          4: 'Апрель',
          5: 'Май',
          6: 'Июнь',
          7: 'Июль',
          8: 'Август',
          9: 'Сентябрь',
          10: 'Октябрь',
          11: 'Ноябрь',
          12: 'Декабрь'}
  if 1 <= month <= 12:

    if 1 <= month <= 3:
      print('Месяц', month, year[month], 'является частью первого квартала')
    elif 4 <= month <= 6:
      print('Месяц', month, year[month], 'является частью второго квартала')
    elif 7 <= month <= 9:
      print('Месяц', month, year[month], 'является частью третьего квартала')
    else:
      print('Месяц', month, year[month], 'является частью четвертого квартала')
    return month
  else:
    print('Месяц введен неверно!')

try:
  month = int(input('Введите номер месяца'))
  quarter_of(month)
except ValueError:
  print('В поле можно вводить только цифры!')