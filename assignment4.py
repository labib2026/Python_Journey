#task 1 
print("Welcome \n Entering the lobby")
password = input("Enter your password : ")

if password == "dev123":
    print("Access Granted! Welcome Developer.")
else:
    print("Access Denied! Wrong Password.")

#task 2
print("Hey! before you coding can you tell me your battery satus?")

battery = float(input("Enter your battery status : "))
if battery >=80:
    print("Battery Full! You can start your mission.")
elif battery >=20:
    print("Battery OK. Keep coding.")
else:
    print("Warning! Please connect your charger.")