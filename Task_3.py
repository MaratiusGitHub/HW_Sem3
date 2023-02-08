# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
# пример
# Ввод:
# ноутбук
# Вывод:
# 12

word = input('Введите слово на на английском или русском языке: ')
word = word.upper()
points = 0

point = \
    {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
        2: ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'],
        3: ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
        4: ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'],
        5: ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'],
        8: ['J', 'X', 'Ш', 'Э', 'Ю'],
        10: ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
    }
for i in word:
    for (k, v) in point.items():
        for j in v:
            if i == j:
                points += k

print(points)

# ver1
# word = input('Введите слово на на английском или русском языке: ')
# word = word.upper()
# print(word)
# points = 0
# onePoint = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
# twoPoint = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
# threePoint = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
# fourPoint = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
# fivePoint = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
# eightPoint = ['J', 'X', 'Ш', 'Э', 'Ю']
# tenPoint = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
#
# for i in word:
#     if i in onePoint:
#         points += 1
#     elif i in twoPoint:
#         points += 2
#     elif i in threePoint:
#         points += 3
#     elif i in fourPoint:
#         points += 4
#     elif i in fivePoint:
#         points += 5
#     elif i in eightPoint:
#         points += 8
#     elif i in tenPoint:
#         points += 10
#
# print(points)

# ver2:
# word = input('Введите слово на на английском или русском языке: ')
# word = word.upper()
# points = 0
#
# point = {}
#
# one = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
# two = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
# three = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
# four = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
# five = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
# eight = ['J', 'X', 'Ш', 'Э', 'Ю']
# ten = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
# for i in one:
#     point[i] = 1
# for i in two:
#     point[i] = 2
# for i in three:
#     point[i] = 3
# for i in four:
#     point[i] = 4
# for i in five:
#     point[i] = 5
# for i in eight:
#     point[i] = 8
# for i in ten:
#     point[i] = 10
# print(point)
#
# for i in word:
#     for (k, v) in point.items():
#         if i == k:
#             points += v
#
# print(points)

