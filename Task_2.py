# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# пример
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Введите количество элементов в массиве: '))

array = []
for i in range(n):
    array.append(int(input('Введите число: ')))
print(array)

x = min = int(input('Задайте число: '))

for i in array:
    if x - i < min:
        min == x - i
        result = i
print(result)
