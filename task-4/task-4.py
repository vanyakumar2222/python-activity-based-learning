
name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime amount: "))
incentives = float(input("Enter incentives: "))

gross = basic + allowances + overtime + incentives

# Progressive deductions
if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 50000:
    deduction = 20000 * 0.05 + (gross - 20000) * 0.10
else:
    deduction = (20000 * 0.05 +
                 30000 * 0.10 +
                 (gross - 50000) * 0.20)

net = gross - deduction

print("\n===== SALARY STATEMENT =====")
print("Employee Name :", name)
print("Basic Pay     : Rs.", round(basic, 2))
print("Allowances    : Rs.", round(allowances, 2))
print("Overtime      : Rs.", round(overtime, 2))
print("Incentives    : Rs.", round(incentives, 2))
print("----------------------------")
print("Gross Salary  : Rs.", round(gross, 2))
print("Deductions    : Rs.", round(deduction, 2))
print("Net Salary    : Rs.", round(net, 2))
