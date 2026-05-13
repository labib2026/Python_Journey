# my first comment 
'''
Multiple comment 
making
'''
'''
print("Hello from PC!")
print("ami code bhalobash")
print("YT: TSUKOYOMI")
print("ami ki bhul korlam")
print("\"labib\"")
print("Ashir \n Inteser")
#print("ashir \t inteser")

'''
'''
# tuto 6
a = 13
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
'''
'''
# tuto 7
name = input("Enter your name : ")
age = input("Enter your age : ")
gpa = input("Enter your GPA : ")
print("Student Verification")
print("---------------------")

print("Name : "+name)
print("Age : "+age)
print("GPA :"+gpa)
'''
'''
# tuto 8
num1 = input("Enter your first number : ")
num2 = input("Enter your second number : ")

result = int(num1) + int(num2)
print("The result is" ,result)

result = int(num1) - int(num2)
print("The result is" ,result)
'''
'''
 # tuto 9
area = float(input("Enter length of side = "))

area = area * area
print("your area is" ,area)

area = float(input("Enter radius = "))

area = 3.1416 * area * area
print(area)
'''
'''
#tuto 10
from math import *

print(max(30,90))
print(min(30,90))
print(pow(30,90))
print(abs(-78))
print(sqrt(225))
print(round(7.89789))
print(floor(8.9))
print(ceil(8.9))
'''
'''
# tuto 11
#type function
print(type(False))

num = "labib"
print(type(num))
# formatted string
num1 = 20
num2 = 30
print(f"{num1} + {num2} = {num1+num2} ")

print("labib" ,end=" ")
print("01742196198")
'''
'''
#tuto 12
print(18>=18) #relational oparation
print(30>20)
print(30<=20)
print(30==20)
print(30!=20)
print(30>20)
print("labib" == "anis")
'''
'''
mark = 90

if mark >= 80:
    print("Grade A+")
elif mark >= 70:
    print("Grade A")
elif mark >= 60:
    print("Grade B")
else:
    print("Fail")
'''
'''
#tuto 14
num = 4
if num%2 == 0:
    print("Even")
else:
    print("Odd")
print("md labib" ,end=" ")
print("01742196198")
'''
'''
#tuto 15
mark = 100
if mark>=80:
    print("A+")
elif mark>=70:
    print("A")
elif mark>=60:
    print("A-")
elif mark>=50:
    print("B")
elif mark>=33:
    print("C")
else:
    print("Fail")
'''
'''
#tuto 16 #inner if statemant
n1 = 85
n2 = 40
n3 = 80
if n1>n2:
    if n2<n3:
        print(n3)
else:
    print("hello")

m1 = 90
m2 = 123
m3 = 133
m4 = 144
if m1<m2:
    if m2<m3:
        if m3<m4:
            print("hello")
else:
    print("good bye")
'''
'''
#tuto 17 #Ternary Operator
num1 = 89
num2 = 40
#if num1<num2:
    #print(num2)
print(num1 if num1>num2 else num2)
'''
'''
#tuto 19
num1 = 40
num2 = 50 
num3 = 30
num4 = 10

if num1>num2 and num1>num3 and num1>num4:
    print(num1)
elif num2>num1 and num2>num3 and num2>num4:
    print(num2)
elif num3>num1 and num3>num2 and num3>num4:
    print(num3)
else:
    print(num4)
'''
'''
#tuto 20
i = 1 
while i<=10:
    print(i)
    i = i+1
print("Program end")
'''
'''
#tuto 21 
n = float(input("enter the last term : "))
i=2
sum = 0
while i<=n:
    sum = sum+i
    i = i + 2
print(sum)
'''
'''
#tuto 22
i = 1
while i<=100:
    print(i)
    i = i + 2
    if i == 20:
        continue
'''
'''
#tuto 23
subject = ["bangla","english","math","c","c++","java"] #list
print (subject)
'''
'''
#tuto24
subject = ["bangla","english","math","c","c++","java"]
print(len(subject))
#subject.append("TOC")
#print(subject)
subject.insert(3,"OS")
print(subject)
subject.remove("OS")
print(subject)
subject.sort()
print(subject)
subject.reverse()
print(subject)
subject.pop()
print(subject)
subject.clear()
print(subject)
subject1 = [20,245,44,4,4444]
subject2 = subject1.copy()
print(subject2)
'''
'''
#tuto 25
num = list(range(2,101,2))#range function
print(num)
'''
'''
a = int(input("enter 1st number : "))
b = int(input("enter 2nd number : "))

if a % b == 0:
    print(0)
else:
    print(b - (a % b))
'''
'''
# tuto 26 (for loop)
num = [10,20,30,40,50,60]
sum = 0 
for x in num:
    sum = sum + x
print(sum)

#index = 0 
#n  = len(num)
#while index <=n:
    #print(num[index])
    #index = index + 1
'''
'''
# tuto 27 
# 2 + 4 + 6+...+n
n = int(input("enter your last number : "))
sum = 1
for x in range(2,n+1,2):
    sum = sum * x
print(sum)
'''
'''
# tuto 28 
Θ = 3 
for x in range(Θ+1):
    print((2*x-1)*"Θ")
Θ = 6 
for x in range(Θ+1):
    print(x*"Θ")
'''
'''
# tuto 29
from random import randint
for x in range(1,6):
    guessnumber = int(input("enter a number between 1 to 5 : "))
    randomnumber = randint(1,5)


    if guessnumber == randomnumber:
     print("you have won")
    else:
        print("you have lost")
        print("random number was: ",randomnumber)
'''
'''
#tuto 30
n = input("enter a text of numbers : ")
list = n.split()
sum = 0 

for num in list:
    sum = sum + int(num)
print(sum)
numofwords = 0
numofletters = 0 
numofdigits = 0

text = input("enter a text of numbers : ")
for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numofletters = numofletters + 1
    elif x >= '0' and x <= '9':
        numofdigits = numofdigits + 1
    elif x == ' ':
        numofwords = numofwords + 1
print("the number of word is : " ,numofwords+1)
print("the number of letter is : " ,numofletters)
print("the number of digit is : " ,numofdigits)
'''
'''
#tuto 31 matrix
matrix = [
    [1,2,3],
    [4,5,6],
]

for row in matrix:
    for column in row:
        print(column)
'''
'''
#TUTO 32 dictionary
studentid = {
    101 : "md ashir intesir",
    102 : "md robin",
    103 : "md sun",
    104 : "md anisul haque",
}
print(studentid.get(106,"not a valid key"))
'''

'''
#tuto 33 tuples 
student = (
    ("md labib",19,4.93),
    "md sun",
    "md robin",
)
print(student)
'''
'''
#tuto 34 sets
num1 = {1,2,3,4,5,6}
num2 = set({5,6,7,8,9})
print(num1 | num2)# union set
print(num1 & num2)#intersection set
print(num1 - num2)
'''
'''
#tuto 35 (Stack And Queue)
books = [ ] # stack
books.append("learn c")
books.append("learn c++")
books.append("learn java")
print(books)
books.pop()
print("the top book is : ", books[-1])

books.pop()
print("the top book is : ", books[-1])
books.pop()
if not books:
    print("there no books left ")
# tuto 35 part 2 queue
from collections import deque
bank = deque(["anis","labib","robin"])
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
if not bank:
    print("no one left in bank")
'''
#tuto 36 user function library\user
'''
def add(x,y):
    sum = x + y
    print(sum)
add(10,20)
'''
'''
#tuto 37 Returning Value from function
def add(x,y):
    sum = x+y
    return sum
result = add(30,50)
print(result)
'''
'''
#tuto 38 xargs xxargs
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
add(70,10)
add(70,10,10)
#xxargs 
def student(**details):
    print(details["name"])
student(id = 101 ,name = "labib")
'''
'''
#tuto 39(Debugging)
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

print(add(10,20))
'''
'''
# tuto 40 (lambda function)
a = (lambda a,b : a*a + 2*a*b + b*b)(2,3)
print(a)
b = (lambda x: x*x*x) (4)
print(b)
'''
'''
#tuto 41( map and filter function)
def add(x):
    return x*x

num = [1,2,3,4]
a= list(map(add,num))
print(a)
# filter function 
num = [1,3,4,8]
a=list(filter(lambda x: x%2==0,num))# filter function
print(a)
'''
'''
# tuto 42 (List Comprehensions)
num = [1,2,5,8,9]
a= [x for x in num if x%2==0] # aamar question je ekhane [x%2==0 for x in num] dile true fales asche keno?
#a = list(map(lambda x: x*x,num))
print(a)
'''
'''
# tuto 43 (Zip Function)
name = ["labib","robin","sun"]
roll = [101,102,103]
print(list(zip(name,roll,"ABA")))
'''
'''
# tuto 44 (Recursion)
def fact(n):
    if n == 1:
        return 1
    else:
        return n *fact(n-1)
print(fact(5))
'''
'''
#tuto 45 (Reading a file)\
file = open("intro.txt", "r")
print(file.readable())
file.close()
acc = open("student.txt", "r+")
#text = acc.readlines()
#print(text)
#size = len(text)
#print(size)
for line in acc:
    print(line)
acc.close()
'''
'''
# tuto 46 (writing in a file)
file = open("student.txt","a")
write = file.write("\nMd Sazzad - Automobile")
'''
'''
# tuto 47 (Exception Handling) part 1
try:
    list = [20,0,80]
    result = list[0] / list[3]
    print(result)
    print("done")
except ZeroDivisionError:
  print("can't divaded by zero")
except IndexError:
   print("index error")
finally:
   print("succesful")
'''
'''
# tuto 48 (Exception Handling (part-2))
def voter(age):
    if age<18:
        raise ValueError("Invalid voter")
    return("You are allowed to vote")
try:
    print(voter(15))
except ValueError as e:
    print(e)
'''
'''
# tuto 49 (Swapping | End of Basic Python)
a= 20 
b = -10
a, b = b , a
print("a = ",a)
print("b = ",b)
'''
'''
#tuto 50 (Introduction to OOP | class and object)
class student:
    roll = ""
    gpa = ""

rahim = student()
#print(isinstance(rahim,student))
rahim.roll= 101
rahim.gpa = 4.5
print(f"Roll : {rahim.roll}, Gpa : {rahim.gpa}")
karim = student()
karim.roll= 102
karim.gpa = 4.0
print(f"Roll : {karim.roll}, Gpa : {karim.gpa}")
'''
'''
# tuto 51 (Introducing Methods)
class student:
    roll = ""
    gpa = ""
    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll} , Gpa : {self.gpa}")

rahim = student()
rahim.set_value(101,4.75)
rahim.display()
'''
'''
# tuto 52 (Constructors)
class student:
    roll = ""
    gpa = ""

    def __init__(self, roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
            print(f"Roll : {self.roll}, Gpa : {self.gpa}")

rahim = student(101,5)
rahim.display()
'''
'''
# tuto 53 (Exercise) by creating class and object with constructor
class triangle:
    base = ""
    height = ""
    def __init__(self, base,height):
        self.base  = base
        self.height = height
    def area(self):
        area = 0.5 * self.base * self.height
        print("Area = ",area)
t1 = triangle(10,20)
t1.area()

t2 = triangle(20,30)
t2.area()
'''
'''
# tuto 54 (Inheritance)
class phone:
    def call(self):
        print("You can call")
    def massage(self):
        print("Youu can massage")

class samsung(phone): # inheritance
    def photo(self):
        print("You can take photo")
s = samsung()
s.call()
s.massage()
s.photo()
print(issubclass(samsung,phone))
'''
'''
# tuto 55 (Method Overriding)
class phone():
    def __init__(self):
        print("I in super class")
class samsung(phone):
    def __init__(self):
        super().__init__() 
        print("I am in samsung class")

s = samsung()
'''
'''
# tuto 56 (A practical example of inheritance)
class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    def area(self):
        print("area of shape")

class triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("area of triangle =" ,area)
class rectengle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("area of rectengle = ",area)
t1 = triangle(20,10)
t1.area()
t2 = rectengle(20,10)
t2.area()
'''
'''
# tuto 57 (Types Of Inheritance)
#Multi-level Inheritance=
class A:
    def display1(self):
        print("I am in inside in A class")
class B(A):# a class inharitation
    def display2(self):
        print("I am in inside in B class")
class C(B):# a,b class inharitation
    def display3(self):
        super().display1()
        super().display2()
        print("I am in inside in C class")
T1 = C()
T1.display3()
#Multiple Inheritance
class A:
    def display(self):
        print("I am in inside in A class")
class B:
    def display(self):
        print("I am in inside in B class")
class C(A,B):
    pass
t1 = C()
t1.display()
'''
'''
# tuto 58(Abstraction)

from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self ,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    @abstractmethod
    def area(self):
        pass

class Triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of triangle : ",area)
class Rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle :",area)
t1 = Triangle(20,30)
t1.area()
r2 = Rectangle(50,30)
r2.area()
'''
'''
# tuto 59 (Polymorphism)
print(len("LABIB"))
print(len([1,2,3,4,5]))

class device:
    def __init__(self,model):
        self.model = model
class phone(device):
    def __init__(self, model, chipset):
        super().__init__(model)
        self.chipset = chipset
    def display(self):
        print(f"This is {self.model} and powered with {self.chipset}")
p1 = phone("Samsung Galaxy S21", "Snapdragon 888")
p1.display()
'''
# tuto 60 (Magic methods)
class bike:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __eq__(self, other):# equality magic method 
        return self.name == other.name and self.color == other.color;
    def __str__(self): # string magic method
        return(f"Name = {self.name}, Color = {self.color}")

    def display(self):
        print(f"Name = {self.name}, Color = {self.color}")
d1 = bike("Yamaha R15", "Blue")
d2 = bike("Yamaha R15","Blue")
print(d1==d2)
# tuto 61 (Creating your own Module)
from Cw import Triangle_area,Rectangle_area
Triangle_area(7,8)
Rectangle_area(8,7)
# tuto 62 (Regular expressions)
import re
color = r"red"
if re.search(color,"i love blue color"):
    print("matched")
else:
    print("not matched")
color = r"red"
if re.match(color,"i love red color"):
    print("matched")
else:
    print("not matched")
color = r"red"
if re.findall(color,"i love red color"):
    print("matched")
else:
    print("not matched")
color = r"red"
text = r"i like red color"
match = re.search(color,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())