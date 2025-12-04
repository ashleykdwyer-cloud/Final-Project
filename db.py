def read_money():
    money = []
    with open("money.txt", "r") as file:
        money = float(file.read())
        print(f"Money:{money}")
    return money

def write_money(money):
    with open("money.txt", "w") as file:
        file.write
