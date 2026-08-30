#identify character types

password="Python@123"
for ch in password:
    if ch.isupper():
        print(ch,"----> Uppercase Letter")
    elif ch.islower():
        print(ch,"----> Lowercase Letter")
    elif ch.isdigit():
        print(ch,"---->Digital Number" )    
    else:
        print(ch,"----> Specail Character" )