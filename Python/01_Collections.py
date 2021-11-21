# Collections - Коллекции

# Коллекция в Python — программный объект (переменная-контейнер), хранящая набор значений одного или различных типов,
# позволяющий обращаться к этим значениям, а также применять специальные функции и методы, зависящие от типа коллекции.
# Стандартные встроенные коллекционные типы данных в Python: список (list), кортеж (tuple), строку (string),
# множества (set, frozenset), словарь (dict).

# Тип коллекции            Изменяемость     Индексированость(Срезы)   Уникальность    Как создать
#                         Сonvertibility        Indexing(Slices)      Originality    How to create

# Строка(string)                -                     +                    -           ' ' , " "

# Список(list)                  +                     +                    -           [], list()

# Кортеж(tuple)                 -                     +                    -           (), tuple()

# Словарь(dict)           + элементы(elements)        -             + элементы         {}, {key: value}, dict()
#                         - ключи(keys)                             + ключи(keys)
#                         + значения(values)                        - значения(values)

# Множество(set)                +                     -                    +           {,}, set()

# Неизменяемое                  -                     -                    +           frozenset()
# множество(frozenset)


# Строка - string  ---  '' , "" , str()
#
# first_string = 'Я текст в одинарных кавычках'
# second_string = 'Слово "Python" обычно подразумевает змею'
#
# my_num = 12345
# my_str = str(my_num)
#
# print(first_string)
# print(second_string)
# print(my_str)
#
# Я текст в одинарных кавычках
# Слово "Python" обычно подразумевает змею
# 12345


# Список - list  ---  a = [] , list()
#
# a = []
#
# b = "Hello 123"   # <class 'str'>
# c = list(b)
#
# print(c)
#
# ['H', 'e', 'l', 'l', 'o', ' ', '1', '2', '3']


# Кортеж - tuple  ---  a = () , tuple()
#
# a = ()
#
# b = (1,)
#
# c = "Hello 123"
# d = tuple(c)
#
# print(b)
# print(d)
#
# (1,)
# ('H', 'e', 'l', 'l', 'o', ' ', '1', '2', '3')


# Словарь - dict  ---  {} , {key: value} , dict()
#
# a = {}
#
# b = {"Hello": "How are you?"}
#
# c = ["12", "he"]    # list
# d = dict(c)
# e = "lo", "34"      # tuple
# f = dict(e)
#
# print(a)
# print(b)
# print(d)
# print(f)
#
# {}
# {'Hello': 'How are you?'}
# {'1': '2', 'h': 'e'}
# {'l': 'o', '3': '4'}


# Множество - set  ---  {elem1,} , {elem1, elem2, elem3} , set()
#
# a = {3, 1, 2}
#
# b = {"Some", "words", "here"}
#
# c = "It is simple text"           # string
# d = set(c)
#
# print(a)
# print(b)
# print(d)
#
# {1, 2, 3}
# {'words', 'here', 'Some'}
# {' ', 'm', 'l', 'x', 'I', 'p', 's', 'i', 't', 'e'}
#
# Неизменное множество - frozenset  ---  frozenset()
# Единственное отличие set от frozenset заключается в том, что set - изменяемый тип данных, а frozenset - нет.
#
# my_set = frozenset([1, 2, 3, -10, 40])
# my_set_two = frozenset([3, -10, 1, 40, 2])
#
# print(type(my_set))
# print(my_set)
# print(type(my_set_two))
# print(my_set_two)
#
# <class 'frozenset'>
# frozenset({1, 2, 3, 40, -10})
# <class 'frozenset'>
# frozenset({1, 2, 3, 40, -10})
