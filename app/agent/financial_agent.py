from app.tools.expense_tools import (
    get_user_transactions
)

from app.services.analyzer import (
    ExpenseAnalyzer
)

from app.llm.model import llm


class FinancialAgent:

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

        summary = analyzer.summary()

        prompt = f"""
        You are a financial advisor.

        User Question:
        {question}

        Financial Summary:
        {summary}

        Give useful financial advice.
        """

        response = llm.invoke(
            prompt
        )

        return response.content