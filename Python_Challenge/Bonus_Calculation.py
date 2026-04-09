# Program to calculate bonus based on salary

def calculate_bonus(salary):
    bonus = salary * 0.07   # 7% bonus
    return bonus

# Taking input
salary = float(input("Enter your salary: "))

# Function call
bonus = calculate_bonus(salary)

# Display result
print("Bonus =", bonus)


# Example Output:
# Enter your salary: 45000
# Bonus = 3150.0