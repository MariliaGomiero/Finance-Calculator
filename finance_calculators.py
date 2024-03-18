# ******** Capstone Project ********

# Creating a program for a small company that allows the user to access two different financial calculators.
# An investment calculator and a home loan repayment calculator.

import math

# The first output that the user sees when the program runs.

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan \n")
investment_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: \n").lower()

# calculation of the future amount/monthly repayment according to the investment type the user input (investment or bond).

# Function to validate numeric inputs
def validate_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value cannot be negative.")
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

if investment_type == "investment":
    # Validate numeric inputs for amount, interest rate, and period
    amount = validate_numeric_input("What is the deposit amount?: \n")
    interest_rate = validate_numeric_input("What is the interest rate?: \n") / 100
    period_years = validate_numeric_input("Insert the number of years you plan on investing?: \n")

    # Validate input for interest type
    interest = input("Do you want simple or compound interest?: \n").lower()
    while interest not in ['simple', 'compound']:
        print("Invalid interest type.")
        interest = input("Do you want simple or compound interest?: \n").lower()

    # Calculate future value based on the selected interest type
    if interest == "simple":
        amount_future = amount * (1 + interest_rate * period_years)
    elif interest == "compound":
        amount_future = amount * math.pow((1 + interest_rate), period_years)
    else:
        amount_future = 0  # Default value if interest type is invalid

    print(f"\nFuture value of your investment: £{amount_future:.2f}")

elif investment_type == "bond":
    # Validate numeric inputs for amount, interest rate, and period
    amount = validate_numeric_input("What is the present value of your house?: \n")
    interest_rate = validate_numeric_input("What is the interest rate?: \n") / 100
    period_month = validate_numeric_input("Insert the number of months do you plan to take to repay the bond: \n")

    # Calculate monthly repayment amount
    repayment = (interest_rate * amount) / (1 - (1 + interest_rate) ** (-period_month))

    print(f"\nThis is your monthly repayment amount: £{repayment:.2f}")

else:
    print("Invalid choice. Please enter 'investment' or 'bond'.")