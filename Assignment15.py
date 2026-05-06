#task 1
sensors = ["Brake", "Engine", "Fuel"]
status = ["Critical", "Stable", "Low"]

car = zip(sensors,status)
result = list(filter(lambda x: x[1] != "Stable" ,car))
print(result)
# task 2
def fun(base,exp):
    if exp == 0:
        return 1
    else:
        return base ** exp
print(fun(5,5))
# task3
words = ["taberu", "iku", "nomu"]
jp = {x : len(x) for x in words}
print(jp)