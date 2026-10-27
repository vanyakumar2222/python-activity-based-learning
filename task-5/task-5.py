class MobilePlan:
    def __init__(self, name, monthly_cost, validity,
                 data_limit, call_limit, sms_limit,
                 extra_data_rate, extra_call_rate, extra_sms_rate):
        self.name = name
        self.monthly_cost = monthly_cost
        self.validity = validity
        self.data_limit = data_limit
        self.call_limit = call_limit
        self.sms_limit = sms_limit
        self.extra_data_rate = extra_data_rate
        self.extra_call_rate = extra_call_rate
        self.extra_sms_rate = extra_sms_rate

    def calculate_total_cost(self, used_data, used_calls, used_sms):
        extra_data = max(0, used_data - self.data_limit)
        extra_calls = max(0, used_calls - self.call_limit)
        extra_sms = max(0, used_sms - self.sms_limit)

        excess_charge = (
            extra_data * self.extra_data_rate +
            extra_calls * self.extra_call_rate +
            extra_sms * self.extra_sms_rate
        )

        total_cost = self.monthly_cost + excess_charge

        return {
            "plan": self.name,
            "base_cost": self.monthly_cost,
            "excess_charge": excess_charge,
            "total_cost": total_cost
        }


# Available plans
plans = [
    MobilePlan(
        "Basic Plan", 299, 28,
        data_limit=20, call_limit=500, sms_limit=100,
        extra_data_rate=10, extra_call_rate=0.5, extra_sms_rate=1
    ),
    MobilePlan(
        "Standard Plan", 499, 56,
        data_limit=50, call_limit=1000, sms_limit=300,
        extra_data_rate=8, extra_call_rate=0.3, extra_sms_rate=0.8
    ),
    MobilePlan(
        "Premium Plan", 799, 84,
        data_limit=100, call_limit=2000, sms_limit=500,
        extra_data_rate=5, extra_call_rate=0.2, extra_sms_rate=0.5
    )
]

# User requirements
used_data = 60      # GB
used_calls = 1200   # Minutes
used_sms = 250      # SMS
required_validity = 30
budget = 1000

eligible_plans = []

for plan in plans:
    if plan.validity >= required_validity:
        result = plan.calculate_total_cost(
            used_data,
            used_calls,
            used_sms
        )

        if result["total_cost"] <= budget:
            eligible_plans.append(result)

# Display results
print("Eligible Plans:")
for p in eligible_plans:
    print(f"\nPlan: {p['plan']}")
    print(f"Base Cost: ₹{p['base_cost']}")
    print(f"Excess Charges: ₹{p['excess_charge']}")
    print(f"Total Cost: ₹{p['total_cost']}")

# Find most economical plan
if eligible_plans:
    best_plan = min(eligible_plans, key=lambda x: x["total_cost"])
    print("\nMost Economical Plan:")
    print(f"{best_plan['plan']} - ₹{best_plan['total_cost']}")
else:
    print("\nNo plans satisfy the validity and budget constraints.")