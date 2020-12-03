#Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа
# (считываем все числа из файла в список а потом записываем обратно в файл только нечетные)

# with open("evenfigures.txt", "w") as file3:
#     with open("figures.txt", "r") as file:
#         a = file.read().split()
#         for i in a:
#             if int(i) % 2 == 1:
#                 file3.write(i + " ")



with open("evenfigures.txt", "w") as file3:
     with open("figures.txt", "r") as file:
         a = list(map(int, file.read().split()))
         for i in a:
             if i % 2 == 1:
                 file3.write(str(i) + " ")