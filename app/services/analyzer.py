
from collections import defaultdict
from datetime import datetime


class ExpenseAnalyzer:

    def __init__(self, transactions: list):
        self.transactions = transactions

    # ---------------------------
    # EXPENSE TRANSACTIONS ONLY
    # ---------------------------

    def get_expenses(self):
        return [
            tx
            for tx in self.transactions
            if tx["type"].lower() == "expense"
        ]

    # ---------------------------
    # INCOME TRANSACTIONS ONLY
    # ---------------------------

    def get_income_transactions(self):
        return [
            tx
            for tx in self.transactions
            if tx["type"].lower() == "income"
        ]

    # ---------------------------
    # TOTAL EXPENSES
    # ---------------------------

    def total_expenses(self):

        expenses = self.get_expenses()

        return sum(
            tx["amount"]
            for tx in expenses
        )

    # ---------------------------
    # TOTAL INCOME
    # ---------------------------

    def total_income(self):

        income = self.get_income_transactions()

        return sum(
            tx["amount"]
            for tx in income
        )

    # ---------------------------
    # CATEGORY WISE SPENDING
    # ---------------------------

    def category_spending(self):

        expenses = self.get_expenses()

        categories = defaultdict(float)

        for tx in expenses:

            category = tx["category"]

            categories[category] += tx["amount"]

        return dict(categories)

    # ---------------------------
    # TOP SPENDING CATEGORY
    # ---------------------------

    def top_category(self):

        categories = self.category_spending()

        if not categories:
            return None

        return max(
            categories,
            key=categories.get
        )

    # ---------------------------
    # AVERAGE EXPENSE
    # ---------------------------

    def average_expense(self):

        expenses = self.get_expenses()

        if len(expenses) == 0:
            return 0

        return (
            self.total_expenses()
            / len(expenses)
        )

    # ---------------------------
    # CASH FLOW
    # ---------------------------

    def cash_flow(self):

        return (
            self.total_income()
            - self.total_expenses()
        )

    # ---------------------------
    # SAVINGS RATE
    # ---------------------------

    def savings_rate(self):

        income = self.total_income()

        if income == 0:
            return 0

        savings = (
            income
            - self.total_expenses()
        )

        return round(
            (savings / income) * 100,
            2
        )

    # ---------------------------
    # OVESPENDING DETECTION
    # ---------------------------

    def detect_overspending(
        self,
        budgets: dict
    ):

        category_spend = self.category_spending()

        overspent = {}

        for category, budget in budgets.items():

            spent = category_spend.get(
                category,
                0
            )

            if spent > budget:

                overspent[category] = {
                    "spent": spent,
                    "budget": budget,
                    "excess": spent - budget
                }

        return overspent

    # ---------------------------
    # MONTHLY SPENDING
    # ---------------------------

    def monthly_spending(self):

        expenses = self.get_expenses()

        monthly = defaultdict(float)

        for tx in expenses:

            date_obj = datetime.fromisoformat(
                tx["date"]
            )

            month_key = (
                f"{date_obj.year}-{date_obj.month:02d}"
            )

            monthly[month_key] += tx["amount"]

        return dict(monthly)

    # ---------------------------
    # SPENDING PATTERN
    # ---------------------------

    def spending_pattern(self):

        monthly = self.monthly_spending()

        months = list(monthly.keys())

        if len(months) < 2:

            return {
                "trend": "insufficient_data"
            }

        values = list(monthly.values())

        if values[-1] > values[-2]:

            trend = "increasing"

        elif values[-1] < values[-2]:

            trend = "decreasing"

        else:

            trend = "stable"

        return {
            "trend": trend,
            "current_month": values[-1],
            "previous_month": values[-2]
        }

    # ---------------------------
    # COMPLETE SUMMARY
    # ---------------------------

    def summary(self):

        return {

            "total_income":
                self.total_income(),

            "total_expenses":
                self.total_expenses(),

            "cash_flow":
                self.cash_flow(),

            "savings_rate":
                self.savings_rate(),

            "average_expense":
                self.average_expense(),

            "top_category":
                self.top_category(),

            "category_spending":
                self.category_spending(),

            "monthly_spending":
                self.monthly_spending(),

            "spending_pattern":
                self.spending_pattern()
        }