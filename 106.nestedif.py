# marks=80
# attendence=90
# if marks>=35:
#     if attendence>=75:
#         print("student passed")
marks=80
attendence=90
marks=int(input("Enter narks : "))
attendence=int(input("Enter attendence : "))
if marks>=35:
    if attendence>=75:
        print("student passed")
    else:
        print("student failed(attendence)")
else:
    print("student failed(marks)")