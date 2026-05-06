#task1 
num1 = float(input("enter your 1st number : "))
num2 = float(input("enter your 2nd number : "))
num3 = float(input("enter your 3rd number : "))
if num1>=num2:
    if num1>=num3:
        print("largest number is : ",num1)
    else:
        print("largest number is : ",num3)
else:
    if num2>=num3:
        print("largest number is : ",num2)
    else:
        print("largest number is : ",num3)
#task2 
num1 = float(input("enter a number : "))
num2 = float(input("enter a number : "))
if num1%num2==0:
        print("even")
else:
    print("odd")
#task3
num1 = 20
num2 = 10
print(num1 if num1>num2 else num2)

