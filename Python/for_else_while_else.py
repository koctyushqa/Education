# Construction for-else, while-else - Конструкция for-else, while-else

# Циклы for и while могут иметь блок else. Блок else выполняется, когда цикл завершается в нормальном режиме.
# Т.е.не был вызван break.

# Пример условия else в цикле for:
#
# for i in range(3):
#     print(i)
# else:
#     print("Finish")
#
# 0
# 1
# 2
# Finish


# Пример условия else в цикле while:
#
# i = 0
# while i < 4:
#     print(i)
#     i += 1
# else:
#     print("Finish")
#
# 0
# 1
# 2
# 3
# Finish


# Условие else не выполняется, если цикл завершается принудительно (например, с помощью оператора break
# или путем вызова исключения):

# 1. for-break-else.
#
# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Finish")
#
# 0
# 1

# 2. while-break-else.
#
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print("Finish")
#
# 0
# 1
# 2
