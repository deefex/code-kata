from model.Money import Money


class MoneyStack:
    def __init__(self):
        self.nickels = 0
        self.dimes = 0
        self.quarters = 0
        self.dollars = 0

    def add_to_stack(self, nickels: int, dimes: int, quarters: int, dollars: int) -> None:
        self.nickels = nickels
        self.dimes = dimes
        self.quarters = quarters
        self.dollars = dollars

    def get_total_value(self) -> int:
        total_nickels: int = self.nickels * Money.NICKEL
        total_dimes: int = self.dimes * Money.DIME
        total_quarters: int = self.quarters * Money.QUARTER
        total_dollars: int = self.dollars * Money.DOLLAR
        return total_nickels + total_dimes + total_quarters + total_dollars
