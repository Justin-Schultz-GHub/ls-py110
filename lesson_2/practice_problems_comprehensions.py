# Practice Problem 1
# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }

# # total_age = 0

# # for person, info in munsters.items():
# #     if info['gender'] == 'male':
# #         total_age += info['age']

# # print(total_age)

# total_age = sum([value['age']
#             for key, value in munsters.items()
#             if value['gender'] == 'male'
#             ])

# print(total_age)

# Practice Problem 2
# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# lst = [sorted(item) for item in lst]
# print(lst)

# for i in range(len(lst)):
#     lst[i] = sorted(lst[i])

# print(lst)

# Expected result
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

# Practice Problem 3
# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# new_list = [sorted(item, key=str) for item in lst]

# print(new_list)

# # Expected result
# # [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

# Practice Problem 4
# lst = [
#     ['a', 1],
#     ['b', 'two'],
#     ['sea', {'c': 3}],
#     ['D', ['a', 'b', 'c']]
# ]

# new_dict = {key: value for key, value in lst}
# print(new_dict)

# # Expected result
# # {
# #     'a': 1,
# #     'b': 'two',
# #     'sea': {c: 3},
# #     'D': ['a', 'b', 'c']
# # }

# Practice Problem 5
# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

# def sum_of_odds(numbers):
#     total = 0

#     for num in numbers:
#         if num % 2 != 0:
#             total += num

#     return total

# sorted_list = sorted([item for item in lst], key=sum_of_odds)

# print(lst)
# print(sorted_list)

# Expected result
# [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

# Practice Problem 6
# lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# # Close but not quite. This returns a list with only a single dictionary
# # new_list = [{key: value + 1
# #             for element in lst
# #             for key, value in element.items()
# #             }]

# # Correct answer
# new_list = [{key: value + 1
#             for key, value in element.items()}
#             for element in lst
#             ]

# print(new_list)


# # Expected result
# # [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

# Practice Problem 7
# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# new_list = [[num for num in element if num % 3 == 0] for element in lst]

# print(new_list)

# Expected result
# [[], [3, 12], [9], [15, 18]]

# # Practice Problem 8
# dict1 = {
#     'grape': {
#         'type': 'fruit',
#         'colors': ['red', 'green'],
#         'size': 'small',
#     },
#     'carrot': {
#         'type': 'vegetable',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'apricot': {
#         'type': 'fruit',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'marrow': {
#         'type': 'vegetable',
#         'colors': ['green'],
#         'size': 'large',
#     },
# }

# # これ超めんどくさかった
# def transform_item(item):
#     if item['type'] == 'fruit':
#         return [color.capitalize() for color in item['colors']]
#     else:
#         return item['size'].upper()


# new_list = [transform_item(value)
#             for key, value in dict1.items()
#             ]

# print(new_list)

# # Expected result
# # [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

# # Practice Problem 9
# lst = [
#     {'a': [1, 2, 3]},
#     {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
#     {'e': [8], 'f': [6, 10]},
# ]

# # Why are the 'hard' ones always easy and the easier ones often hard?
# def even_dict(dictionary):
#     for sublist in list(dictionary):
#         for num in sublist:
#             if num % 2 != 0:
#                 return False

#     return True

# new_list = [dictionary
#             for dictionary in lst
#             if even_dict(dictionary.values())
#             ]

# print(new_list)

# expected_list = [{'e': [8], 'f': [6, 10]}]

# print(new_list == expected_list) # Should print True

# Practice Problem 10
# My solution. Probably uses more memory than the LS solution because I'm
# generating a random number with each iteration. Didn't know about
# random.choice(). Incidentally, if sections[0] and sections[-1] were the same
# integer, this wouldn't work.
# import random

# VALID_CHARACTERS = 'abcdef1234567890'

# def create_uuid():
#     uuid = ''
#     sections = [8, 4, 4, 4, 12]

#     for number in sections:
#         for _ in range(number):
#             random_int = random.randint(0, 15)
#             uuid += VALID_CHARACTERS[random_int]
#         if number is not sections[-1]:
#             uuid += '-'

#     return uuid

# print(create_uuid())

# Practice Problem 11
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

VOWELS = 'aeiou'

# # My first solution
# def determine_vowels(lst):
#     lst_vowels = ''

#     for word in lst:
#         for letter in word:
#             if letter in VOWELS:
#                 lst_vowels += letter

#     return lst_vowels

# list_of_vowels = [letter
#                 for verse in dict1.values()
#                 for letter in determine_vowels(verse)
#                 ]

# My second solution
list_of_vowels = [letter
                for lst in dict1.values()
                for word in lst
                for letter in word
                if letter in VOWELS
                ]

# list_of_vowels = [letter
#                 for key in dict1
#                 for word in dict1[key]
#                 for letter in word
#                 if letter in VOWELS
#                 ]


expected_list = ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
print(list_of_vowels)
print(list_of_vowels == expected_list)