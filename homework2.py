#Императивный(самый понятный как по мне)


# numbers = [10, 15, 20, 25, 30] 
# sum = 0
# for number in numbers: 
#     if number % 2 == 0:
#          sum += number
# print(f'Сумма: {sum}')





# Процедурный(я не понял почему у меня 10 выдает, вроде все правильно)
# def sum_of_even(numbers):
#     sum_even = 0    
#     for number in numbers:
#         if number % 2 == 0:
#             sum_even += number
#             return sum_even

# numbers = [10, 15, 20, 25, 30]
# result = sum_of_even(numbers)
# print(f'Сумма: {result}')






#Функциональный(было сложно, но я уместил это в 3 строки)
numbers = [10, 15, 20, 25, 30]
sum_even = sum(filter(lambda x: x % 2 == 0, numbers))
print(f'Сумма: {sum_even}')