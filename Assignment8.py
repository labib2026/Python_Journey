# task 1 

num = list(range(5,50,5))
for x in num:
    print(x)

# task 2 
number = [10,20,30,40,50]
sum = 0 
for x in number:
    sum = sum + x
print(sum)# fixed1
# task 3
files = ["boot.bin", "recovery.img", "system.df", "vender.img", "userdata.img"]
for x in files:
    if x == "system.df": #fixed 2
        break
print("System file detected! Scanning paused.")
