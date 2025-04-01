class Stack:
    def __init__(self, data_type):
        self.data_type = data_type
        self.items = []
    
    def push(self, item):
        if not isinstance(item, self.data_type):
            raise TypeError(f"Неверный тип данных для стека. Ожидается {self.data_type}, получен {type(item)}")
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0



if __name__ == "__main__":
    print("Тестирование стека для целых чисел (int)")
    int_stack = Stack(int)
    print("Стек пуст?", int_stack.is_empty())  # True
    
    int_stack.push(10)
    int_stack.push(20)
    int_stack.push(30)
    

    print("Верхний элемент:", int_stack.peek())  # 30

    print("Извлеченный элемент:", int_stack.pop())  # 30
    print("Извлеченный элемент:", int_stack.pop())  # 20
    

    print("Стек пуст?", int_stack.is_empty())  
    

    try:
        int_stack.push("строка")  
    except TypeError as e:
        print("Ошибка:", e)  
    

    int_stack.pop()  
    try:
        int_stack.pop()  
    except IndexError as e:
        print("Ошибка:", e)  
    
    print("\nТестирование стека для строк (str)")
    str_stack = Stack(str)
    
    str_stack.push("hello")
    str_stack.push("world")
    
    print("Верхний элемент:", str_stack.peek())  
    print("Извлеченный элемент:", str_stack.pop()) 
    print("Извлеченный элемент:", str_stack.pop()) 
    

    print("\nТестирование стека для чисел с плавающей точкой (float)")
    float_stack = Stack(float)
    
    float_stack.push(3.14)
    float_stack.push(2.71)
    
    try:
        float_stack.push(100)  
        print("Целое число 100 было добавлено в стек float")
    except TypeError as e:
        print("Ошибка:", e)
    
    print("Верхний элемент:", float_stack.peek())

#Прогуглил про __name__ == '__main__', удобная вещь оказывается