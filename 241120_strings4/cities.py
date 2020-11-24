#требуется из файла взять города и записать их в другой файл

with open("list1.txt", "r") as file:
    a = file.read().splitlines()
    city = a[1:]
    city.sort()
    result = city

with open("city.txt", "w") as file2:
    file2.write(result)