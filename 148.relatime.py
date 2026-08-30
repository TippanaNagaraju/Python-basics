# ATM pin verification using for loop
correct_pin="6264"
for attempt in range(1,4):
    pin=input("Enter ATM pin: ")
    if pin==correct_pin:
        print("Login Sucessful")
        break
    else:
        print("Incorrect Pin")
else:
    print("ATM card Blocked")