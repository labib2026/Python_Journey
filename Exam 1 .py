# level 1
user = float(input("enter your number : "))
if user>=10 and user<=50 and user%3==0:
     print("Target Matched")
else:
    print("Not Matched")
# level 2
prices = [100, 250, 400, 50, 800]
valu = list(filter(lambda x : x<500, prices))
tax = [x*1.05 for x in valu ]
print(tax)
#level 3
try:
        file = open("log.txt", "r")
        text = file.read()
        print(text)
except FileNotFoundError:
      print("Security Alert: Log file missing!")

file.close()