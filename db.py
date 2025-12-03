def read_money():
    money = []
    with open("money.txt") as file:
        for line in file:
           print("Money: ", line)

def write_money():
    with open("money.txt", "w") as file:
        file.write
