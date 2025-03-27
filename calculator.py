# Basic Calculator Program

# Function to perform the operation
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator!"

# Take user input
print("Welcome to the simple calculator!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

# Perform the calculation and display the result
result = calculate(num1, num2, operator)
print(f"The result of {num1} {operator} {num2} is: {result}")
