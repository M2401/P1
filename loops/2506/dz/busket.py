a1 = int(input('Сколько очков набрала первая команда в 1 четверти? '))
b1 = int(input('Сколько очков набрала первая команда во 2 четверти? '))
c1 = int(input('Сколько очков набрала первая команда в 3 четверти? '))
d1 = int(input('Сколько очков набрала первая команда в 4 четверти? '))
a2 = int(input('Сколько очков набрала вторая команда в 1 четверти? '))
b2 = int(input('Сколько очков набрала вторая команда в 2 четверти? '))
c2 = int(input('Сколько очков набрала вторая команда в 3 четверти? '))
d2 = int(input('Сколько очков набрала вторая команда в 4 четверти? '))
print()
print(a1, a2, sep=' ')
print(b1, b2, sep=' ')
print(c1, c2, sep=' ')
print(d1, d2, sep=' ')

S1 = a1+b1+c1+d1
S2 = a2+b2+c2+d2
print(f'Сумма очков первой команды {S1}')
print(f'Сумма очков второй команды {S2}')
if S1>S2:
    print('По сумме очков первая команда выиграла')
elif S2>S1:
    print('По сумме очков вторая команда выиграла')
else:
    print('Draw')
