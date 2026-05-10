#task 1
class vehicle:
    def massage(self):
        print("I am a vehicle")
    def bus(vehicle):
        pass
m1 = vehicle()
m1.massage()
# task 2
class car():
    def  start(self):
        print("Key turn and start")
class ElectricCar(car):
    def start(self):
        print("Push button and start (Silent)")
m2 = ElectricCar()
m2.start()
#task 3
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


