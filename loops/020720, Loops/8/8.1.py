#1. Дана последовательность из n вещественных чисел. Первое число в последовательности нечетное.
# Найти сумму всех идущих подряд в начале последовательности нечетных чисел.
# Условный оператор не использовать. Решить задачу используя циклическую конструкцию for.

n = int(input('Введите количество чисел '))

s = 0
flag = False
for i in range(1, n+1):
    a = int(input('Введите число '))
    if a % 2 == 1 and flag == False:
        s = s+a
    else:
        flag = True
print(s)