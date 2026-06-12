from langchain_core.tools import tool

from app.db.queries import (
    fetch_user_transactions
)

@tool
def get_user_budget(user_id: str):
    """
    Fetch user budget information.
    """

    data =fetch_user_transactions(user_id)
    print("user budget :: ",data)
    return str(data)
