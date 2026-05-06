#Task 1
try:
        file = input("Enter your file name : ")
        content = open(file, "r")
        content.read()
        print("File founded")
except FileNotFoundError:
        print("file not found")
finally:
        print("Operation Finished.")
#task 2
file = open("number.txt","r")
text = file.read().split(",") 
new = list(map(lambda x : int(x)+10 ,text ))
print(new)
file.close()
#task 3
try:
        jp_dict ={
                "Taberu": "Tabete",
                "Nomu": "Nonde",
                "Iku": "Itte",
                "Matsu": "Matte",
                "Yomu": "Yonde"
        }
        user = input("Enter your JP verd : ").capitalize()
        result = jp_dict[user]
        print(f"The Te-form is: {result}")
except:
        print("Verb not found in our N5 database!")


