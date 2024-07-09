# # Searching 101
# # https://launchschool.com/exercises/a1c4fed5?track=python
# numbers_list = []

# def get_numbers():
#     user_integer = input(f'Enter number {int(len(numbers_list)) + 1}: ')

#     while not valid_num(user_integer):
#         user_integer = input('Please enter a valid number: ')

#     user_integer = int(user_integer)

#     numbers_list.append(user_integer)

# def valid_num(number):
#     if number.isdigit():
#         return True

#     return False

# while len(numbers_list) < 5:
#     get_numbers()

# sixth_number = input('Enter number 6: ')

# while not valid_num(sixth_number):
#     sixth_number = input('Please enter a valid number: ')

# sixth_number = int(sixth_number)

# if sixth_number in numbers_list:
#     print(f'{sixth_number} is in the first 5 numbers')
# else:
#     print(f'{sixth_number} is not in the first 5 numbers')

# # Palindromic Strings (Part 1)
# # https://launchschool.com/exercises/407bf4aa?track=python
# def is_palindrome():
#     input_string = input('Please enter palindrome check text: ')
#     character_list = []
#     [character_list.append(character) for character in input_string]

#     reverse_list = character_list[::-1]

#     return reverse_list == character_list

# print(is_palindrome() == True)

# # Palindromic Strings (Part 2)
# # https://launchschool.com/exercises/4f333858?track=python
# def is_real_palindrome(string):
#     new_string = ''.join([character.lower() for character in string if
#         character.isalpha() is True or character.isdigit() is True])

#     reverse_string = new_string[::-1]

#     return new_string == reverse_string

# print(is_real_palindrome('madam') is True)           # True
# print(is_real_palindrome('356653') is True)          # True
# print(is_real_palindrome('356635') is False)         # True
# print(is_real_palindrome('356a653') is True)         # True
# print(is_real_palindrome('123ab321') is False)       # True

# # # # case doesn't matter
# print(is_real_palindrome('Madam') is True)           # True

# # # only alphanumerics matter
# print(is_real_palindrome("Madam, I'm Adam") is True) # True

# # Running Totals
# # https://launchschool.com/exercises/8e9d667a?track=python
# def running_total(numbers):
#     running_total_list = []
#     running_count = 0

#     for i in range(len(numbers)):
#         running_count += numbers[i]
#         running_total_list.append(running_count)

#     return running_total_list

# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

# # Letter Counter (Part 1)
# # https://launchschool.com/exercises/094a11fe
# def word_sizes(words):
#     word_size_dictionary = {}

#     if len(words) > 0:
#         word_list = words.split(" ")

#         for word in word_list:
#             word_length = int(len(word))
#             if word_length in word_size_dictionary:
#                 word_size_dictionary[word_length] += 1
#             else:
#                 word_size_dictionary[word_length] = 1

#     return word_size_dictionary

# # All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# string = 'Humpty Dumpty sat on a wall'
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# print(word_sizes('') == {})

# # Letter Counter (Part 2)
# # https://launchschool.com/exercises/0871b97b
# def word_sizes(words):
#     word_size_dictionary = {}
#     clean_word_list = []
#     temp_string = ""

#     if len(words) > 0:
#         word_list = words.split()

#         for word in word_list:
#             for character in word:
#                 if character.isalpha():
#                     temp_string += character

#             clean_word_list.append(temp_string)
#             temp_string = ""

#         for word in clean_word_list:
#             word_length = int(len(word))
#             if word_length in word_size_dictionary:
#                 word_size_dictionary[word_length] += 1
#             else:
#                 word_size_dictionary[word_length] = 1

#     return word_size_dictionary

# # All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})

# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

# print(word_sizes('') == {})

# Letter Swap
# https://launchschool.com/exercises/81a9b8ef
def swap(string):
    word_list = string.split()
    swapped_list = []
    temp_string = ""

    for word in word_list:
        if len(word) > 2:
            temp_string += word[-1]
            for i in range(len(word) - 1):
                if i > 0:
                    temp_string += word[i]

            temp_string += word[0]
            swapped_list.append(temp_string)
            temp_string = ""

        elif len(word) == 1:
            swapped_list.append(word)

        else:
            temp_string += word[-1]
            temp_string += word[0]
            swapped_list.append(temp_string)
            temp_string = ""

    new_string = ' '.join(swapped_list)
    return new_string

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True