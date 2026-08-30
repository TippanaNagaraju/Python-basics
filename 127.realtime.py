#identify character types

password="Python@123"
for ch in password:
    if not ch.isalnum():
        print(ch,"----> Alpha Numeric")
  
    else:
        print(ch,"----> Specail Character" )