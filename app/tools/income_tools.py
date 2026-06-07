from langchain_core.tools import tool

from app.db.queries import (
    fetch_user_transactions
)


@tool
def get_user_income(user_id: str):
    """
    Fetch user income details.
    """

    return fetch_user_transactions(user_id)