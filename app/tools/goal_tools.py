from langchain_core.tools import tool

from app.db.queries import (
    fetch_user_transactions
)


@tool
def get_user_goals(user_id: str):
    """
    Fetch financial goals.
    """

    data = fetch_user_transactions(user_id)
    print("user goals :: ",data)
    return str(data)