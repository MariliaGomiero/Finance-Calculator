# ******** Capstone Project ********

# Creating a program for a small company that allows the user to access two different financial calculators.
# An investment calculator and a home loan repayment calculator.

import math

# The first output that the user sees when the program runs.

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan \n")

investment_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: \n").lower()

# Improved input validation
while investment_type not in ['investment', 'bond']:
    print("Invalid choice. Please enter 'investment' or 'bond'.")
    investment_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: \n").lower()

# calculation of the future amount/monthly repayment according to the investment type the user input (investment or bond).

if investment_type == "investment":
    amount = (float(input("What is the deposit amount?: \n")))
    interest_rate = (float(input("What is the interest rate?: \n")))/100
    period_years = (int(input("Insert the number of years you plan on investing?: \n")))
    interest = input("Do you want simple or compound interest?: \n").lower()

    if interest == "simple":
       amount_future = amount * (1 + interest_rate*period_years)
    elif interest == "compound":
       amount_future = amount * math.pow((1+interest_rate), period_years)
    else:
        print("Invalid interest type.")  # the user will get this message if they input a different interest type than simple or compound.
        amount_future = 0  
    
    print(f"\nFuture value of your investment: £{amount_future:.2f}")

elif investment_type == "bond":
     amount = (float(input("What is the present value of your house?: \n")))
     interest_rate = ((float(input("What is the interest rate?: \n")))/100)/12
     period_month = (int(input("Insert the number of months do you plan to take to repay the bond: \n")))
   
     repayment = (interest_rate*amount)/(1-(1+interest_rate)**(-period_month))

     print(f"\nThis is your monthly repayment amount: £{repayment:.2f}")

else:
     print("Invalid choice. Please enter 'investment' or 'bond'.") # the user will get this message if they input a different investment type than investment or bond.