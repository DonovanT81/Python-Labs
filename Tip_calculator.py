#inputs
print("Welcome to the Tip Calculator!")
total_bill = float(input("How much was your total bill? $ "))
tip_amount = float(input("How much would you like to tip? 10, 12, 15? "))
total_party = int(input("How many people will be splitting the bill? "))


#conversions
tip_conversion = tip_amount / 100
total_bill_tip = total_bill * (1 + tip_conversion)
payment_per_person = total_bill_tip / total_party
payment_per_person = round(payment_per_person, 2)
print(f"Each person should pay: ${payment_per_person: .2f}")