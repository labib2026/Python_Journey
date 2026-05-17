#task 1 (The Secure File Logger (with open & Exception))
try:
    with open("system_log.txt","r") as file:
            content = file.read()
            print(content)
            file.close()
except FileNotFoundError:
    print("file not found")
finally:
     print("Log Scan Complete.")
#task 2 (Smart Math Scanner (Multiple Errors))
try:
     user = int(input("Enter your first number : "))
     user2 = int(input("Enter your second number : "))
     sum = user / user2
     print(sum)
except ZeroDivisionError,ValueError:
     print("Error: Please enter a valid number!")
# task3
import re
text = "Contact security at labib9690@gmail.com for the corrupted memory block 0x5b3c."
pattern = r"labib9690@gmail.com"
match = re.findall(pattern,text)
pattern2 = r"0x([a-f0-9]+)"
match2 = re.findall(pattern2,text)
print("Your Gmail is",match)
print("Hexadecimal characters found:",match2)
