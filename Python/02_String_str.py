# String - str - Строки

# Строки - упорядоченные НЕИЗМЕНЯЕМЫЕ последовательности символов, используемые для хранения и представления текстовой
# информации, поэтому с помощью строк можно работать со всем, что может быть представлено в текстовой форме.

# Строки можно создать несколькими способами:
#
# 1. С помощью одинарных или двойных кавычек:
#
# first_string = "Я текст в кавычках."
# second_string = 'Слово "Python" обычно подразумевает змею.'
#
# print(type(first_string))
# print(type(second_string))
# print(first_string)
# print(second_string)
#
# <class 'str'>
# <class 'str'>
# Я текст в кавычках.
# Слово "Python" обычно подразумевает змею.
#
# Строки в одинарных и двойных кавычках - одно и то же.
# Это сделано для того, чтобы когда в строке есть слово в ковычках оно выделялось по другому, чем сама строка.
# second_string = 'Слово "Python" обычно подразумевает змею'
#
# 2. С помощью тройных кавычек:
#
# Главное достоинство строк в тройных кавычках в том, что их можно использовать для записи многострочных блоков текста.
#
# a = """Главное достоинство строк в тройных кавычках в том, что их можно использовать для записи многострочных блоков
# текста. Главное достоинство строк в тройных кавычках в том, что их можно использовать для записи многострочных блоков
# текста. Главное достоинство строк в тройных кавычках в том, что их можно использовать для записи многострочных блоков
# текста. Главное достоинство строк в тройных кавычках в том, что их можно использовать для записи многострочных блоков
# текста. Главное достоинство строк в тройных кавычках в том, что их можно использовать для записи многострочных блоков
# текста."""
#
# print(type(a))
#
# <class 'str'>
#
# 3. С помощью метода str() :
#
# my_num = 12345
# my_str = str(my_num)
#
# print(type(my_num))
# print(type(my_str))
# print(my_str)
#
# <class 'int'>
# <class 'str'>
# 12345

# Базовые операции:

# 1. Оператор сложения строк:
#
# a = 'Вот так работает'
# b = ' конкатенация строк'
#
# print(a + b)
#
# Вот так работает конкатенация строк

# 2. Оператор умножения строк:
#
# Оператор создает несколько копий строки. Если str это строка, а n целое число, то будет создано n копий строки str.
#
# a = 'Строка'
#
# print(5 * a)
#
# СтрокаСтрокаСтрокаСтрокаСтрока

# 3. Длина строки (функция len):
#
# a = 'Строка'
#
# print(len(a))
#
# 6

# Команды:

# S.isdigit()       -  Проверяет cостоит ли строка из цифр.
# S.isalpha()       -  Проверяет cостоит ли строка из букв.

# S.join(iterable) :
#
# Есть два варианта использования join:
#
# 1. У нас есть два объекта(или строки) и можно вставить что-то между ними:
#
# 1)
# a = "...".join(["1", "10"])
# print(a)
#
# 1...10
#
# 2)
# a = "В начале идут рисунки,"
# b = "какой-то текст."
# print(" а дальше ".join([a, b]))
#
# В начале идут рисунки, а дальше какой-то текст.
#
# 2. У нас есть один объект(или строка) и можно вставить что-то в его начало и конец:
#
# a = "были цифры, а потом их"
# print(a.join(["Сначала ", " рисунки."]))
#
# Сначала были цифры, а потом их рисунки.

# S.capitalize()  -  Делает первую букву первого слова большой, а все остальные маленькими

# S.split(x)      -  Разбивает строку S на части, используя специальный разделитель x, и возвращает эти
# части в виде списка
#
# a = "1_2_3".split("_")
# print(a)
#
# ['1', '2', '3']
