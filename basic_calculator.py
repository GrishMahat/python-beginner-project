print("Welcome to the Calculator Program!")
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
operator = input("Please enter the operation (+, -, *, /):")

if operator == "+":
    r = num1 + num2
    print("The result is:", r)
elif operator == "-":
    r = num1 - num2
    print("The result is:", r)
elif operator == "*":
    r = num1 * num2
    print("The result is:", r)
elif operator == "/":
    r = num1 / num2
    print("The result is:", r)
else:
    print("Error: Invalid operator.")
