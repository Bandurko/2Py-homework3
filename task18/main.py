# Задача 18: Требуется найти в массиве A[1..N] самый 
# близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках 
# записаны N целых чисел Ai. Последняя строка содержит число X

# PS: Значения вводим строкой
# PS2: Если имеются два самых близких к заданному числа, то
# берем меньшее из них

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

nums = input('Введите список значений через пробел: ').split()
x = input('Задайте число: ')
min = nums[0]
i = 1
while i < (len(nums)):
    if (x - nums[i]) <= min and (x - nums[i]) > 0:
        min = nums[i]
        i += 1
print(f'Самый близкий по величине элемент к заданному числу {x} является {min}')