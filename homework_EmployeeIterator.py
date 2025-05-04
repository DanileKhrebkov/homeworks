from abc import ABC, abstractmethod
from typing import List, Dict

class Employee:
    def __init__(self, name: str, position: str, department: str):
        self.name = name
        self.position = position
        self.department = department
        self.received_messages = []
    
    def receive_message(self, message: str):
        self.received_messages.append(message)
    
    def __str__(self):
        return f"{self.name} ({self.position}, {self.department})"

class EmployeeIterator:
    def __init__(self, employees: List[Employee]):
        self._employees = employees
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._employees):
            employee = self._employees[self._index]
            self._index += 1
            return employee
        raise StopIteration

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee: Employee):
        self.employees.append(employee)
    
    def __iter__(self):
        return EmployeeIterator(self.employees)

class Mediator(ABC):
    @abstractmethod
    def send_message(self, sender: Employee, receiver_name: str, message: str):
        pass

class DepartmentMediator(Mediator):
    def __init__(self):
        self.departments = {}
    
    def add_department(self, department: Department):
        self.departments[department.name] = department
    
    def send_message(self, sender: Employee, receiver_name: str, message: str):
        for department in self.departments.values():
            for employee in department:
                if employee.name == receiver_name:
                    employee.receive_message(f"От {sender.name}: {message}")
                    return
        print(f"Сотрудник {receiver_name} не найден")

if __name__ == "__main__":
    it_department = Department("IT")
    hr_department = Department("HR")

    employees = [
        Employee("Иван Петров", "Разработчик", "IT"),
        Employee("Мария Сидорова", "Тестировщик", "IT"),
        Employee("Алексей Иванов", "HR-менеджер", "HR"),
        Employee("Елена Смирнова", "Рекрутер", "HR")
    ]

    for emp in employees:
        if emp.department == "IT":
            it_department.add_employee(emp)
        else:
            hr_department.add_employee(emp)

    mediator = DepartmentMediator()
    mediator.add_department(it_department)
    mediator.add_department(hr_department)

    print("Сотрудники IT отдела:")
    for employee in it_department:
        print(employee)

    print("\nСотрудники HR отдела:")
    for employee in hr_department:
        print(employee)

    mediator.send_message(employees[0], "Алексей Иванов", "Нужно нанять нового разработчика")
    mediator.send_message(employees[2], "Иван Петров", "Ваше резюме получено")

    print("\nСообщения Алексея Иванова:")
    for msg in employees[2].received_messages:
        print(msg)

    print("\nСообщения Ивана Петрова:")
    for msg in employees[0].received_messages:
        print(msg)