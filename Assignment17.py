#task 1
user = int(input("Enter Your Age: ")) #mistake 1
def check_age(user_age):
    if user_age < 18: 
        raise ValueError("Access Denied: You are too young for ROM Porting!")
    return "You are allowed to port ROM"

try:
    print(check_age(user)) #mis 2
except ValueError as e:
    print(e)
#task 2
print("Smart Swapping (The Variable Exchange)")
phone_1 = "Redmi"
phone_2 = "Samsung"
phone_1 ,phone_2 = phone_2 ,phone_1
print("phone 1 :",phone_1)
print("phone 2 :",phone_2)
#task 3
print("Your First Class (The Mobile Architect)")
class mobile:
    model =""
    chipset = ""
Redmi = mobile()
Redmi.model = "Redmi Note 14 5g"
Redmi.chipset = "Mediatek Dimensity 7025 Ultra"
print(f"Phone name is :{Redmi.model}\n This phone is powered by :{Redmi.chipset}")

