# numbers = [1, 2, 3, 4]

# numbers = [num + 1 for num in numbers]

# print(numbers)

# dict1 = {
#     'apple': 'Produce',
#     'carrot': 'Produce',
#     'pear': 'Produce',
#     'broccoli': 'Produce',
# }

# dict1['apple'] = 'Fruit'
# dict1['carrot'] = 'Vegetable'
# dict1['pear'] = 'Fruit'
# dict1['broccoli'] = 'Vegetable'

# print(dict1)


# numbers = [61, 103, 525, 103, 25, 103]

# numbers_str = ' '.join(str(num) for num in numbers)
# print(numbers_str)

# numbers_str = numbers_str.replace('103', '102')
# print(numbers_str)

# numbers = [int(num) for num in numbers_str.split()]
# print(numbers)


# shades = ('crimson', 'emerald', 'azure')
# r, g, b = shades
# # r
# # 'crimson'

# # g
# # 'emerald'

# # b
# # 'azure'

# print(*shades)
# print(r)
# print(g)
# print(b)

# fruits_list = ["apple", "banana", "cherry"]
# fruits_tuple = tuple(fruits_list)
# # fruits_tuple
# # ('apple', 'banana', 'cherry')

# list(fruits_tuple)
# # ['apple', 'banana', 'cherry']

# data = {'apple': 5, 'banana': 3, 'cherry': 8}
# print(list(data.items()))
# # ['apple', 'banana', 'cherry']
# key_types = [type(key) for key, value in data.items()]
# value_types = [type(value) for key, value in data.items()]
# print(key_types)
# print(value_types)

# print(tuple(data.keys()))
# # ('apple', 'banana', 'cherry')

# fruits = ["apple", "banana", "cherry"]

# for index, fruit in enumerate(fruits):
#     print(f"Index {index} has fruit: {fruit}")

# # Index 0 has fruit: apple
# # Index 1 has fruit: banana
# # Index 2 has fruit: cherry

# colors = ("red", "green", "blue")

# for index, color in enumerate(colors):
#     print(f"Color at index {index} is {color}")
#     print(f"Item at index {index} is type {type(color)}")

# # Color at index 0 is red
# # Color at index 1 is green
# # Color at index 2 is blue

# my_list = [3, 2, 2, 1, 4, 4, 4]
# my_set = set(my_list)
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())

# # {1, 2, 3, 4}

# The Python visualizer seems to make a temporary dictionary object when using
# the double unary operator. Not sure if this is actually what's happening
# though.

def print_person_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# Example usage:
person_info = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland",
    "occupation": "Adventurer",
}

# Additional information
additional_info = {
    "hobby": "Reading",
    "pets": ["White Rabbit", "Cheshire Cat"],
}

# Update person_info dictionary
person_info.update(additional_info)

# Print updated details
print_person_details(**person_info)

