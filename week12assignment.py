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
                cash_amount = float(cash)
                check_amount = float(check)
            except ValueError:
                continue

            total_donation = cash_amount + check_amount

            if cause not in cause_totals:
                cause_totals[cause] = 0
            cause_totals[cause] += total_donation

            if total_donation > 500:
                top_donors.append((donor, total_donation))

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
