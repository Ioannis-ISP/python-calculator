#print("-Basic Calculator-")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# operator = input("Choose operator (+, -, *, /): ")

# if operator == "+":
#     result = num1 + num2
#     print(f"{num1} + {num2} = {result}")
# elif operator == "-":
#     result = num1 - num2
#     print(f"{num1} - {num2} = {result}")
# elif operator == "*":
#     result = num1 * num2
#     print(f"{num1} * {num2} = {result}")
# elif operator == "/":
#     result = num1 / num2
#     if num2 == 0:
#         print("Can not divide by zero")
#         exit()
#     else:    
#         print(f"{num1} / {num2} = {result}")
# else:
#     print("Invalid operator")


print("-Better Calculator-")
result = float(input("Enter number: "))

while True:
    operator = input("operator: ")
    if operator == "=":
        print(result)
        break
    else:
        try:
            number = float(input("Enter number: "))
        except ValueError:
            print("Invalid input")
            continue

    if operator == "+":
        result += number
    elif operator == "-":
        result -= number
    elif operator == "*":
        result *= number
    elif operator == "/":
        if number == 0:
            print("Can not divide by 0")
            continue
        result /= number
    else:
        print("Invalid operator")
        continue


