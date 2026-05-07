# task 1
class car:
    name = ""
    engine = ""
display_info = car()
display_info.name = "Toyota"
display_info.engine = "V4"
print(f"This is {display_info.name} with a {display_info.engine} engine.")


class car:
    name = ""
    engine = ""
    
    def display_info(self):
        print(f"This is {self.name} with a {self.engine} engine.")

obj = car()
obj.name = "Toyota"
obj.engine = "V4"
obj.display_info() 