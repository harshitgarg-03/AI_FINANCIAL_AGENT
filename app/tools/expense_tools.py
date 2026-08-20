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
    # print("user txns  :: ",data)
    return str(data)


# @tool
# def get_user_transactions(user_id: str):
#     """
#     Fetch all user transactions.
#     """
#     pass

# @tool
# def get_user_income(user_id:str):
#     pass

# @tool
# def get_user_budget(user_id:str):
#     pass

# @tool
# def get_user_goals(user_id:str):
#     pass