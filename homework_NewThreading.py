import threading
import random

def fill_list(numbers, size, event):
    numbers.extend([random.randint(1, 100) for _ in range(size)])
    event.set()  # Сигнализируем, что список заполнен

def calculate_sum(numbers, event, result):
    event.wait()  # Ждем сигнала
    result['sum'] = sum(numbers)

def calculate_average(numbers, event, result):
    event.wait()  # Ждем сигнала
    result['average'] = sum(numbers) / len(numbers) if numbers else 0

numbers = []
result = {}
event = threading.Event()
size = 10

thread1 = threading.Thread(target=fill_list, args=(numbers, size, event))
thread2 = threading.Thread(target=calculate_sum, args=(numbers, event, result))
thread3 = threading.Thread(target=calculate_average, args=(numbers, event, result))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("Список:", numbers)
print("Сумма:", result['sum'])
print("Среднее:", result['average'])