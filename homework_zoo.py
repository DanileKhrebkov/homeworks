class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.__age = age  
        self.die = False  

    
    def get_age(self):
        return self.__age

    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Возраст должен быть положительным числом.")

    
    def make_sound(self):
        print(f"{self.name} издает звук.")

    
    def display_info(self):
        print(f"Имя: {self.name}, Вид: {self.species}, Возраст: {self.__age}")


class Mammal(Animal):
    def __init__(self, name, species, age, fur_color):
        super().__init__(name, species, age)
        self.fur_color = fur_color  

    
    def make_sound(self):
        print(f"{self.name} (млекопитающее) рычит.")


class Bird(Animal):
    def __init__(self, name, species, age, wing_span):
        super().__init__(name, species, age)
        self.wing_span = wing_span  

    
    def make_sound(self):
        print(f"{self.name} (птица) поет.")


class ZooEmployee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    
    def feed_animal(self, animal):
        print(f"{self.name} ({self.position}) кормит {animal.name}.")


class Visitor:
    def __init__(self, name, ticket_number):
        self.name = name
        self.ticket_number = ticket_number

    
    def watch_animal(self, animal):
        print(f"{self.name} (билет №{self.ticket_number}) наблюдает за {animal.name}.")


# Ввод данных
lion = Mammal("Симба", "Лев", 5, "золотистый")
eagle = Bird("Орел", "Орел", 3, 2.0)


employee = ZooEmployee("Иван", "Смотритель")


visitor = Visitor("Анна", 123)


lion.display_info()
lion.make_sound()

eagle.display_info()
eagle.make_sound()

employee.feed_animal(lion)
visitor.watch_animal(eagle)

# Геттер и сеттер
print(f"Возраст льва: {lion.get_age()}")
lion.set_age(6)
print(f"Новый возраст льва: {lion.get_age()}")