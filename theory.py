import dataclasses
import os
import time

# a = 50
# b = 'string'


# print(
#     type(
#         list(b)
#     )
# )

# for i in b:
#     print(i)

# while a < 100:
#     a += 1
#     print(a)

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print(f'Время выполнения функции {func.__name__}: {end_time - start_time} сек')
#
#     return wrapper


# #set / frozenset
#
# @timer
# def waiting():
#     time.sleep(5)
#     print('Hello, world')
#
#
# waiting()

# if a > 0 and b > 0:
#     print(f'Число {a} и число {b} больше 0')
#
# if a > 0 or b < 0:
#     print(f'Число {a} и число {b} больше 0')
#
# if not a < 0:
#     print('some text')


# set_ = {5, 4, 8, 55, 5, 55}
# set_ = frozenset(set_)
# print(set_)
# a = []
# b = []
#
# """Генераторы"""
#
# start = time.time()
#
#
# def gen_1(n):
#     gen_ = range(n)
#     for i in gen_:
#         yield i
#
#
# # @timer
# def gen_2(n):
#     return (i for i in range(n))
#
#
# def gen_3(n):
#     for i in range(n):
#         return i
#
#
# # for j in gen_1(1000000):
# #     print(j)
#
#
# # for j in gen_2(1000000):
# #     print(j)
#
# gen_3(1000000)
#
# end = time.time()
# print(end - start)

# str_ = '\tHello World!\n'
# str_ += 'Text'
# print(str_[1:6:])

# names_list = ['Artem', 'Vasya', 'john']
# names_list[1] = 'Vlad'
# names_list.append('John')
# names_list.insert(1, 'Petya')
# # del names_list[-1]
# print(names_list)
# # names_list.pop(0)
#
# # names_list.remove('Petya')
# names_list.sort(reverse=True)
# print(sorted(names_list))
# print(names_list)
import pysnooper

user_1 = {'login': 'login_1', 'password': 'password_1'}
# print(user_1)
# user_1['email'] = '111@gmail.com'
# # del user_1['email']
#
# print(user_1.get('123', 'Такого ключа не существует'))

users = {
    '10Б': {
        'Иван': 15,
        'Петя': 14,
        'Вова': 15,
    },
    '10А': {
        'Вася': 14,
        'Андрея': 15,
    }
}


def recursive_search(dictionary, search_by):
    """Рекурсивный поиск по вложенным словарям

    :param dictionary: передаваемый словарь (словарь, по которому будем производить поиск)
    :param search_by: параметр, по которому будем производить поиск
    :return: результат поиска
    """
    if search_by in dictionary.keys():
        return dictionary[search_by]

    for value in dictionary.values():
        if type(value) == dict:
            search_by = recursive_search(value, search_by)

    if search_by is not None:
        return search_by
    else:
        return 'Нет элементов, удовлетворяющих условию'


# search = input('Введите имя или класс: ')
# print(f'{search}: {recursive_search(users, search)}')

def rebus():
    K = [i for i in range(1, 10)]
    O = [i for i in range(0, 10)]
    T = [i for i in range(1, 10)]

    for k in K:
        for o in O:
            for t in T:
                KTO = str(k) + str(t) + str(o)
                KOT = str(k) + str(o) + str(t)
                TOK = str(t) + str(o) + str(k)

                current_kto = int(KTO)
                current_kot = int(KOT)
                current_tok = int(TOK)

                if current_kto + current_kot == current_tok:
                    print(f'{current_kto} + {current_kot} = {current_tok}')
                    break


# rebus()

# gen_1 = (i for i in range(10))
#
# gen_2 = [i for i in range(10)]
#
# list_ = []
# for i in range(10):
#     list_.append(i)
#
# for i in gen_1:
#     print(i)
#
# print(gen_2)


# def test_gen():
#     for i in range(10):
#         yield i
#
#
# for j in test_gen():
#     print(j)

# def bus_ticket():
#     numbers = [i for i in range(100000, 9999999)]
#     for i in numbers:
#         number = [int(i) for i in str(i)]
#         sum_ticket_1 = sum(number)
#         sum_ticket_2 = sum(number) + 1
#         if sum_ticket_1 % 7 == 0 and sum_ticket_2 % 7 == 0:
#             print(f'Билет счастливый')
#
#
# bus_ticket()

class Dog:
    """Модель собаки"""

    def __init__(self, name: str, age=None):
        """Инициализация атрибутов name, age

        :param name: Имя собаки
        :param age: Возраст собаки
        """
        self.name = name
        self.age = age

    def sit(self) -> str:
        """Собака садится"""
        return f'{self.name} садится'

    def __str__(self) -> str:
        """Строковое представление объекта собаки

        :return: Строковое представление
        """
        if self.age:
            return f'Имя: {self.name}, Возраст: {self.age}'
        else:
            return f'Имя: {self.name}'


# my_pet = Dog('Vasya')
# print(my_pet.sit())

# print(my_pet)

class Car:
    def __init__(self, make: str, model: str, year: int, odometer=0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def __str__(self) -> str:
        return f'Марка: {self.make}\nМодель: {self.model}\nГод выпуска: {self.year}'

    def get_odometer(self):
        return f'Пробег: {self.odometer} км\n'

    def __add_odometer(self, km: int):
        self.odometer += km


class ElectricCar(Car):
    def __init__(self, make, model, year, odometer, battery_size: int):
        super(Car, self).__init__(make, model, year, odometer)
        self.battery_size = battery_size

    def get_power_reserve(self):
        if self.battery_size < 75:
            return 'Запас хода: < 200 км'
        else:
            return 'Запас хода: > 200 км'


# car_1 = Car('BMW', 'X5', 2019, 25000)
# car_2 = ElectricCar('Tesla', 'Model 3', 2021, 15000, 85)
#
# print(car_1)
# car_1._Car__add_odometer(100)
# print(car_1.get_odometer())
#
# print(car_2)
# print(car_2.get_odometer())
# print(car_2.get_power_reserve())
"""Работа с файлами

r - только для чтения
r+ - для записи и чтения
w - только для записи (создаст новый файл, если файл с таким именем не найден)
w+ - для чтения и записи (создаст новый файл, если файл с таким именем не найден)
rb - чтение бинарного файла
wb - только для записи в .bin файл 
а - откроет файл для добавления новой информации (создаст новый файл, если файл с таким именем не найден)

Привет, меня зовут name
"""


@pysnooper.snoop()
def writer(name: str, param: str):
    if not os.path.exists('files'):
        os.mkdir('files')
    with open(r'files\some_file.txt', f'{param}', encoding='utf-8') as file:
        file.write(f'Привет, меня зовут {name.title()}\n')


def reader():
    with open(r'files\some_file.txt', 'r', encoding='utf-8') as file:
        # text = file.read()
        text = file.readlines()
        print(text)


# for i in range(10):
#     writer('Artem', 'a')

reader()
