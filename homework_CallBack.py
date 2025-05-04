def apply_callback(callback):
    def decorator(func):
        def wrapper(lst):
            processed_list = [callback(item) for item in lst]
            return func(processed_list)
        return wrapper
    return decorator

def multiply_by_two(x):
    return x * 2

def add_ten(x):
    return x + 10

def to_string(x):
    return str(x)

@apply_callback(multiply_by_two)
def process_numbers(lst):
    print("Обработанный список:", lst)

@apply_callback(add_ten)
def process_numbers_add(lst):
    print("Обработанный список (+10):", lst)

@apply_callback(to_string)
def process_numbers_str(lst):
    print("Обработанный список (строки):", lst)

process_numbers([1, 2, 3, 4])
process_numbers_add([1, 2, 3, 4])
process_numbers_str([1, 2, 3, 4])