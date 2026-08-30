#identify character types

password="Python@123"
for ch in password:
    if ch.isalnum():
        print(ch,"----> Alpha Numeric")
  
    else:
        print(ch,"----> Specail Character" )