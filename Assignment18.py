#task 1
class Engine:
    type = ""
    horsepower = ""

    def __init__(self, type,horsepower):
        self.type = type 
        self.horsepower = horsepower
    def start_engine(self):
        print(F"{self.type} engine with {self.horsepower} HP is starting... Vroom Vroom!")
my_car = Engine("V8",500)
my_car.start_engine()

#task 2
class trip:
    distance = ""
    fuel_unit = ""
    def __init__(self,distance,fuel_unit):
        self.distance = distance
        self.fuel_unit = fuel_unit
    def total(self):
        total = self.distance / self.fuel_unit
        print ("Total cost = ",total)
calculation = trip(5,3)
calculation.total()
# task 3
class student():
    name = ""
    id = ""

    def __init__(self,name,id):
        self.name= name
        if type(id) == int:
            self.id = id
        else:
            self.id = "Invalid ID"
            print(f"Warning: ID for {self.name} must be a number!")

    def intro(self):
        print(f"This is {self.name} with ID {self.id}")

student1 = student("Labib", 400)
student1.intro()
student2 = student("Asir", "Labib123")
student2.intro()