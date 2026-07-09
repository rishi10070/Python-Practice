hourly_wage = float(input("Hourly wage:"))
hours_worked = float(input("Hours worked:"))
days_of_week = input("Day of the week:")
if days_of_week == "Sunday":
    hourly_wage *= 2

total_wages = hourly_wage * hours_worked
print(f"Daily wages: {total_wages} euros") 