# Основы Python 2 02/04/2023
# TODO - отличие списков от кортежей
# TODO - задачки
# TODO - условный оператор if
# TODO - операторы цикла while, for
# TODO - однострочники


# Задача 1
# Приведен список покупок в магазине

# shop_list = ['Картофель','Горошек', 'Рис','Хлеб']

# # Изучаем объект за переменной shop_list
# # from pprint import pprint
# # print(type(shop_list))
# # pprint(dir(shop_list))

# shop_list.insert(2, 'Рыба')
# print(shop_list )

# # Измените список согласно пунктам задания
# # Выведите результат каждого пункта на консоль по очереди

# #   a. Вставьте рыбу между горошком и рисом
# #   b. Дабавьте фпукты из списка fruits в конец списка shop_list

# fruits = ['Яблоко','Апельсин', 'Клубника']

# # shop_list.append(fruits)
# # print(shop_list)

# shop_list.extend(fruits)
# print(shop_list)

# #   c. Удалите из списка shop_list картофель

# # obj = shop_list.pop(0)
# # print(obj, shop_list)

# shop_list.remove('Картофель')
# print(shop_list)

# #   d. Какими по счету стоят хлеб и апельсин? Выведите номер на консоль
# #   в формате Номер "продукта" в списке - N _  

# # Как выоводить строки на экран
# bread_pos = shop_list.index('Хлеб')
# print('Номер "продукта" в списке - N', bread_pos)
# print('Номер "продукта" в списке - N ' + str(bread_pos))
# print('Номер "продукта" в списке - N {}'.format(bread_pos))
# # 'http://www.website.com/{}/{}/{}/'.format() - очень легко запутаться
# print(f'Номер "продукта" в списке - N {bread_pos}')

# # Отличие списка от кортежа?
# # Список
# shop_list = ['Картофель','Горошек', 'Рис','Хлеб']

# Кортеж - неизменяемый список
# rainbow = ('Red', 'Green,' 'Blue')
# # print(dir(rainbow))

# # Проблема изменяемых объектов
# new_lst = shop_list
# new_lst.append('Что - то вкусное')
# print(new_lst)
# print(shop_list)
# print(id(shop_list))
# print(id(shop_list) == id(new_lst))

# new_tpl = rainbow
# new_tpl = new_tpl + ('Violet',)
# print(rainbow)
# print(new_tpl)
# print(id(new_tpl) == id(rainbow))

# Кортеж работает быстрее, чем список

# x,y = 1, 2
# for pair in enumerate(rainbow):
#     print(pair)

# Условный оператор if

# x = 0

# if x > 0:
#     print('x больше 0')
# elif x < 0:
#     print('х меньше 0')
# else:
#     print('x равен 0')

# print('Условие отработало')

# Про эластичность
# elasticity_dem = 1
# if elasticity_dem == 0:
#     print('Товары первой необходимости')
#     result = 0.0
# elif 0 < elasticity_dem < 1:
#     print('Нормальные блага')
#     result = 0.5
# elif elasticity_dem > 1:
#     print('Роскошь')
#     result = 3.0
# else:
#     print ('Товары низкого качества')
#     result = -1.0
#     if elasticity_dem == 1:
#         print ('Единичная эластичность')
#         result = 1.0
# print('значение =',result)

# # Альтернатива if - elif
# try:
#     x = [1, 2, 3][4]
# except IndexError:
#     x = [1, 2, 3][-1]

# print(x)

# Задача 2
# Создайте список списков населения перечисленных городов

# population = [
#     ['Москва', 8000000],
#     ['Казань', 3000000],
#     ['Нижний Новгород', 1000000]
#     ]

# Выведите на консоль население второго города в списке
# в формате Население Москвы - ХХ человек

# Выведите на консоль общий размер населения перечисленных городов как сумму
# Итого размер населения - ХХ человек

# print(population[0][1] + population[1][1] + population[2][1])

# total = population[0][1] + population[1][1] + population[2][1]

# Циклы for и while
# for перебирает элементы внутри массива

# total = 0
# for i in population:
#     #  print(i[1])
#     total += i[1]
# print(total)

# room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]
# for price in room_prices:
#     if price == max(room_prices):
#         continue

#     if price == min(room_prices):
#         print('Минимальная цена:', price)
#         break

#     print('Текущая цена:', price)
# else:
#     print('Такой цены нет!')

# print('До свидания!')


# for i in [1,2]:
#     pass

# for city, people in population:
#     print(f'Население города{city} - {people} человек')

# for i in population:
#      print(f'Население города{i[0]} - {i[1]} человек')

# for ind in range(len(population)):
#      print(f'Населения города {population[ind][0]} - {population[ind][1]} человек')

# i = -1
# while i < len(population)-1:
#      i += 1
#      print(f'Населения города {population[i][0]} - {population[i][1]} человек')
     
# (i,y) = [Москва, 0000]

# i = 0
# while i < 10:
#     i += 1
#     print('i=',i)

# room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]

# for ind, elem in enumerate(room_prices):
#      print(ind,elem)
# i = -1
# while i < len(room_prices):
#     i += 1
#     price = room_prices[i]
#     print('Проверяем ', price)
#     if price == min(room_prices):
#         print('Найдена минимальная цена')
#         break

# for city, people in population:
#     print(f 'Население города{city} - {people} человек')

# for i in population:
#      print(f'Население города{i[0]} - {i[1]} человек')

# Однострочники

employees = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}

# # Вариант 1
# top_mgrs = []
# for i in employees:
#     if employees[i] >= 100000:
#         top_mgrs.append(i)

# print(top_mgrs)

# Вариант 2 однострочник 

top_mgrs = [i for i in employees if employees[i] >= 100000]
print(top_mgrs)

# if

# flag = True if employees ['Alice'] >= 100000 else False
# # однострочник for

# for i in employees:
#     print(i)

# lst = [i for i in employees]
# print(lst)

# Что такое словари?

# lst = [1,2]
# tpl = (1,2)
# dct = {}

# capitals = {'Россия' : 'Москва'}  
# # print(capitals['Россия'])
# capitals['Италия'] = 'Рим'
# print(capitals)