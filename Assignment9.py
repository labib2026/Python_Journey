#task 1 
for x in range(2,101,2):
    print(x)
#task 2
Θ = int(input("enter your last number : "))

for x in range(Θ+1):
    print(x*"Θ")
# task 3
from random import randint
randomnumber = randint(1, 10) # লুপের বাইরে একবার
for x in range(1, 6):
    guessnumber = int(input("Guess a number between 1 to 10 : "))
    if guessnumber == randomnumber:
        print("System Access Granted! You won.")
        break # জিতলে লুপ থামিয়ে দাও
    else:
        print("Access Denied!")

# ৫ বার শেষ হলে আসল নম্বর দেখানো (ঐচ্ছিক)
print("The secret number was:", randomnumber)
