# match case
# week days

day=int(input("Enter Day Number (1-7): "))

match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")            
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturdayy")
    case 7:
        print("sunday")
    case _:
        print("Invalid Day Number")                            
                    
