TICKET_WIDTH = 30


class Category:
    def __init__(self, category: str):
        self.category = category
        self.ledger = []
        self.balance = 0.0

    def deposit(self, amount: float, description: str = ""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        if not self.check_funds(amount):
            return False

        self.deposit(-amount, description)
        return True

    def get_balance(self) -> float:
        return self.balance

    def transfer(self, amount: float, dest) -> bool:
        if not self.check_funds(amount) and not dest.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {dest.category}")
        dest.deposit(amount, f"Transfer from {self.category}")
        return True

    def check_funds(self, amount: float) -> bool:
        return amount <= self.balance

    def __repr__(self):
        cat_length = len(self.category)
        blanks_left = (TICKET_WIDTH - cat_length) // 2
        blanks_right = TICKET_WIDTH - blanks_left - cat_length

        ticket = f"""{'*' * blanks_left}{self.category}{'*' * blanks_right}"""

        for line in self.ledger:
            amount, description = f"{line['amount']:.2f}", line["description"][:23]
            blanks = TICKET_WIDTH - len(amount) - len(description)
            ticket += f"""\n{description}{' ' * blanks}{amount}"""

        ticket += f"""\nTotal: {self.balance:.2f}"""

        return ticket


def get_expenses(category: Category) -> float:
    """HELPER. Given a Category onject, sum up and return all the expenses"""
    ledger = category.ledger
    if ledger[1:]:
        return sum([expense["amount"] for expense in ledger[1:]])
    return 0


def get_breakdown(categories: list) -> dict:
    """HELPER. Given a list of Category instances, return a breakdown in a dictionary"""
    total_expenses = sum([get_expenses(category) for category in categories])
    breakdown: dict = {}
    for category in categories:
        expenses = get_expenses(category)
        breakdown[category.category] = {
            "expenses": round(expenses, 2) * (-1),
            "pct": round(expenses / total_expenses, 2),
        }
    return breakdown


def get_percent_width(percents: list) -> int:
    """HELPER. Given a list of strings, returns the maximum line length"""
    return max([len(line) for line in percents])


def get_chart_percents(summary: dict) -> list:
    """HELPER. Return the string representation of the percents"""
    percents_info = []
    for n in range(100, -10, -10):
        line = f"{n:>3}|"
        for category in summary:
            line += " o " if summary[category]["pct"] * 100 >= n else "   "
        percents_info.append(f"{line} ")
    return percents_info


def get_chart_categories(categories: list) -> list:
    """HELPER. Return the representation of the expense categories"""
    categories_info = []
    max_height = max([len(category.category) for category in categories])
    for i in range(max_height):
        line = f"{' ' * 4}"
        for category in categories:
            category_name = category.category
            try:
                line += f" {category_name[i]} "
            except IndexError:
                line += f"   "
        categories_info.append(f"{line} ")
    return categories_info


def create_spend_chart(categories):
    breakdown = get_breakdown(categories)

    chart = "Percentage spent by category\n"
    percents = get_chart_percents(breakdown)
    max_width = get_percent_width(percents)
    chart += "\n".join(percents)
    chart += f"\n{' ' * 4}{'-' * (max_width - 4)}\n"
    cats = get_chart_categories(categories)
    chart += "\n".join(cats)

    return chart

