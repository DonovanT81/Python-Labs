#Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
weeks_per_year = 52
total_years = 90

new_age = float(age)
weeks_left = (total_years * weeks_per_year) - (new_age * weeks_per_year)
last_weeks = int(weeks_left)


print(f"You have {last_weeks} weeks left.")
