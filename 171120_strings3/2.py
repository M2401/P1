#дана строка 3А4Б, требуется её распаковать.

import math
def unpack(s:str):
    res = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            p = ''
            while s[i].isdigit():
                p += s[i]
                i += 1
            p = int(p)
            res += s[i] * p
        else:
            res += s[i]
        i += 1
    return res

def main():
    with open("INPUT.txt", "r") as file:
        s = file.readline()
    s = unpack(s)
    with open("output.txt", "w") as file2:
        countrow = math.ceil(len(s)/40)
        for i in range(countrow):
            start = i*40
            finish = start + 40
            file2.write(s[start:finish]+"\n")

main()
