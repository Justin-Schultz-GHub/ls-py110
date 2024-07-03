'''
Commented out at the bottom is my first attempt at solving the problem.
Unfortunately, I wasn't sure how to make it work using a dictionary. I asked
ChatGPT for a hint and it suggested using tuples instead of a dictionary, and
using sorted() with a custom key function. This led to my solution below. Good
practice with custom keys, since I haven't actually implemented them before.
Additionally, the use of -tuples[1] in the custom key function to get a
descending order was new.

Update: After comparing with the LS implementation, it seems that my code uses a
lot more memory. Interestingly, I ran into the same problem when writing my code
that LS used to demonstrate debugging.
'''

def sort_by_consonant_count(string_list):
    tuple_list = []
    new_string_list = []

    def adjacent_consonant_count(string):
        adjacent_counter = 0

        string = string.replace(" ", "")
        adjacent_string = ""

        for letter in string:
            if letter not in "aeiou":
                adjacent_string += letter
                if len(adjacent_string) > adjacent_counter:
                    adjacent_counter = len(adjacent_string)
            elif letter in "aeiou":
                if len(adjacent_string) > adjacent_counter:
                    adjacent_counter = len(adjacent_string)

                adjacent_string = ""

        if adjacent_counter == 1:
            adjacent_counter = 0

        return adjacent_counter

    for s in string_list:
        count = adjacent_consonant_count(s)
        tuple_list.append((s, count))

    def get_tuple_object(tuples):
        return -tuples[1]

    sorted_tuple_list = sorted(tuple_list, key=get_tuple_object)

    for i in range(len(sorted_tuple_list)):
        new_string_list.append(sorted_tuple_list[i][0])

    return new_string_list

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list) == ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa'])


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# def sort_by_consonant_count(string_list):
#     adjacent_consonant_dict = {
#     }

#     new_string_list = []

#     def adjacent_consonant_count(string):
#         adjacent_counter = 0

#         string = string.replace(" ", "")
#         adjacent_string = ""

#         for letter in string:
#             if letter not in "aeiou":
#                 adjacent_string += letter
#                 if len(adjacent_string) > adjacent_counter:
#                     adjacent_counter = len(adjacent_string)
#             elif letter in "aeiou":
#                 if len(adjacent_string) > adjacent_counter:
#                     adjacent_counter = len(adjacent_string)
#                     adjacent_string = ""

#                 else:
#                     adjacent_string = ""

#         if adjacent_counter == 1:
#             adjacent_counter -= 1
#             return adjacent_counter

#         return adjacent_counter


#     for i in range(len(string_list)):
#         adjacent_consonant_dict[string_list[i]] = adjacent_consonant_count(string_list[i])

#     print(adjacent_consonant_dict)

#     new_string_list = list(adjacent_consonant_dict)

#     return new_string_list