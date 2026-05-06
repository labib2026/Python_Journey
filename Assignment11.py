#task tuples
student_ids = (
    "rahim",
    "karim",
    "jabbar",
    "labib",
    "robin"
)

print(student_ids[2])
#task 2(set)
name = {"neko", "inu", "gakusei", "sensei", "kyuoshitsu", "inu", "neko"}
print(name)

#task 2 stack
website = []
website.append("dodi repack")
website.append("fitgirl repack")
website.append("gemini ai")
print(website)
website.pop()
print(website)
# queue
from collections import deque

food = deque(["burger","pizza","chese"])
food.popleft()
print(food)