class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.category}")
            other_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance(): return False
        return True

    def __str__(self):
        title = self.category.center(30, "*") + "\n"

        items = ''
        for i in self.ledger:
            items += f'{i["description"]:23.23}{i["amount"]:7.2f}' + "\n"

        total = f"Total: {self.get_balance():0.2f}"

        return title + items + total


def create_spend_chart(categories):
    pass
