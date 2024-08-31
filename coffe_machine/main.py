class CoffeMachine:
    def __init__(self):
        self.water = 1000
        self.milk = 500
        self.coffee = 500
        self.balance = 100

    def check_stock(self):
        if self.water < 0:
            print("Sorry there is not enough water")
            return False
        if self.coffee < 0:
            print("Sorry there is not enough coffe")
            return False
        if self.milk < 0:
            print("Sorry there is not enough milk")
            return False
        else:
            print("Enjoy the drink")
            return True

    def buy(self, drink: str):
        if drink == "espresso":
            self.water -= 100
            self.coffee -= 50
            self.balance += 1

            return self.check_stock()

        elif drink == "latte":
            self.water -= 200
            self.milk -= 100
            self.coffee -= 100
            self.balance += 2

            return self.check_stock()
        elif drink == "cappuccino":
            self.water -= 200
            self.milk -= 100
            self.coffee -= 100
            self.balance += 3

            return self.check_stock()
        else:
            print("Invalid drink")


def main():
    machine = CoffeMachine()

    def start():
        next_action = input(
            "What would you like to do? (expresso, latte, cappuccino, report, exit): "
        )

        if next_action == "report":
            print(
                f"Water: {machine.water}ml\nMilk: {machine.milk}ml\nCoffee: {machine.coffee}g\nMoney: ${machine.balance}"
            )
            start()

        elif next_action == "exit":
            print(f"Goodbye!, today you made: ${machine.balance}")

        else:
            machine.buy(next_action)
            start()

    start()


main()
