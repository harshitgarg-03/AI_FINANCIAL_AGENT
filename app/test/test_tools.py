from app.tools.expense_tools import (
    get_user_transactions
)

result = get_user_transactions.invoke(
    {
        "user_id":"K96x7m4yUck5Z0hDCLxdQ5oYjtpm2cez"
    }
)

print(result)
