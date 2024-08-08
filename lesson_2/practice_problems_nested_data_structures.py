# lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]

# lst2 = [
#     {
#         'first': ['a', 'b', 'c'],
#         'second': ['d', 'e', 'f']
#     },
#     {
#         'third': ['g', 'h', 'i']
#     }
# ]

# lst3 = [['abc'], ['def'], {'third': ['ghi']}]

# dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

# # This one is much more challenging than it looks! Try it, but don't
# # stress about it. If you don't solve it in 10 minutes, you can look
# # at the answer.
# dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}

# print(lst1[2][1][3])
# print(lst2[1]['third'][0])
# print(lst3[2]['third'][0][0])
# print(dict1['b'][1])
# print(list(dict2['3rd'].keys())[0])

# lst1 = [1, [2, 3], 4]
# lst1[1][1] = 4

# lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
# lst2[2] = 4

# dict1 = {'first': [1, 2, [3]]}
# dict1['first'][2][0] = 4

# dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
# dict2['a']['a'][2] = 4

# print(lst1)
# print(lst2)
# print(dict1)
# print(dict2)

# a = 2
# b = [5, 8]
# lst = [a, b]
# # [2, [5, 8]]

# lst[0] += 2
# # [4, [5, 8]]
# print(lst)


# lst[1][0] -= a
# # [4, [3, 8]]
# print(lst)


# print(a)
# print(b)

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for name, details in munsters.items():
    print(f'{name} is a {details["age"]}-year-old {details["gender"]}.')