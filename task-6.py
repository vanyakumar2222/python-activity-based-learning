class Passenger:
    def __init__(self, name, age, distance, travel_class):
        self.name = name
        self.age = age
        self.distance = distance
        self.travel_class = travel_class


# Fare rates per km
CLASS_RATES = {
    "Sleeper": 0.8,
    "3AC": 1.8,
    "2AC": 2.5,
    "1AC": 4.0
}

RESERVATION_FEE = {
    "Sleeper": 20,
    "3AC": 40,
    "2AC": 50,
    "1AC": 60
}


def calculate_base_fare(distance, rate):
    """Distance slab fare calculation"""

    if distance <= 100:
        fare = distance * rate

    elif distance <= 500:
        fare = (100 * rate) + ((distance - 100) * rate * 0.9)

    else:
        fare = (100 * rate) + \
               (400 * rate * 0.9) + \
               ((distance - 500) * rate * 0.8)

    return fare


def apply_concession(fare, age):
    """Age-based concession"""

    if age < 5:
        return 0

    elif age >= 60:
        return fare * 0.60  # 40% concession

    else:
        return fare


def calculate_ticket(passenger):
    rate = CLASS_RATES[passenger.travel_class]

    fare = calculate_base_fare(passenger.distance, rate)

    fare_after_concession = apply_concession(
        fare, passenger.age
    )

    total_fare = fare_after_concession + \
                 RESERVATION_FEE[passenger.travel_class]

    return round(total_fare, 2)


def cancellation_penalty(ticket_amount):
    """
    Cancellation Penalty:
    Less than ₹100 -> ₹20
    ₹100-500 -> 10%
    Above ₹500 -> 20%
    """

    if ticket_amount < 100:
        return 20

    elif ticket_amount <= 500:
        return ticket_amount * 0.10

    else:
        return ticket_amount * 0.20


# Multiple passengers
passengers = [
    Passenger("Rahul", 30, 650, "Sleeper"),
    Passenger("Priya", 65, 650, "3AC"),
    Passenger("Aman", 10, 650, "Sleeper")
]

grand_total = 0

print("RAILWAY FARE DETAILS")
print("-" * 40)

for p in passengers:
    ticket_fare = calculate_ticket(p)
    penalty = cancellation_penalty(ticket_fare)

    grand_total += ticket_fare

    print(f"\nPassenger: {p.name}")
    print(f"Age: {p.age}")
    print(f"Class: {p.travel_class}")
    print(f"Distance: {p.distance} km")
    print(f"Ticket Fare: ₹{ticket_fare}")
    print(f"Cancellation Penalty: ₹{round(penalty, 2)}")

print("\n" + "-" * 40)
print(f"Total Reservation Cost: ₹{round(grand_total, 2)}")