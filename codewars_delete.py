def check_vowel(c):
    c = c.lower()
    vowels = 'aoeiu'
    if c in vowels:
        return True
    else:
        return False

def disemvowel(string):
    res = ""

    for c in string:
        if check_vowel(c) == False:
            res += c

    return res

def main():
    s = input("Введите строку \n")
    res = disemvowel(s)
    print(res)

main()

