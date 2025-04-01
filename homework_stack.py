class Stack:
    def __init__(self):
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0
    

    def push(self, item):
        self.__stack.append(item)
        print(f"{item} is added")


    def pop(self):
        if not self.is_empty():
            popped_item = self.__stack.pop()
            print(f"Удален: {popped_item}")
        else:
            print(" is empty")
            return None
        
    
    def check_last(self):
        if not self.is_empty():
            return self.__stack[-1]
        else:
            print(" is empty")
            return None
        
    def size(self):
        return len(self.__stack)
    
    def display(self):
        print(f"Selected stack: {self.__stack}")

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(4)
my_stack.push(3)
my_stack.pop()
my_stack.is_empty()
my_stack.check_last()
print("//////////////////////////////////////////")
my_stack.display()