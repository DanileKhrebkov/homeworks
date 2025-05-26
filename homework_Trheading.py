import threading
import random
import time


warehouse = {
    "ноутбуки": 100,
    "телефоны": 150,
    "наушники": 200,
    "мониторы": 50,
    "клавиатуры": 120,
    "мыши": 180
}


lock = threading.Lock()

def add_item(stock, item_name, quantity):
    with lock:
        stock[item_name] += quantity
        print(f"Добавлено {quantity} единиц товара '{item_name}'. Текущее количество: {stock[item_name]}")

def remove_item(stock, item_name, quantity):
    with lock:
        if stock[item_name] >= quantity:
            stock[item_name] -= quantity
            print(f"Отгружено {quantity} единиц товара '{item_name}'. Текущее количество: {stock[item_name]}")
        else:
            print(f"Недостаточно товара '{item_name}' для отгрузки {quantity} единиц. Доступно: {stock[item_name]}")

def warehouse_worker(stock, operations_count):
    items = list(stock.keys())
    
    for _ in range(operations_count):

        item = random.choice(items)
        operation = random.choice(["add", "remove"])
        quantity = random.randint(1, 10)
        
        if operation == "add":
            add_item(stock, item, quantity)
        else:
            remove_item(stock, item, quantity)
        

        time.sleep(random.uniform(0.1, 0.3))

def main():
    print("Начальное состояние склада:")
    for item, quantity in warehouse.items():
        print(f"{item}: {quantity}")
    print("\nНачинаем работу...\n")
    

    threads = []
    num_threads = random.randint(5, 10)  
    operations_per_thread = random.randint(20, 50) 
    for i in range(num_threads):
        thread = threading.Thread(
            target=warehouse_worker,
            args=(warehouse, operations_per_thread),
            name=f"Worker-{i+1}"
        )
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    

    print("\nРабота всех потоков завершена.")
    print("\nИтоговое состояние склада:")
    for item, quantity in warehouse.items():
        print(f"{item}: {quantity}")

if __name__ == "__main__":
    main()