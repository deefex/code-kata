from model.MoneyStack import MoneyStack
from model.Money import Money
from model.Item import Item
from termcolor import colored


class VendingMachine:
    def __init__(self):
        self.machine_stack: MoneyStack = MoneyStack()
        self.vending_stack: MoneyStack = MoneyStack()
        self.item_slots: dict = {'A': [Item], 'B': [Item], 'C': [Item]}
        self.service()
        self.print_stock()

    def insert_nickel(self) -> None:
        self.vending_stack.nickels += 1
        self.display_money_inserted()

    def insert_dime(self) -> None:
        self.vending_stack.dimes += 1
        self.display_money_inserted()

    def insert_quarter(self) -> None:
        self.vending_stack.quarters += 1
        self.display_money_inserted()

    def insert_dollar(self) -> None:
        self.vending_stack.dollars += 1
        self.display_money_inserted()

    def coin_return(self) -> MoneyStack:
        return_stack: MoneyStack = MoneyStack()
        return_stack.add_to_stack(self.vending_stack.dollars, self.vending_stack.quarters,
                                  self.vending_stack.dimes, self.vending_stack.nickels)
        self.vending_stack.dollars = 0
        self.vending_stack.quarters = 0
        self.vending_stack.dimes = 0
        self.vending_stack.nickels = 0
        return return_stack

    def service(self) -> None:
        item_a: Item = Item("Hula Hoop", 65)
        item_b: Item = Item("Mars Bars", 100)
        item_c: Item = Item("Coke Zero", 150)
        self.item_slots['A'] = [item_a] * 2
        self.item_slots['B'] = [item_b] * 2
        self.item_slots['C'] = [item_c] * 2
        self.machine_stack.add_to_stack(50, 50, 50, 50)

    def vend_item(self, slot: str) -> (Item, MoneyStack):
        if len(self.item_slots[slot]) >= 1:
            if self.vending_stack.get_total_value() >= self.item_slots[slot][0].price:
                # Calculate change
                change: int = self.vending_stack.get_total_value() - self.item_slots[slot][0].price

                # Transfer the money from the vending stack to the machine stack
                self.machine_stack.dollars += self.vending_stack.dollars
                self.machine_stack.quarters += self.vending_stack.quarters
                self.machine_stack.dimes += self.vending_stack.dimes
                self.machine_stack.nickels += self.vending_stack.nickels

                # Zero out the vending stack
                self.vending_stack.dollars = 0
                self.vending_stack.quarters = 0
                self.vending_stack.dimes = 0
                self.vending_stack.nickels = 0

                # Return the item and the change
                item: Item = self.item_slots[slot].pop(0)
                self.display_vended_item(item)
                return item, self.return_change(change)
            else:
                self.display_warning_insufficient_money(self.item_slots[slot][0].price, self.vending_stack.get_total_value())
                # None is returned
        else:
            self.display_warning_slot_is_empty()
            # None is returned

    def return_change(self, amount_due: int) -> MoneyStack:
        nickels_due: int = 0
        dimes_due: int = 0
        quarters_due: int = 0
        dollars_due: int = 0
        change_stack: MoneyStack = MoneyStack()

        while amount_due >= Money.DOLLAR and self.machine_stack.dollars >= 1:
            dollars_due += 1
            self.machine_stack.dollars -= 1
            amount_due -= Money.DOLLAR
        while amount_due >= Money.QUARTER and self.machine_stack.quarters >= 1:
            quarters_due += 1
            self.machine_stack.quarters -= 1
            amount_due -= Money.QUARTER
        while amount_due >= Money.DIME and self.machine_stack.dimes >= 1:
            dimes_due += 1
            self.machine_stack.dimes -= 1
            amount_due -= Money.DIME
        while amount_due >= Money.NICKEL and self.machine_stack.nickels >= 1:
            nickels_due += 1
            self.machine_stack.nickels -= 1
            amount_due -= Money.NICKEL

        change_stack.add_to_stack(nickels_due, dimes_due, quarters_due, dollars_due)

        if amount_due != 0:
            print("Apologies. Full change amount not available. Contact Service Engineer")
            print("Returning $", "{:.2f}".format(amount_due / 100), end="")
        else:
            print("Returning $", "{:.2f}".format(change_stack.get_total_value() / 100), end="")

        print("(", dollars_due, "dollars", quarters_due, "quarters", dimes_due, "dimes", nickels_due, "nickels )")
        return change_stack

    def admin(self) -> None:
        pass  # TODO

    def print_stock(self) -> None:
        for key in self.item_slots:
            if len(self.item_slots[key]) == 0:
                print("  - Slot %s: EMPTY" % key)
            else:
                print("  - Slot %s: " % key,
                      "Quantity:", len(self.item_slots[key]),
                      ", Item:", self.item_slots[key][0].name,
                      ", Price:", "{:.2f}".format(self.item_slots[key][0].price / 100))

    def display_money_inserted(self) -> None:
        print("Money Inserted:", "{:.2f}".format(self.vending_stack.get_total_value() / 100))

    @staticmethod
    def display_warning_insufficient_money(money_required, money_inserted) -> None:
        print(colored('WARNING', 'yellow'))
        print("Please Insert:     ", "{:.2f}".format(money_required / 100))
        print("Currently Inserted:", "{:.2f}".format(money_inserted / 100))

    @staticmethod
    def display_warning_slot_is_empty() -> None:
        print(colored('WARNING', 'yellow'))
        print("Slot is empty. Please make another selection.")

    @staticmethod
    def display_vended_item(item: Item) -> None:
        print(colored('SUCCESS', 'green'))
        print("You have received a", item.name, "for", "{:.2f}".format(item.price / 100))

