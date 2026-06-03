# -----------------------------------------------------------------------------

# from app.tools.expense_tools import (
#     get_user_transactions
# )

# result = get_user_transactions.invoke(
#     {
#         "user_id":"K96x7m4yUck5Z0hDCLxdQ5oYjtpm2cez"
#     }
# )

# print(result)


# ---------------------------------------------------------------------------------



# from app.services.analyzer import ExpenseAnalyzer

# transactions = [
#     {
#         "amount": 50000,
#         "category": "Salary",
#         "type": "income",
#         "date": "2026-06-01"
#     },
#     {
#         "amount": 4000,
#         "category": "Food",
#         "type": "expense",
#         "date": "2026-06-05"
#     },
#     {
#         "amount": 3000,
#         "category": "Travel",
#         "type": "expense",
#         "date": "2026-06-10"
#     },
#     {
#         "amount": 2500,
#         "category": "Food",
#         "type": "expense",
#         "date": "2026-06-15"
#     }
# ]

# budgets = {
#     "Food": 5000,
#     "Travel": 5000
# }

# analyzer = ExpenseAnalyzer(transactions)

# print(analyzer.summary())

# print(
#     analyzer.detect_overspending(
#         budgets
#     )
# )



# -----------------------------------------------------------------------------------


from app.agent.financial_agent import (
    FinancialAgent
)

agent = FinancialAgent()

response = agent.chat(
    user_id="K96x7m4yUck5Z0hDCLxdQ5oYjtpm2cez",
    question="How can I save more money?"
)

print(response)

# ----------------------------------------------------------------------------------