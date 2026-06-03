from sqlalchemy import text
from app.db.postgres import engine


def fetch_user_transactions(user_id: str):
    print("user id  in queries " , user_id)
    query = text("""
        SELECT *
        FROM transactions
        WHERE user_id = :user_id
        ORDER BY date DESC
    """)

    with engine.connect() as conn:

        result = conn.execute(
            query,
            {"user_id": user_id}
        )

        return [dict(row._mapping) for row in result]