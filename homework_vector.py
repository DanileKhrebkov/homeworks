import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"
    


# Пример Создания с проверкой файла:
if __name__ == "__main__":
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

# Примеры перегрузок
    v3 = v1 + v2
    print(f"Сложение: {v1} + {v2} = {v3}")


    v4 = v1 - v2
    print(f"Вычитание: {v1} - {v2} = {v4}")


    scalar = 2
    v5 = v1 * scalar
    print(f"Умножение на скаляр: {v1} * {scalar} = {v5}")


    print(f"Сравнение: {v1} == {v2} -> {v1 == v2}")


    print(f"Длина вектора {v1}: {v1.magnitude()}")