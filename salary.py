base_salary = int(input("Enter your Base Salary per month:"))
baremin_allowance = (20/100) * base_salary
house_rent_allowance = (10/100) * base_salary
transport_allowance = (5/100) * base_salary
total_salary = base_salary + baremin_allowance + house_rent_allowance + transport_allowance
total_base_salary = base_salary * 12
salary_per_year = total_salary * 12
final_salary = 0

if salary_per_year < 250000 :
    print(f"{salary_per_year} Rs is your Salary.")
    print("You are Exempted From Tax.")

elif salary_per_year < 600000:
    print("You come under 5% Tax Bracket")
    final_salary = salary_per_year - (5/100)*salary_per_year
    print(f"{salary_per_year} salary before taxes.")
    print(f"{final_salary} salary after taxes.")

elif salary_per_year < 900000:
    print("You come under 10% Tax Bracket")
    final_salary = salary_per_year - (10/100)*salary_per_year
    print(f"{salary_per_year} salary before taxes.")
    print(f"{final_salary} salary after taxes.")

elif salary_per_year < 1200000:
    print("You come under 15% Tax Bracket")
    final_salary = salary_per_year - (15/100) *salary_per_year
    print(f"{salary_per_year} salary before taxes.")
    print(f"{final_salary} salary after taxes.")
elif salary_per_year < 1500000:
    print("You come under 20% Tax Bracket")
    final_salary = salary_per_year - (20/100)*salary_per_year
    print(f"{salary_per_year} salary before taxes.")
    print(f"{final_salary} salary after taxes.")
elif salary_per_year > 1500000:
    print("You come under 25% Tax Bracket")
    final_salary = salary_per_year - (25/100)*salary_per_year
    print(f"{salary_per_year} salary before taxes.")
    print(f" {final_salary} salary after taxes.")
elif salary_per_year > 5000000:
    print("You come under Criminal Tax Bracket")
    final_salary = salary_per_year - (10/100) *salary_per_year
    print("salary gayi bhaad ma < tm pehzai Jail chalo.")