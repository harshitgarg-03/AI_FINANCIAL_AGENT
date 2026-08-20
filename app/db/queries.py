from sqlalchemy import text
from app.db.postgres import engine

def fetch_user_transactions(user_id: str):
    query = text("""
    SELECT *
    FROM "Transaction"
    WHERE "userId" = :user_id
    ORDER BY date DESC
""")
    with engine.connect() as conn:

        result = conn.execute(
            query,
            {"user_id": user_id}
        )

        return [dict(row._mapping) for row in result]