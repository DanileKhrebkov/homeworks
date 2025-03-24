from dataclasses import dataclass

@dataclass
class Vehicle:
    __year: int
    __model: str
    __brand: str
    __mileage: int

class Car(Vehicle):
    def __init__(self, bodytype):
        self.__bodytype = bodytype
    
class Truck(Vehicle):
    def __init__(self, veight):
        self.__veight = veight
        