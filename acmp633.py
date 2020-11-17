with open("command.txt", "r") as file:
    a = file.read().splitlines()
    name = a[0]
    players = a[1:]
    players.sort()
    result = name + ": " + ", ".join(players)

with open("result.txt", "w") as file2:
    file2.write(result)




