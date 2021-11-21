# Function - def - Функция

# Рекурсивные функции:
#
# Рекурсия — это не особенность Python. Это общепринятая и часто используемая техника в Computer Science,
# когда функция вызывает сама себя.
# Самый известный пример — вычисление факториала a! = a * a - 1 * a - 2 * ... Зная, что факториал 0 равен 1 --- 0! = 1.
#
# def factorial(a):
#         if a != 0:
#             return a * factorial(a - 1)
#         else:
#             return 1
#
# print(factorial(4))
#
# 24
# 4 * (4-1) * (4-2) * (4-3) = 4 * 3 * 2 * 1 = 24

# Присвоение функции переменной:
#
# Переменным также можно присваивать встроенные функции.
# Таким образом позже есть возможность вызывать функцию другим именем. Такой подход называется непрямым вызовом функции.
#
# def plus(a, b):
#     return a + b
#
# new_value = plus(2, 5)
#
# print(new_value)
#
# 7
#
# Менять название переменной также разрешается:
#
# В этом примере a1, a2 и function имеют один и тот же id. Они ссылаются на один объект.
#
# def function(x):
#     return x
#
# a1 = function
# a2 = a1
#
# print(function(10))
# print(a1(10))
# print(a2(10))
#
# 10
# 10
# 10

# Анонимная функция: лямбда:
#
# Лямбда-функция — это короткая однострочная функция, которой даже не нужно имя давать.
# Такие выражения содержат лишь одну инструкцию, поэтому - if, for и while использовать нельзя.
# В отличие от функций, здесь не используется ключевое слово return. Результат работы и так возвращается.
# Лямбда-функцию также можно присваивать переменным:
#
# product = lambda x, y: x * y
#
# print(product(2, 3))
# print(type(product))
#
# 6
# <class 'function'>

# Функция внутри функции:
#
# Функции можно создавать, вызывать и возвращать из других функций.
#
# В этой функции реализованы два важных свойства:
# - внутри функции mul() мы создаём ещё одну функцию helper();
# - функция mul() возвращает функцию helper() в качестве результата работы.
#
# def mul(a):
#     def helper(b):
#         return a * b
#
#     return helper
#
# print(mul(2)(3))      # a - 2, b - 3
#
# 6
#
# Особенность заключается в том, что можно создавать на базе функции mul() собственные кастомизированные функции:
#
# def mul(a):
#     def helper(b):
#         return a - b
#
#     return helper
#
# five_mul = mul(5)
#
# print(five_mul(8))      # a - 5, b - 8
#
# -3    #(минус три)
#
# Написана функция, которая отнимает любое число от 5(пяти).

# Декоратор функции:
#
# Конструктивно речь идёт о некоторой функции, в качестве аргумента которого выступает другая функция.
# Декоратор в Python добавляет дополнительный функционал к функции, не меняя её содержимое.
#
# Имеем пару простых функций first_test() и second_test() :
# При этом желаем их дополнить таким образом, чтобы перед вызовом основного кода нашей функции
# печаталась строчка “Start function”, а в конце – строка “Stop function”.
# Реализовать поставленную задачу можно несколькими методами.
# Во-первых, мы можем добавить необходимые строки в конец и начало каждой функции. Но вряд ли это удобно,
# ведь если мы пожелаем их убрать, придётся модифицировать тело функции.
#
# def first_test():
#     print("Test function 1")
#
#
# def second_test():
#     print("Test function 2")
#
#
# def simple_decorate(a):
#     print("Start function")
#     a()
#     print("Stop function")
#
#
# first_test_decorated = simple_decorate(first_test)
# second_test_decorated = simple_decorate(second_test)
#
# Start function
# Test function 1
# Stop function
# Start function
# Test function 2
# Stop function

# Второй вариант оформления декоратора:
#
# @simple_decorate – это не что иное, как декоратор функции.
#
# def simple_decorate(a):
#     print("Start function")
#     a()
#     print("Stop function")
#
#
# @simple_decorate
# def first_test():
#     print("Test function 1")
#
#
# @simple_decorate
# def second_test():
#     print("Test function 2")
#
# Start function
# Test function 1
# Stop function
# Start function
# Test function 2
# Stop function
