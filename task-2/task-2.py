
n = int(input("Enter number of months: "))
bills = []

for i in range(n):
    print("\nMonth", i + 1)
    units = float(input("Enter electricity units: "))

    # Progressive slab calculation
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed = 50
    surcharge = bill * 0.05

    # 5% rebate for bills below Rs. 300
    rebate = bill * 0.05 if bill < 300 else 0

    total = bill + fixed + surcharge - rebate
    bills.append(total)

    print("Energy Charge:", round(bill, 2))
    print("Fixed Charge:", fixed)
    print("Surcharge:", round(surcharge, 2))
    print("Rebate:", round(rebate, 2))
    print("Total Bill: Rs.", round(total, 2))

print("\nMonthly Bill Comparison")

for i in range(n):
    print("Month", i + 1, ": Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if increase > 0:
            percent = increase / bills[i - 1] * 100
            print("Increase:", round(percent, 2), "%")

            if percent > 30:
                print("Unusual increase detected!")
        elif increase < 0:
            print("Bill decreased.")
        else:
            print("No change in bill.")
