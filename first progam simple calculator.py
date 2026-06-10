def calculator():
    
    print("simple calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print ("5. exponent (**)")
    print("6. floor Division (//)")

    choice = input("choose the operation(1/2/3/4/5/6) :")
        
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))

    if choice == '1' :
        print("Result =", num1 + num2)
    if choice =='2' :
        print("Result =", num1 - num2)
    if choice == '3' :
        print("Result=", num1 * num2)
    if choice == '4' :
        if num2 != 0:
            print("Result=", num1 / num2)
        else:
            print("Error! Division by zero")
    if choice == '5' :
        print("Result=", num1 ** num2)
    if choice == '6' :
        print("Result=", num1 // num2)
    else:
        print("Invalid choice")

calculator()

