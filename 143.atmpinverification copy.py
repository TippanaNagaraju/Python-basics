correct_pin = "6264"
attempt = 1

while attempt <= 3:
    pin = input("Enter ATM PIN: ")

    if pin == correct_pin:
        print("Login Successful")
        break
    else:
        print("Incorrect PIN")

    attempt += 1

if attempt > 3:
    print("ATM Card Blocked")