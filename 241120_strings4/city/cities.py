#требуется из файла взять города и записать их в другой файл
with open("city.txt", "w") as file2:
    with open("list2.csv", "r") as file:
        a = file.read().splitlines()
        for i in range(2, len(a)):
            b = a[i].split(";")
            city = b[1]
            file2.write(city + "\n")

