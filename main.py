# Это мой модуль

# print('Название модуля', __name__)

import ex_module
from ex_module import foo, __name__

def foo_2():
     var_1 = 1
     var_2 = 2
     return var_1 + var_2

print(foo_2())

var_1 = 'Привет'

def foo():
    print('Как дела?')

# импорт системного атрибута __name__

print(ex_module.__name__) # ex_module
print(__name__)           # __main__

if __name__ == '__main__': # если данный файл является запускаемым
     print('Название модуля', __name__,'\nЗапуск')
    # app.run()
    # bot.polling()




