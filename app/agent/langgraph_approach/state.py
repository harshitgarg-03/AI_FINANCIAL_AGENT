from typing import TypedDict


class FinancialState(TypedDict):

    user_id: str

    question: str

    preferences: dict
    
    transactions: list

    summary: dict

    recommendations: list

    response: str