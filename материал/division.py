# -*- coding: utf-8 -*-
"""division.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RrsSdBJr7pzStD-JF-9qLlzSIzHBPT9l
"""

a=int(input("Введи делимое"))
 b=int(input("Введи делитель"))
 try:
   x=a//b
   print(x)
 except ZeroDivisionError:
   print('на 0 делить нельзя!!!')
 finally:
   print("Сработал блок файнали")

import random
x=random.randint(0,100)
print(x)

import random
arr = [1,2,3,4,5,'test1','test2','test3']
#print ("Случайное значение: ", random.choice(arr))
#print(arr[1])
#print(len(arr))
print(type(arr))

import random
y=random.random()
#print(y)
print(type(y))

import random
y=random.uniform(2.5,31.8)
print(y)

import random
a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)
d = random.randint(1,6)
totalSum = a+b+c+d
print ("Бросок 1", a, "Бросок 2", b, "Бросок 3", c, "Бросок 4", d)
print (totalSum)

import random

k=4
y=[]

while k!=0:
  x=random.randint(1,6)
  k-=1
  y.append(x)
  print(y)
print("Сумма 4 бросков:", sum(y))

import random

k=4
y=[]
total = 0

while k!=0:
  x=random.randint(1,6)
  k-=1
  y.append(x)
  print(y)
for i in y:
  print ("Значение i", i, "Значение total", total)
  total+=i

print ("Суммарное значение:", total)

import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
length = input('Длинна пароля:' + "\n")
password = ""

try:
  length = int(length)
  for i in range(length):
      password += random.choice(chars)
  print ("Ваш пароль", password)
except ValueError:
  print ("Ты ввел не цифры, а буквы или символы. Исправься!")
finally:
  password=""
  length = input('Длинна пароля:' + "\n")
  length = int(length)
  for i in range(length):
      password += random.choice(chars)
  print ("Ваш пароль", password)