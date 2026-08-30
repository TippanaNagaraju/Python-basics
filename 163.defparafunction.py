def calculate_bill(amount,gst=18):
    total=amount+(amount*gst/100)
    print("total bill=",total)

calculate_bill(1000)
calculate_bill(1450)
calculate_bill(1810)
calculate_bill(1810)