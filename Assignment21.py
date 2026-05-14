#task 1 (Magic Methods (__str__ & __eq__))
class smartphone:
    def __init__(self,model ,ram):
        self.model = model
        self.ram = ram
    def __str__(self):
        return(f"Smartphone: {self.model}, RAM:{self.ram} GB")
    def __eq__(self, value):
        return self.ram == value.ram
    def display(self):
        print(f"Smartphone: {self.model}, RAM:{self.ram} GB")
s1 = smartphone("Redmi note 14 5G","8")
s2 = smartphone("Samsung Galaxy A57","8")
print(s1==s2)
print(s1)
print(s2)
#task 2 (Creating Your Own Module)
import calc_tool
print(f"Total vat is: {calc_tool.total(40)}")
#task 3 (Regular Expressions (The Security Scanner))
import re
text = "My number is 01742196198 and his number is 01800000000"
numbers = re.findall(r"\d{11}", text) 
print(numbers) 

