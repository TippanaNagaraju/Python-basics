num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number :"))
choice=input("Enter Operator (+,-,*,/)")

match choice:    
    case "+":
        print("Resuly=",num1+num2)
    case "-":
        print("Result=",num1-num2)
    case "*":
        print("Result=",num1*num2)
    case "/":
        if num2!=0:
            print("Result=",num1/num2)
        else:
            print("Division by zero is not Allowed")
    case _:
            print("Invalid Operator: ")