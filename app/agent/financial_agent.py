from app.llm.model import llm

from app.tools.expense_tools import (
    get_user_transactions
)

from app.tools.budget_tools import (
    get_user_budget
)

from app.tools.income_tools import (
    get_user_income
)

from app.tools.goal_tools import (
    get_user_goals
)

from app.services.analyzer import (
    ExpenseAnalyzer
)

from app.tools.registry import TOOLS

from langchain.agents import create_agent


class FinancialAgent:

    def __init__(self):
        # self.analyzer = ExpenseAnalyzer()



        self.agent = create_agent(
            model=llm,
            tools=TOOLS
        )

    def chat(
        self,
        user_id: str,
        question: str
    ):

        transactions = (
            get_user_transactions.invoke(
                {
                    "user_id": user_id
                }
            )
        )

        analyzer = ExpenseAnalyzer(
        transactions
    )
        budgets = (
            get_user_budget.invoke(
                {
                    "user_id": user_id
                }
            )
        )

        incomes = (
            get_user_income.invoke(
                {
                    "user_id": user_id
                }
            )
        )

        goals = (
            get_user_goals.invoke(
                {
                    "user_id": user_id
                }
            )
        )

        summary = analyzer.summary(
            # transactions=transactions,
            # budgets=budgets,
            # incomes=incomes,
            # goals=goals
        )

        prompt = f"""
You are an expert AI Financial Advisor.

Your job is to help users understand:

- Spending habits
- Savings
- Budgets
- Financial goals
- Expense categories
- Financial health

Rules:

1. Use only the provided financial data.
2. Never invent numbers.
3. Give practical advice.
4. Keep responses concise.
5. Mention risks if overspending is detected.

User Question:
{question}

Financial Summary:
{summary}
"""

        response = llm.invoke(
            prompt
        )

        return response.content