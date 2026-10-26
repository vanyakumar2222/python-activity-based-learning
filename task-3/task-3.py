
n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nPatient", i + 1)

    name = input("Enter patient name: ")
    consultation = float(input("Enter consultation charges: "))
    diagnostic = float(input("Enter diagnostic charges: "))
    treatment = float(input("Enter treatment charges: "))
    age = int(input("Enter patient age: "))
    income = float(input("Enter annual family income: "))

    if consultation < 0 or diagnostic < 0 or treatment < 0:
        print("Invalid charges")
        continue

    total = consultation + diagnostic + treatment

    # Apply concessions
    concession = 0

    if age >= 60:
        concession = total * 0.10
    elif income <= 200000:
        concession = total * 0.20

    final_bill = total - concession

    # Patient classification
    if income <= 100000:
        category = "Financial Assistance"
    elif income <= 300000:
        category = "Subsidized Patient"
    else:
        category = "Regular Payment"

    print("\n--- Hospital Bill ---")
    print("Patient Name:", name)
    print("Total Charges: Rs.", round(total, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Final Bill: Rs.", round(final_bill, 2))
    print("Patient Category:", category)
