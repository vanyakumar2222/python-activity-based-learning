import math

class CampusEvent:
    def __init__(self, venue_cost, equipment_cost,
                 catering_cost_per_person,
                 transport_cost,
                 certificate_cost_per_person,
                 participants,
                 registration_fee,
                 sponsorship_amount):

        self.venue_cost = venue_cost
        self.equipment_cost = equipment_cost
        self.catering_cost_per_person = catering_cost_per_person
        self.transport_cost = transport_cost
        self.certificate_cost_per_person = certificate_cost_per_person
        self.participants = participants
        self.registration_fee = registration_fee
        self.sponsorship_amount = sponsorship_amount

    def calculate_finances(self):

        catering_total = (
            self.catering_cost_per_person *
            self.participants
        )

        certificate_total = (
            self.certificate_cost_per_person *
            self.participants
        )

        total_cost = (
            self.venue_cost +
            self.equipment_cost +
            self.transport_cost +
            catering_total +
            certificate_total
        )

        participant_contribution = (
            self.registration_fee *
            self.participants
        )

        total_income = (
            participant_contribution +
            self.sponsorship_amount
        )

        shortfall = max(0, total_cost - total_income)

        # Variable cost per participant
        variable_cost = (
            self.catering_cost_per_person +
            self.certificate_cost_per_person
        )

        fixed_cost = (
            self.venue_cost +
            self.equipment_cost +
            self.transport_cost
        )

        contribution_per_participant = (
            self.registration_fee - variable_cost
        )

        if contribution_per_participant > 0:
            break_even_participants = math.ceil(
                max(0, fixed_cost - self.sponsorship_amount)
                / contribution_per_participant
            )
        else:
            break_even_participants = "Not Possible"

        return {
            "Catering Total": catering_total,
            "Certificate Total": certificate_total,
            "Total Cost": total_cost,
            "Participant Contribution": participant_contribution,
            "Total Income": total_income,
            "Shortfall": shortfall,
            "Break Even Participants": break_even_participants
        }


# Sample Input
event = CampusEvent(
    venue_cost=30000,
    equipment_cost=15000,
    catering_cost_per_person=250,
    transport_cost=10000,
    certificate_cost_per_person=50,
    participants=200,
    registration_fee=500,
    sponsorship_amount=25000
)

result = event.calculate_finances()

print("\nCAMPUS EVENT FINANCIAL REPORT")
print("=" * 50)

print(f"Venue Cost                    : ₹{event.venue_cost}")
print(f"Equipment Cost                : ₹{event.equipment_cost}")
print(f"Transport Cost                : ₹{event.transport_cost}")

print(f"Catering Cost                 : ₹{result['Catering Total']}")
print(f"Certificate Cost              : ₹{result['Certificate Total']}")

print("-" * 50)
print(f"Total Event Cost              : ₹{result['Total Cost']}")

print(f"\nParticipant Contributions     : ₹{result['Participant Contribution']}")
print(f"Sponsorship Amount            : ₹{event.sponsorship_amount}")

print(f"Total Income                  : ₹{result['Total Income']}")

if result['Shortfall'] > 0:
    print(f"Sponsorship Shortfall         : ₹{result['Shortfall']}")
else:
    surplus = result['Total Income'] - result['Total Cost']
    print(f"Event Surplus                 : ₹{surplus}")

print(f"\nMinimum Registrations for")
print(f"Break-Even                    : {result['Break Even Participants']}")

print("=" * 50)