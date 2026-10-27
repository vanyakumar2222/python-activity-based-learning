class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity


# Category-wise tax rates (%)
TAX_RATES = {
    "Grocery": 5,
    "Electronics": 18,
    "Clothing": 12,
    "Books": 0
}

# Discount rules
DISCOUNT_THRESHOLD = 5000      # Bill amount threshold
DISCOUNT_PERCENT = 10          # 10% discount
MAX_DISCOUNT = 1000            # Maximum concession allowed


def calculate_bill(products):
    subtotal = 0
    total_tax = 0

    print("=" * 80)
    print("RETAIL BILL INVOICE")
    print("=" * 80)
    print(f"{'Product':15}{'Category':15}{'Qty':5}{'Price':10}"
          f"{'Amount':12}{'Tax':10}")

    for product in products:
        amount = product.price * product.quantity

        tax_rate = TAX_RATES.get(product.category, 0)
        tax = amount * tax_rate / 100

        subtotal += amount
        total_tax += tax

        print(f"{product.name:15}{product.category:15}"
              f"{product.quantity:<5}{product.price:<10.2f}"
              f"{amount:<12.2f}{tax:<10.2f}")

    # Threshold discount
    discount = 0
    if subtotal >= DISCOUNT_THRESHOLD:
        discount = subtotal * DISCOUNT_PERCENT / 100

        # Apply max concession limit
        if discount > MAX_DISCOUNT:
            discount = MAX_DISCOUNT

    final_amount = subtotal + total_tax - discount

    print("-" * 80)
    print(f"Subtotal        : ₹{subtotal:.2f}")
    print(f"Total Tax       : ₹{total_tax:.2f}")
    print(f"Discount        : ₹{discount:.2f}")
    print(f"Net Payable     : ₹{final_amount:.2f}")
    print("=" * 80)

    return final_amount


# Sample Products
products = [
    Product("Rice", "Grocery", 60, 20),
    Product("Laptop", "Electronics", 45000, 1),
    Product("Shirt", "Clothing", 1200, 2),
    Product("Book", "Books", 500, 3)
]

# Generate Bill
calculate_bill(products)