class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance()}"
        return title + items + total

    def get_balance(self):
        total = 0
        for transaction in self.ledger:
            if "amount" in transaction:
                total += transaction["amount"]
        return total

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        new_deposit = {"amount": amount, "description": description}
        self.ledger.append(new_deposit)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            new_withdraw = {"amount": -amount, "description": description}
            self.ledger.append(new_withdraw)
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            withdraw_desc = f"Transfer to {category.name}"
            deposit_desc = f"Transfer from {self.name}"
            self.withdraw(amount, withdraw_desc)
            category.deposit(amount, deposit_desc)
            return True
        return False


def create_spend_chart(categories):
    total_withdrawals = 0
    categories_sum_withdrawals = []

    # Calculate total withdrawals for each category and append to list
    for category in categories:
        category_sum = 0
        for transaction in category.ledger:
            if "amount" in transaction and transaction["amount"] < 0:
                category_sum += abs(transaction["amount"])
        categories_sum_withdrawals.append(category_sum)

    # Convert categories_sum_withdrawals to int with map()
    categories_sum_withdrawals = list(map(int, categories_sum_withdrawals))

    # Calculate total withdrawals of all categories
    total_withdrawals = sum(categories_sum_withdrawals)

    # Calculate percentage spent per category using list comprehensions
    category_percentages = [
        int(item / total_withdrawals * 100) for item in categories_sum_withdrawals
    ]

    # Build chart
    chart = "Percentage spent by category\n"

    for amount in range(100, -10, -10):
        chart += str(amount).rjust(3) + "| "
        for percent in category_percentages:
            if percent >= amount:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    ----------\n"

    category_names = [category.name for category in categories]
    max_name_length = max(len(name) for name in category_names)

    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart
