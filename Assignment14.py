#task 1
name = ["Alice","Bob"]
score = [85,90]
print(list(zip(name,score)))
#task 2
def fact(n):
    if n == 1:
        return 1
    else:
       return n * fact(n-1)
print(fact(5))