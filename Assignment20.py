#task 1 (Multiple Inheritance (The Hybrid Tech))
class Mechanical:
    def engine_info(self):
        print("This is a mechanical engine.")
class Electronics:
    def battery_info(self):
        print("This is an electronic battery.")
class HybridCar(Mechanical, Electronics):
    def car_info(self):
        print("This is a hybrid car.")
c1 = HybridCar()
c1.car_info()
c1.engine_info()
c1.battery_info()
#task 2 (Abstraction (The Security Blueprint))
from abc import ABC,abstractmethod

class DeviceSecurity(ABC):
      @abstractmethod
      def check_vulnerability(self):
          pass

class MobileSecurity(DeviceSecurity):
      def scanning_bugs(self):
          print("Scanning MTK chipset for bugs...")

      def check_vulnerability(self): # eituku parsilam na claude code e thke override kore niyechi
          print("Running vulnerability scan on mobile device.")
          self.scanning_bugs()

m1 = MobileSecurity()
m1.scanning_bugs()
# task 3 (Polymorphism (The Universal Method))

def perform_move(vehicle):
      vehicle.move()
class Car:
      def move(self):
          print("Driving on 4 wheels")

class Bike:
      def move(self):
          print("Riding on 2 wheels")
car1 = Car()
bike1 = Bike()
perform_move(car1) # ami ekhane bujhini amake pore bujhiye dibe eita auto correction
perform_move(bike1)
