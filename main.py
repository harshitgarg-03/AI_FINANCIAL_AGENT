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
    user_id="yibmylMlF2uFIBaZD0Wuyr2aDsEsNNMW",
    question="give all transaction sumamry",
    thread_id = "test2"
)

print(response)

# from sqlalchemy import text

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT 1"))
#     print(result.fetchone())