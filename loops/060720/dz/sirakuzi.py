#Гипотеза Сиракуз - любое натуральное число сводится к единице в результате повторения следующих действий над
# самим числом и результатами этих действий.
#Если число четное -следует разделить его на 2.
# Если нечетное, то умножить его на 3, прибавить 1 и разделить на 2.

a = int(input('Введите число '))
while a != 1:
    if a % 2 == 0:
        a = a//2

    else:
        a = (3*a+1)//2
    print(a)


