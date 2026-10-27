class ManufacturingProduct:
    def __init__(self, name, units_produced,
                 material_cost_per_unit,
                 labour_cost_per_unit,
                 machine_cost_per_unit,
                 wastage_percentage,
                 selling_price_per_unit):

        self.name = name
        self.units_produced = units_produced
        self.material_cost_per_unit = material_cost_per_unit
        self.labour_cost_per_unit = labour_cost_per_unit
        self.machine_cost_per_unit = machine_cost_per_unit
        self.wastage_percentage = wastage_percentage
        self.selling_price_per_unit = selling_price_per_unit

    def calculate_profitability(self):

        material_cost = self.units_produced * self.material_cost_per_unit
        labour_cost = self.units_produced * self.labour_cost_per_unit
        machine_cost = self.units_produced * self.machine_cost_per_unit

        wastage_cost = material_cost * (self.wastage_percentage / 100)

        total_cost = (
            material_cost +
            labour_cost +
            machine_cost +
            wastage_cost
        )

        revenue = (
            self.units_produced *
            self.selling_price_per_unit
        )

        profit = revenue - total_cost

        profit_percentage = (
            (profit / total_cost) * 100
            if total_cost > 0 else 0
        )

        return {
            "Material Cost": material_cost,
            "Labour Cost": labour_cost,
            "Machine Cost": machine_cost,
            "Wastage Cost": wastage_cost,
            "Total Cost": total_cost,
            "Revenue": revenue,
            "Profit": profit,
            "Profit %": profit_percentage
        }


# -------------------------
# Sample Product Details
# -------------------------

product = ManufacturingProduct(
    name="Steel Component",
    units_produced=1000,
    material_cost_per_unit=50,
    labour_cost_per_unit=20,
    machine_cost_per_unit=10,
    wastage_percentage=5,
    selling_price_per_unit=95
)

# Target Profit
TARGET_PROFIT = 10000

# Analysis
result = product.calculate_profitability()

print("\nMANUFACTURING COST ANALYSIS")
print("=" * 40)

print(f"Product                : {product.name}")
print(f"Units Produced         : {product.units_produced}")

print(f"\nMaterial Cost          : ₹{result['Material Cost']:.2f}")
print(f"Labour Cost            : ₹{result['Labour Cost']:.2f}")
print(f"Machine Cost           : ₹{result['Machine Cost']:.2f}")
print(f"Wastage Cost           : ₹{result['Wastage Cost']:.2f}")

print(f"\nTotal Production Cost  : ₹{result['Total Cost']:.2f}")
print(f"Sales Revenue          : ₹{result['Revenue']:.2f}")

print(f"\nProfit/Loss            : ₹{result['Profit']:.2f}")
print(f"Profit Percentage      : {result['Profit %']:.2f}%")

if result['Profit'] >= TARGET_PROFIT:
    print("\n✅ Target Profit Achieved")
else:
    shortfall = TARGET_PROFIT - result['Profit']
    print(f"\n❌ Target Not Achieved")
    print(f"Profit Shortfall: ₹{shortfall:.2f}")