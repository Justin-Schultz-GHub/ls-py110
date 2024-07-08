# PP 1
# fruits = ("apple", "banana", "cherry", "date", "banana")

# def count_bananas(fruit_tuple):
#     banana_counter = fruit_tuple.count("banana")

#     return banana_counter

# print(count_bananas(fruits))

# PP 2
# numbers = {1, 2, 3, 4, 5, 5, 4, 3}
# print(len(numbers))
# print(numbers) # ?

# PP 3
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# def unique_integer_set(set_a, set_b):
#     # Mutating
#     # set_a.update(set_b)

#     # return set_a

#     # Non-mutating
#     # unique_set = set_a.union(set_b)
#     # or
#     unique_set = set_a | set_b

#     return unique_set

# print(unique_integer_set(a, b))
# print(a)
# print(b)

# PP 4
# names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
# name_positions = {}
# for index, name in enumerate(names):
#     name_positions[name] = index
# print(name_positions) # ?

# PP 5
# ages = {
#     "Herman": 32,
#     "Lily": 30,
#     "Grandpa": 5843,
#     "Eddie": 10,
#     "Marilyn": 22,
#     "Spot": 237,
# }

# total_age = 0

# for name, age in ages.items():
#     total_age += age

# or

# total_age = sum(ages.values())

# print(total_age)

# PP 6
# print(min(ages.values()))

# words = ['ant', 'bear', 'cat']
# selected_words = []
# for word in words:
#     if len(word) > 3:
#         selected_words.append(word)

# print(selected_words) # ?

# PP 7
# words = ['ant', 'bear', 'cat']
# selected_words = []
# for word in words:
#     if len(word) > 3:
#         selected_words.append(word)

# print(selected_words) # ?

# PP 8
# statement = "The Flintstones Rock"

# my_dict = {
# }

# for letter in statement:
#     if letter.isalpha():
#         my_dict[letter] = statement.count(letter)

# print(my_dict == {
#     'T': 1,
#     'h': 1,
#     'e': 2,
#     'F': 1,
#     'l': 1,
#     'i': 1,
#     'n': 2,
#     't': 2,
#     's': 2,
#     'o': 2,
#     'R': 1,
#     'c': 1,
#     'k': 1
# })

# PP 9
# [num for num in [1, 2, 3] if num > 1] # ?

# PP 10
# dictionary = {'a': 'ant', 'b': 'bear'}
# print(dictionary.popitem()) # ?

# PP 11
# lst = [1, 2, 3, 4, 5]
# lst[:2] # ?

# PP 12
# frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6)
# print(frozen) # ?