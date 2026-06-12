from sqlalchemy import text
from app.db.postgres import engine

# def fetch_user_goals(user_id: str):

#     query = text("""
#         SELECT *
#         FROM "Goal"
#         WHERE "userId" = :user_id
#         ORDER BY "createdAt" DESC
#     """)

#     with engine.connect() as conn:

#         result = conn.execute(
#             query,
#             {"user_id": user_id}
#         )

#         return [
#             dict(row._mapping)
#             for row in result
#         ]

# def fetch_user_income(user_id: str):

#     query = text("""
#         SELECT *
#         FROM "Income"
#         WHERE "userId" = :user_id
#         ORDER BY date DESC
#     """)

#     with engine.connect() as conn:

#         result = conn.execute(
#             query,
#             {"user_id": user_id}
#         )

#         return [
#             dict(row._mapping)
#             for row in result
#         ]

# def fetch_user_budget(user_id: str):

#     query = text("""
#         SELECT *
#         FROM "Budget"
#         WHERE "userId" = :user_id
#         ORDER BY "createdAt" DESC
#     """)

#     with engine.connect() as conn:

#         result = conn.execute(
#             query,
#             {"user_id": user_id}
#         )

#         return [
#             dict(row._mapping)
#             for row in result
#         ]

def fetch_user_transactions(user_id: str):
    # print("user id  in queries " , user_id)
    query = text("""
    SELECT *
    FROM "Transaction"
    WHERE "userId" = :user_id
    ORDER BY date DESC
""")
    # {"userId": user_id}
    print("hiii")
    with engine.connect() as conn:

        result = conn.execute(
            query,
            {"user_id": user_id}
        )

        return [dict(row._mapping) for row in result]