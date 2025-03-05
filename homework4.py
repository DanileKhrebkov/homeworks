class Device:
    def __init__(self, voltage, cost):
        self.voltage = voltage
        self.cost = cost
    
    def show_info(self):
        print(f'Вольтаж устройства: {self.voltage}, Текущая цена: {self.cost}')
    def change_cost(self):
        new_cost = int(input('Введите новую цену: '))
        self.cost = new_cost
    

class CoffeeMachine(Device):
    def __init__(self, voltage, cost):
        super().__init__(voltage, cost)
    def show_info(self):
        print(f'Вольтаж кофемашины: {self.voltage}, Текущая цена: {self.cost}')
    def change_cost(self):
        new_cost = int(input('Введите новую цену кофемашины: '))
        self.cost = new_cost

class Blender(Device):
    def __init__(self, voltage, cost):
        super().__init__(voltage, cost)
    def show_info(self):
        print(f'Вольтаж Блендера: {self.voltage}, Текущая цена: {self.cost}')
    def change_cost(self):
        new_cost = int(input('Введите новую цену Блендера: '))
        self.cost = new_cost

class MeatGrinder(Device):
    def __init__(self, voltage, cost):
        super().__init__(voltage, cost)
    def show_info(self):
        print(f'Вольтаж Мясорубки: {self.voltage}, Текущая цена: {self.cost}')
    def change_cost(self):
        new_cost = int(input('Введите новую цену мясорубки: '))
        self.cost = new_cost






coffee_machine = CoffeeMachine(220, 15000)
coffee_machine.show_info()
coffee_machine.change_cost()
coffee_machine.show_info()

meat_grinder = MeatGrinder(380, 39950)
meat_grinder.show_info()