from langchain.tools import tool

from app.db.queries import (
    fetch_user_transactions
)

@tool
def get_user_transactions(
    user_id: str
):
    """
    Fetch all transactions
    for a user.
    """

    data = fetch_user_transactions(
        user_id
    )
    return str(data)
