c = input('Введите город \n')
c = c.lower()
e = ''
d = []
for j in c:
    if j not in d:
        counter = c.count(j)
        e += j+":"+"*"*counter
        d.append(j)
print(e)