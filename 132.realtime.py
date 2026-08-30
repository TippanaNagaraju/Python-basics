# stop sacanning a password when a special characters found

password="Python@123"

for ch in password:
    if not ch.isalnum():
        print("Special character found:" ,ch)
        break