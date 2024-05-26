""" This is a basic calculator that does addition, subtraction, multiplication and division
    with two variables. I used a while loop, if-elif-else block, and the break keyword in 
    this script. """

print("Welcome to my simple calculator!")
print("This calculator does addition, subtration, multiplcation, and division with two variables.")

while True:
    var_1 = int(input("Input the first vriable: "))
    var_2 = int(input("Input the second variable: "))
    operator = input("Enter the operator symbol (+, -, *, /) or spell it out (add, subtract, multiple, divide): ")
    operator = operator.lower()
    if operator == "add" or operator == "+":
        print(var_1 + var_2)
    elif operator == "subtract" or operator == "-":
        print(var_1 - var_2)
    elif operator == "multiple" or operator == "*":
        print(var_1 * var_2)
    elif operator == "divide" or operator == "/":
        print(var_1 / var_2)
    else:
        print("Try again.")
    input_quit = input("Press 'q' if you would like quit or any key to continue: ")
    if input_quit == "q":
        break
