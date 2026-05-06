#task1 
i = 1
while i <=20:
    if i == 10:
        break
    i = i + 1
    if i == 5:
        continue
    print(i)
#task 2
n = float(input("Enter the last term : "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)
#task3
subject = ["mtkclient", "ghidra", "python", "nmap", "metasploit"]
print(subject[-1])
subject = subject + ["burpsuite"]
subject.pop(1) 
print(subject)

