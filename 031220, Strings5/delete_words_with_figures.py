#В данном текстовом файле удалить все слова, которые содержат хотя бы одну цифру
# (считываем весь текст из файла, разбиваем по словам, пробегаемся по списку слов,
# если в слове есть хотя бы одна цифра то его не записываем обратно в файл)

def check(f):
    for i in f:
        if i.isdigit():
            return False
    return True

with open("file_with_words.txt", "r") as file_without_figures:
    a = file_without_figures.read().split()
with open("file_with_words.txt", "w") as file_without_figures:
    for i in a:
        if check(i):
            file_without_figures.write(i+" ")

