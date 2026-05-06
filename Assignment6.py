#task 1
print("Hey ya! welcome my assignment6 game")
ch = input("enter your any alphabet : ")
if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    print("volwel")
else:
    print("consonent")
#task 2
print("now are gonna play letter grade game!")
marks = int(input("enter your number : "))
if marks >= 80 and marks <= 100:
    print("A+")
elif marks >= 70 and marks <= 79:
    print("A")
elif marks >= 60 and marks <= 69:
    print("B")
elif marks >= 50 and marks <= 59:
    print("C")
elif marks >= 33 and marks <= 49:
    print("D")
else:
    print("Fail")
#task 3
print("now we are gonna play while number game! and its automated")
i = 1
while i <= 50: 
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i = i + 1 
print("program end")
