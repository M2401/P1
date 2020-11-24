#требуется проверить, является ли сообщение шифром. Сообщение является шифром, если
#заданное сочетание цифр встречается в нем несколько раз.

def check_message(s, k):
    for i in range(len(s)-k+1):
        p = s[i:i+k]
        pos = s.find(p, i+1)
        if pos != -1:
            return True
        # for j in range(i+1, len(s)-k+1):
        #     t = s[j:j+k]
        #     if p == t:
        #         return True
    return False


def main():
    s = input('Введите сообщение: ')
    k = int(input('Длина шифра = '))
    if check_message(s, k):
        print('yes')
    else:
        print('no')

main()