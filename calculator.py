while True:
    operation = input('''Select :
+ for addition
- for subtraction
* for multiplication
/ for division
// for integer division
% for remainder
** for power
Enter your operation : ''')
    if operation!=["+","-","*","/","//","%","**"]:
        print("Invalid operation. Please enter one of the specified operators: +, -, *, /, %,//,**")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if operation == "+":
        print(f"Sum of {num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"Subtraction of {num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"Multiplication of {num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"Division of {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero.")
    elif operation == "//":
        print(f"Integer division of {num1} // {num2} = {num1 // num2}")
    elif operation == "%":
        print(f"Reminder of {num1} % {num2} = {num1 % num2}")
    elif operation == "**":
        print(f"Power of {num1} ** {num2} = {num1 ** num2}")

    repeat = input("Do you want to perform another calculation? (yes/no): ")
    if repeat.lower() != 'yes':
        print("Oky , have a nice day!")
        break