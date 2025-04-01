class Queue:

    def __init__(self):
        self.__Queue = []

    def is_empty(self):
        return len(self.__Queue) == 0
    

    def push(self, item):
        self.__Queue.append(item)
        print(f"{item} is added")


    def pop(self):
        if not self.is_empty():
            popped_item = self.__Queue.pop()
            print(f"Удален: {popped_item}")
        else:
            print(" is empty")
            return None


    def check_last(self):
        if not self.is_empty():
            return self.__Queue[0]
        else:
            print(" is empty")
            return None

    def size(self):
        return len(self.__Queue)

    def display(self):
        print(f"Selected queue: {self.__Queue}")

my_queue = Queue()
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)
my_queue.push(4)
my_queue.pop()
my_queue.pop()
print(my_queue.size())
my_queue.check_last()
print("//////////////////////////////////////////")
my_queue.display()
