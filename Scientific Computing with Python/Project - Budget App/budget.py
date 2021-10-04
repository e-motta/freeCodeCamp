class Category:
    """A class to represent budgeting categories."""

    def __init__(self, category):
        """Creates a Category object with a given name and an empty ledger.

        Args:
            category (str): The name of the category.

        Attributes:
            ledger (list): A ledger to store deposits and withdrawals.
        """
        
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        """Add a deposit to the ledger.

        Args:
            amount (float/int): The amount of the deposit in $.
            description (str, optional): The description of the deposit. Defaults to ''.
        """

        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        """Add a withdrawal to the ledger

        Args:
            amount (float/int): The amount of the withdrawal in $.
            description (str, optional): The description of the withdrawal. Defaults to ''.

        Returns:
            boolean: True if the withdrawal was performed, False otherwise.
        """

        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Get the balance of the ledger.

        Returns:
            float/int: The current balance.
        """

        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance

    def get_withdrawals(self):
        """Get to total withdrawals from the ledger.

        Returns:
            float/int: The total withdrawals.
        """

        withdrawals = 0
        for i in self.ledger:
            if i["amount"] < 0:
                withdrawals += i["amount"]
        return withdrawals

    def transfer(self, amount, other_category):
        """Transfer an amount from object's category to another category.

        Args:
            amount (float/int): The amount to be transfered in $.
            other_category (Category class object): the category to transfer the amount to.

        Returns:
            bool: True if the transfer was performed, False otherwise.
        """

        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.category}")
            other_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        """Check if there available funds in the ledger.

        Args:
            amount (float/int): The amount to check againt the ledger balance.

        Returns:
            bool: False if the amount is greater than the balance, True otherwise.
        """

        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        """Print all items and amounts in the ledger, with total.

        Returns:
            str: A list with the items and amounts in the ledger.
        """

        title = self.category.center(30, "*") + "\n"

        items = ''
        for i in self.ledger:
            items += f"{i['description']:23.23}{i['amount']:7.2f}" + "\n"

        total = f"Total: {self.get_balance():0.2f}"

        return title + items + total


def create_spend_chart(categories):
    """Create a chart with the percentage spent in each Category object passed in to the function

    Args:
        categories (list): A list with Category class objects.

    Returns:
        str: The chart.
    """

    first_column = "1           "
    second_column = "0987654321  "
    third_column = "00000000000 "
    fourth_column = "||||||||||| "
    empty_column = "           -"

    columns = [first_column, second_column,
               third_column, fourth_column, empty_column]

    bigger_name = ""

    total_withdrawals = 0
    for category in categories:
        # Get total withdrawals
        total_withdrawals += category.get_withdrawals()
        # Get bigger name
        if len(category.category) > len(bigger_name):
            bigger_name = category.category

    # Pad columns
    columns = [column + len(bigger_name) * " " for column in columns]

    # Add items to columns
    for category in categories:
        percentage = 100 * category.get_withdrawals() / total_withdrawals
        bar_height = int(percentage/10) + 1
        columns.append(
            f"{bar_height * 'o':>11}-{category.category:{len(bigger_name)}}")
        columns.append(columns[4])
        columns.append(columns[4])

    # Draw chart. Lines are printed vertically
    chart = "Percentage spent by category\n"
    for character in range(len(columns[0])):
        for column in columns:
            chart += column[character]
        chart += "\n"

    # The slicing removes last '\n' character to pass all tests. Not really necessary
    return chart[0:-1]
