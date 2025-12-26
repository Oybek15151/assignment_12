with open("donations.txt", "w") as file:
    file.write(
        "Alice,HomelessShelter,200,100\n"
        "Bob,FoodBank,50,50\n"
        "Charlie,HomelessShelter,400,200\n"
        "Diana,AnimalRescue,1000,0\n"
        "Corrupt,Line,No,Money\n"
        "Eve,FoodBank,20,10\n"
        "Frank,AnimalRescue,300,300\n"
    )


def process_donations(filename):
    cause_totals = {}
    top_donors = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) != 4:
                continue

            donor, cause, cash, check = parts

            try:
                cash = float(cash)
                check = float(check)
            except ValueError:
                continue

            total = cash + check
            cause_totals[cause] = cause_totals.get(cause, 0) + total

            if total > 500:
                top_donors.append((donor, total))

    return cause_totals, top_donors


def write_fundraising_report(cause_totals, top_donors):
    with open("fundraising_summary.txt", "w") as file:
        file.write("FUNDS RAISED PER CAUSE\n")
        file.write("----------------------\n")

        for cause, total in cause_totals.items():
            file.write(f"{cause}: ${total:.2f}\n")

        file.write("\nGOLD TIER DONORS (> $500)\n")
        file.write("-------------------------\n")

        for donor, amount in top_donors:
            file.write(f"{donor} (${amount:.2f})\n")


cause_totals, top_donors = process_donations("donations.txt")
write_fundraising_report(cause_totals, top_donors)
