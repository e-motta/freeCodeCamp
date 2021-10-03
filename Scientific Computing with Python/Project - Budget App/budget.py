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

    def get_withdrawals(self):
        withdrawals = 0
        for i in self.ledger:
            if i["amount"] < 0: withdrawals += i["amount"]
        return withdrawals

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
            items += f"{i['description']:23.23}{i['amount']:7.2f}" + "\n"

        total = f"Total: {self.get_balance():0.2f}"

        return title + items + total


def create_spend_chart(categories):
    
    first_column =  "1           "
    second_column = "0987654321  "
    third_column =  "00000000000 "
    fourth_column = "||||||||||| "
    empty_column =  "           -"

    columns = [first_column, second_column, third_column, fourth_column, empty_column]

    bigger_name = ""

    total_withdrawals = 0
    for category in categories:
        # Get total withdrawals
        total_withdrawals += category.get_withdrawals()
        # Get bigger name
        if len(category.category) > len(bigger_name): bigger_name = category.category

    # Pad columns
    columns = [column + len(bigger_name) * " " for column in columns]

    # Add items to columns
    for category in categories:
        percentage = 100 * category.get_withdrawals() / total_withdrawals
        bar_height = int(percentage/10) + 1
        columns.append(f"{bar_height * 'o':>11}-{category.category:{len(bigger_name)}}")
        columns.append(columns[4])
        columns.append(columns[4])

    # Draw chart
    chart = "Percentage spent by category\n"
    for character in range(len(columns[0])):
        for column in columns:
            chart += column[character]
        chart += "\n"

    return chart[0:-1]  # The slicing removes last '\n' character to pass all tests. Not really necessary
