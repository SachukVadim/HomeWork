# 
# class Iterator:
#     def __init__(self, object:list):
#         self.list = object
# 
#     def __iter__(self):
#         self.index = 0
#         return self
# 
#     def __next__(self):
#         if self.index == len(self.list):
#             raise StopIteration()
# 
#         result1 = self.index
#         result2 = self.list[self.index]
#         self.index += 1
#         return (result1, result2)
# 
# list = [1,2,3,4,5,67,8,76,5,4,678,7,6,5]
# for idx,value in Iterator(list):
#     print(f"{idx} - {value} ")

# import time
# import random
# 
# # Function to generate a random string without using the string module
# def generate_random_string_no_string_fixed(length):
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     result = ''.join(letters[random.randint(0, len(letters) - 1)] for _ in range(length))
#     return result
# 
# # Function to generate a list of random strings
# def generate_list_of_random_strings_no_string_fixed(count, min_length, max_length):
#     return [generate_random_string_no_string_fixed(random.randint(min_length, max_length)) for _ in range(count)]
# 
# # Start measuring time
# start_time_fixed = time.time()
# 
# # Generate the list
# random_strings_fixed = generate_list_of_random_strings_no_string_fixed(10000, 3, 8)
# 
# # Stop measuring time
# end_time_fixed = time.time()
# 
# execution_time_fixed = end_time_fixed - start_time_fixed
# 
# execution_time_fixed
# print(random_strings_fixed)
# print(end_time_fixed)

# import os
# import random
#
# PATH = os.path.dirname(os.path.abspath(__file__))
# litter = "abcdefg"
#
# with open(os.path.join(PATH, "RandomNun.txt"), "w") as f:
#     for _ in range(10000):
#         f.write(random.choice(litter))
#
# with open(os.path.join(PATH, "RandomNun.txt"), "r") as f:
#     content = f.read()
#     print(content[0])
#     print(content[-1])

import os


PATH = os.path.dirname(os.path.abspath(__file__))

def save_func():
    with open(os.path.join(PATH, "RandomNun.txt"), "a") as f:
        f.write(f"{num1},{num2},{result},")

try:
    with open(os.path.join(PATH, "RandomNun.txt"), "r") as f:
        my_list = f.read().split(",")
except:
    my_list = []

while True:
    print("Оберіть дію : 1 - '+', 2 - '-', 3 - '*', 4 - '/', 9 - 'Подивитись історію' 0 - 'Вихід' ")
    user_input = int(input("дія: "))
    if user_input == 9:
        print("Попередня історія:")
        with open(os.path.join(PATH, "RandomNun.txt"), "r") as file:
            print(file.read())

    elif user_input == 0:
        print("До зустрічі!")
        break
    num1 = int(input("Введить перше число: "))
    num2 = int(input("Введить друге число: ")) 
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
        save_func()
    elif user_input == 2:
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
        save_func()
    elif user_input == 3:
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
        save_func()
    elif user_input == 4:
        if num2 == 0:
            print("Неможливо знайти частну ділянку з нуля.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
            save_func()
    else:
        print("Неправильний вибір дії.")
