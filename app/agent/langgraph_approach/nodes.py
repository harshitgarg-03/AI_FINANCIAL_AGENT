from app.tools.expense_tools import (
    get_user_transactions
)

from app.services.analyzer import (
    ExpenseAnalyzer
)

from app.llm.model import llm


def fetch_data_node(state):

    transactions = (
        get_user_transactions.invoke(
            {
                "user_id": state["user_id"]
            }
        )
    )

    return {
        "transactions": transactions
    }


def analysis_node(state):

    analyzer = ExpenseAnalyzer(
        state["transactions"]
    )

    summary = analyzer.summary()

    return {
        "summary": summary
    }


def recommendation_node(state):

    summary = state["summary"]

    recommendations = []

    if (
        summary["top_category"]
        == "Food"
    ):

        recommendations.append(
            "Reduce food delivery spending."
        )

    return {
        "recommendations":
        recommendations
    }


def response_node(state):

    prompt = f"""
    User Question:
    {state['question']}

    Financial Summary:
    {state['summary']}

    Recommendations:
    {state['recommendations']}

    Generate helpful advice.
    """

    response = llm.invoke(
        prompt
    )

    return {
        "response":
        response.content
    }