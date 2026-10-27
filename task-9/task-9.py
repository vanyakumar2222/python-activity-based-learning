class TravelExpense:
    def __init__(self, category, amount, currency):
        self.category = category
        self.amount = amount
        self.currency = currency


# Exchange rates to INR
exchange_rates = {
    "USD": 83.0,
    "EUR": 90.0,
    "GBP": 105.0,
    "INR": 1.0
}

# Conversion fee percentage
CONVERSION_FEE_PERCENT = 2

# Travel budget in INR
TRAVEL_BUDGET = 150000

# Sample expenses
expenses = [
    TravelExpense("Accommodation", 800, "USD"),
    TravelExpense("Flights", 1000, "USD"),
    TravelExpense("Food", 400, "EUR"),
    TravelExpense("Shopping", 500, "GBP"),
    TravelExpense("Local Transport", 10000, "INR")
]

total_expense = 0
category_totals = {}

print("=" * 70)
print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")
print("=" * 70)

print(f"{'Category':20}{'Amount':12}{'Currency':10}"
      f"{'Converted(INR)':18}")

for exp in expenses:

    rate = exchange_rates[exp.currency]

    converted_amount = exp.amount * rate

    conversion_fee = converted_amount * \
                     (CONVERSION_FEE_PERCENT / 100)

    final_amount = converted_amount + conversion_fee

    total_expense += final_amount

    category_totals[exp.category] = final_amount

    print(f"{exp.category:20}"
          f"{exp.amount:<12.2f}"
          f"{exp.currency:<10}"
          f"{final_amount:<18.2f}")

# Largest expense category
largest_category = max(
    category_totals,
    key=category_totals.get
)

largest_amount = category_totals[largest_category]

print("\n" + "=" * 70)
print(f"Total Travel Expense : ₹{total_expense:.2f}")
print(f"Travel Budget        : ₹{TRAVEL_BUDGET:.2f}")

if total_expense <= TRAVEL_BUDGET:
    savings = TRAVEL_BUDGET - total_expense
    print(f"Status               : WITHIN BUDGET")
    print(f"Budget Remaining     : ₹{savings:.2f}")
else:
    excess = total_expense - TRAVEL_BUDGET
    print(f"Status               : OVER BUDGET")
    print(f"Budget Exceeded By   : ₹{excess:.2f}")

print(f"\nLargest Expense Category : {largest_category}")
print(f"Amount Spent            : ₹{largest_amount:.2f}")

print("=" * 70)