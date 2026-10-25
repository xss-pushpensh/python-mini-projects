from datetime import date

print("=" * 35)
print("       AGE CALCULATOR")
print("=" * 35)

try:
    dob_input = input("Enter your date of birth (DD-MM-YYYY): ")

    # Convert input into a date
    day, month, year = map(int, dob_input.split("-"))
    dob = date(year, month, day)
    today = date.today()

    # Validate date of birth
    if dob > today:
        print("Error: Date of birth cannot be in the future.")

    else:
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        # Adjust negative days
        if days < 0:
            months -= 1

            # Find days in the previous month
            if today.month == 1:
                previous_month = 12
                previous_year = today.year - 1
            else:
                previous_month = today.month - 1
                previous_year = today.year

            days_in_previous_month = (
                date(previous_year, previous_month + 1, 1)
                - date(previous_year, previous_month, 1)
            ).days if previous_month < 12 else (
                date(previous_year + 1, 1, 1)
                - date(previous_year, 12, 1)
            ).days

            days += days_in_previous_month

        # Adjust negative months
        if months < 0:
            years -= 1
            months += 12

        print("\nYour Age:")
        print(f"Years  : {years}")
        print(f"Months : {months}")
        print(f"Days   : {days}")

except ValueError:
    print("Invalid date! Please enter DD-MM-YYYY, e.g. 15-08-2005.")