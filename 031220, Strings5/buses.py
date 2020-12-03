#Первая строка входного файла INPUT.TXT содержит единственное натуральное число N –
# количество записанных Васей номеров (N ≤ 50). Далее следует N строк с записями
# номеров автобусов. Длины строк от 1 до 300 и содержат только символы с кодами ASCII
# от 33 до 127 (не содержат пробелов, специальных и русских символов).
#В выходной файл выведите N строк, в i-й строке должно содержаться «Yes»,
# если соответствующая i-я запись номера верна и «No» в противном случае.
# Номер считается правильным, если сначала идет буква, затем 3 цифры и еще 2 буквы заканчивают запись.
# В качестве цифр могут использоваться любые цифры от 0 до 9, а в качестве букв только прописные буквы,
# обозначения которых присутствуют как в английском, так и в русском алфавите, т.е. только
# следующие символы: A, B, C, E, H, K, M, O, P, T, X, Y.


def check(number:str):
    if len(number) != 6:
        return False
    vowels = 'ABCEHKMOPTXY'
    if number[0] in vowels and number[1].isdigit() and number[2].isdigit() and number[3].isdigit() and number[4] in vowels and number[5] in vowels:
        return True
    else:
        return False

def main():
    with open("busnumbers.txt", "r") as file:
        n = int(file.readline())
        with open("output.txt", "w") as file2:
            for i in range(n):
                number = file.readline().strip("\n")
                if check(number):
                    file2.write("Yes \n")
                else:
                    file2.write("No \n")




# def check2(k):
#     vowels = 'ABCEHKMOPTXY'
#     figures = '0123456789'
#
#     if k[0] in vowels and k[1] in figures and k[2] in figures and k[3] in figures and k[4] in vowels and k[5] in vowels:
#         return True
#     else:
#         return False
#
#
# def main():
#     n = int(input('Введите количество номеров '))
#     for i in range(n):
#         k = input('Введите номер ')
#
#         if len(k) < 5 or len(k) > 6:
#             print('Номер неверный')
#         else:
#             c = check2(k)
#             if c:
#                 print('Номер верный')
#             else:
#                 print('Номер неверный')

main()



