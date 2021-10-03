class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})

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
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance(): return False
        else: return True

    def __str__(self):
        pass

def create_spend_chart(categories):
    pass

# TEST
test1 = Category('test1')
test1.deposit(10)
print(test1.ledger)
test2 = Category('test2')
test1.transfer(11, test2)
print(test1.ledger)
print(test2.ledger)
