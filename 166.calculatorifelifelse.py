def calculator(num1,num2=10,operation="+"):
    if operation =="+":
        print("addition",num1,operation,num2,"=",num1+num2)
    elif operation=="-":
        print("subraction",num1,operation,num2,"=",num1-num2)

calculator(20)
calculator(20,5,"+")
calculator(20,16,"-")