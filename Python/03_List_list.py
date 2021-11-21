# List - list - Список

# Списки в Python - упорядоченные изменяемые коллекции объектов произвольных типов
# (почти как массив, но типы могут отличаться).

# Списки можно создать несколькими способами:
#
# 1. С помощью квадратных скобок - [] :
# Пустой список:
# a = []
#
# print(type(a))
#
# <class 'list'>
#
# Список с различными элементами:
#
# a = [1, "Hello", 7, -5, 823, "World"]
#
# print(type(a))
# print(a)
#
# <class 'list'>
# [1, 'Hello', 7, -5, 823, 'World']
#
# 2. С помощью - list() :
#
# a = "How are you?"
# a_list = list(a)
#
# print(elements_clear)
# print(elements)
# print(a)
# print(a_list)

# Команды для списков:

# Добавление в список:
#
# elements = [1, "Hello", -259]
#
# elements.append(8)
# elements.append("AaA")
#
# print(elements)
#
# [1, 'Hello', -259, 8, 'AaA']

# Добавление в список на указанную позицию:
# Немаловажно обратить внимание на метод list.insert(i, x),где list – название списка, i – позиция, x – нужное значение.
#
# elements = [9, "Hello", -259, 8]
# elements.insert(1, 2)
# print(elements)
#
# [9, 2, 'Hello', -259, 8]

# Изменение элементов списка:
#
# Изменение элементов списка происходит следующим образом: нужно выбрать элемент по индексу
# (порядковому номеру элемента) и присвоить новое значение.
#
# elements = [9, "Hello", -259, 8]
# elements[2] = "World"
#
# print(elements)
#
# [9, 'Hello', 'World', 8]

# Удаление элемента из списка:
#
# Для удаление из списка используют инструкцию del list[i] , где list – список, i – индекс (позиция) элемента в списке.
# Еще один способ удаления из списка – list.remove(x) , где list – список, x – значение, которое нужно удалить.
#
# elements = [14, 1732, 9, "Hello", -259, "World"]
# del elements[2]                  # Удаляет по индексу
# elements.remove("Hello")         # Удаляет по названию
#
# print(elements)
#
# [14, 1732, -259, 'World']     # Удалило 9 - потому что индекс 2, и удалило "Hello"

# Удалять можно как из текущего списка, так и из вложенных списков:
#
# my_list = ["I'm", "OK"]
# elements = [14, 9, my_list, -259, "Hello"]    # [14, 9, ["I'm", 'OK'], -259, 'Hello'] - список внутри списка
# del elements[2][1]
#
# print(elements)
#
# [14, 9, ["I'm"], -259, 'Hello']

# Можно удалять целыми диапазонами:
#
# elements = [14, 1732, 9, "Hello", -259, "World", 546]
# del elements[5:]     # Удаляем все элементы после 5-го (четвёртый удаляется тоже)
# print(elements)      # [14, 1732, 9, 'Hello', -259]
# del elements[:1]     # Удаляем все элементы до 2-го
# print(elements)      # [1732, 9, 'Hello', -259]
# del elements[0:2]    # Удаляем все элементы начиная с 1-го до 3-го ()
# print(elements)      # ['Hello', -259]
#
# [14, 1732, 9, 'Hello', -259]
# [1732, 9, 'Hello', -259]
# ['Hello', -259]

# Как проверить наличие элемента в списке:
#
# Для того, чтобы проверить существование какого-либо элемента в списке, нужно воспользоваться оператором in.
#
# elements = [14, 1732, 9, "Hello", -259, "World"]
# if 9 and "World" in elements:
#     print("Yes")
#
# Yes

# Объединение списков:
#
# Списки в Python можно объединят с помощью оператора + или метода extend.
#
# a = [3, 1, 5]
# b = [2, 1, 8, 10]
# print(a + b)
#
# d = ["Hello", "W", "o", "r", "l", "d"]
# e = ["How", "a", "r", "e", "you"]
# d.extend(e)                           # extend не возвращает новый список, а дополняет текущий.
# print(d)
#
# [3, 1, 5, 2, 1, 8, 10]
# ['Hello', 'W', 'o', 'r', 'l', 'd', 'How', 'a', 'r', 'e', 'you']

# Копирование списка:
#
# Если скопировать список оператором = , мы скопируем не сам список, а только его ссылку.
#
# a = [1, 2, 3, 4]
# b = a              # переменной b присваивается не значение списка a, а его адрес
# a.append(5)
# b.append(6)
# print(a)
# print(b)
#
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]
#
# Для копирования списков можно использовать несколько вариантов:
# 1) elements.copy() – встроенный метод copy
# 2) list(elements) – через встроенную функцию list()

# Цикл по списку:
#
# Для перебора списков в Python есть два цикла: for и while.
#
# elements = [9, "Hello", -259, 8]
# for i in elements:
#     print(i)
#
# 9
# Hello
# -259
# 8

# list.count(x) – посчитает количество элементов x в списке
# list.index(x) – вернет позицию первого найденного элемента x в списке
# list.reverse() – меняет порядок элементов в списке на противоположный
# list.sort() – сортирует список
# list.clear() – предназначен для удаления всех элементов (после этой операции список становится пустым []);
