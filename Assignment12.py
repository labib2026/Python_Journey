#task 1  Square & Multiply (Return Concept):
def add(a):
    sum = a*a
    return sum
result = add(5)
print(result * 2)
print(result)
#task2 The Power Function (Basic Function):
def pow(base,exp):
    sum = base ** exp
    print(sum)
pow(90,7)
# task 3 Super Adder (xargs Concept):
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num 
    print(sum) 

add(10, 20)
add(1, 2, 3, 4)
