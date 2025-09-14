print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

match choice:
    case 1:
        result = num1 + num2
    case 2:
        result = num1 - num2
    case 3:
        result = num1 * num2
    case 4:
        result = num1 / num2 if num2 != 0 else "Error! Division by zero."
    case _:
        result = "Invalid choice"

print("Result:", result)
