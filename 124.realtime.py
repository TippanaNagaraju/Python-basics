#sending reminder messages with delay
import time
for customer in range (1,6):
    print("Reminder sent to customer",customer)
    time.sleep(2)

print("All rminders have been sent sucessfully")