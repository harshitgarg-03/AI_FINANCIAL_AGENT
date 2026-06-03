from typing import Dict, List


CATEGORY_LIMITS = {
    "Food": 0.20,           # 20% of income
    "Travel": 0.10,         # 10%
    "Bills": 0.25,          # 25%
    "Entertainment": 0.10,  # 10%
    "Shopping": 0.15,       # 15%
    "Health": 0.10          # 10%
}


def generate_recommendations(
    monthly_income: float,
    category_totals: Dict[str, float]
) -> List[str]:

    recommendations = []

    if monthly_income <= 0:
        return ["Unable to generate recommendations because income is not available."]

    # Food
    food = category_totals.get("Food", 0)
    if food / monthly_income > CATEGORY_LIMITS["Food"]:
        recommendations.append(
            "Reduce food spending by limiting restaurant visits and food delivery orders."
        )

    # Travel
    travel = category_totals.get("Travel", 0)
    if travel / monthly_income > CATEGORY_LIMITS["Travel"]:
        recommendations.append(
            "Travel expenses are high. Consider public transport or better trip planning."
        )

    # Bills
    bills = category_totals.get("Bills", 0)
    if bills / monthly_income > CATEGORY_LIMITS["Bills"]:
        recommendations.append(
            "Review monthly bills and subscriptions to identify possible savings."
        )

    # Entertainment
    entertainment = category_totals.get("Entertainment", 0)
    if entertainment / monthly_income > CATEGORY_LIMITS["Entertainment"]:
        recommendations.append(
            "Set a fixed entertainment budget to avoid unnecessary spending."
        )

    # Shopping
    shopping = category_totals.get("Shopping", 0)
    if shopping / monthly_income > CATEGORY_LIMITS["Shopping"]:
        recommendations.append(
            "Limit shopping expenses and prioritize essential purchases."
        )

    # Health
    health = category_totals.get("Health", 0)
    if health / monthly_income > CATEGORY_LIMITS["Health"]:
        recommendations.append(
            "Health expenses are significant. Review recurring medical costs and insurance coverage."
        )

    # Savings Analysis
    total_expenses = sum(category_totals.values())
    savings = monthly_income - total_expenses
    savings_rate = savings / monthly_income

    if savings_rate < 0.10:
        recommendations.append(
            "Your savings rate is below 10%. Focus on reducing discretionary expenses."
        )

    elif savings_rate >= 0.20:
        recommendations.append(
            "You are saving more than 20% of your income. Consider investing part of your savings."
        )

    if not recommendations:
        recommendations.append(
            "Your spending pattern looks balanced. Continue tracking expenses and maintaining healthy savings habits."
        )

    return recommendations


# -------------------------
# Example Usage
# -------------------------

if __name__ == "__main__":

    monthly_income = 50000

    category_totals = {
        "Food": 13000,
        "Travel": 7000,
        "Bills": 8000,
        "Entertainment": 4000,
        "Shopping": 9000,
        "Health": 2000,
    }

    recommendations = generate_recommendations(
        monthly_income,
        category_totals
    )

    print("\nRecommendations:\n")

    for idx, recommendation in enumerate(recommendations, start=1):
        print(f"{idx}. {recommendation}")