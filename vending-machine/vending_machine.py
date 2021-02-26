from model.VendingMachine import VendingMachine


def main():
    vending_machine: VendingMachine = VendingMachine()
    while True:
        command: str = input("---> ")
        if command == "n":
            vending_machine.insert_nickel()
        if command == "d":
            vending_machine.insert_dime()
        if command == "q":
            vending_machine.insert_quarter()
        if command == "D":
            vending_machine.insert_dollar()
        if command in ("cr", "CR"):
            vending_machine.coin_return()
        if command == "service":
            vending_machine.service()
        if command == "get-a":
            vending_machine.vend_item('A')
        if command == "get-b":
            vending_machine.vend_item('B')
        if command == "get-c":
            vending_machine.vend_item('C')
        if command == "stock":
            vending_machine.print_stock()


if __name__ == "__main__":
    main()
