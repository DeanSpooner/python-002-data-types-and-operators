age = input("What is your age? ")

age_int = int(age)

days_90 = 90 * 365

weeks_90 = 90 * 52

months_90 = 90 * 12

print(
    f"You have approximately {days_90 - age_int * 365} days, {weeks_90 - age_int * 52} weeks or {months_90 - age_int * 12} months left to live if you were to reach 90 years old.")
