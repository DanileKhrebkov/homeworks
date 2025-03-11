class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color


    def display_info(self):
        print(f"Автомобиль: {self.brand} {self.model} ({self.year}), цвет: {self.color}")



# 3 представителя Car
car1 = Car("Toyota", "Camry", 2020, "черный")
car2 = Car("BMW", "X5", 2019, "белый")
car3 = Car("Audi", "A4", 2021, "синий")

# Вывод инфы
car1.display_info()
car2.display_info()
car3.display_info()