total_bill = float(input(
    "Welcome to the tip calculator.\nWhat was the total bill? £"))

percentage = int(input("What percentage tip would you like to give? "))

guests = int(input("How many people are splitting the bill? "))

percentage_decimal = 1 + (percentage / 100)

total_amount = total_bill * percentage_decimal

per_person = '{:.2f}'.format(round(total_amount / guests, 2))

message = f"The total amount from a £{'{:.2f}'.format(total_bill)} bill with a {percentage}% tip is £{'{:.2f}'.format(total_amount)}.\nEach of the {guests} guests should pay approximately £{per_person}."

print(message)
