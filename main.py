# def main():
#     print("Hello from ai-financial-agent!")


# if __name__ == "__main__":
#     main()


# from fastapi import FastAPI

# app = FastAPI();
# @app.get("/")
# def Home():
#     return {"message": "AI Financial Advisor "}


from app.agent.financial_agent import (
    FinancialAgent
)

agent = FinancialAgent()

response = agent.chat(
    user_id="ueP0HbKzLAwueZKwHV5QpSJb20DpBq1X",
    question="Where am I spending most of my money?"
)

print(response)

# from sqlalchemy import text

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT 1"))
#     print(result.fetchone())