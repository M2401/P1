#Дано число n. Требуется найти сумму ряда n+n//2+n//4 с учетом того, что члены ряда только больше 0.
n = int(input('Введите n '))
s = 0
i = n
while i >= 1:
    #print(i)

    s = s + i
    i = i // 2
print('Сумма ', s)