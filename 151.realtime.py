# atm language selection
langugae=input("Choose Langugae(EN/TE/HI):")

match langugae:
    case "EN":
        print("English Selected")
    case "TE":
        print("Telugu Selected")
    case "HI":
        print("Hindi Selected")
    case _:
        print("Langugae not Avilable")