def read_money():
    money = []
    try:
        with open("money.txt", "r") as file:
            money =float(file.read())
            print(f"Money: {money}")
        return money
    except FileNotFoundError:
        print("Could not find file 'money.txt'")
        return None
    
def write_money(money):
    with open("money.txt", "w") as file:
        file.write(str(money))
