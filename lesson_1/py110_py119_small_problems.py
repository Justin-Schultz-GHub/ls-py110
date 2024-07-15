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

# # Letter Swap
# # https://launchschool.com/exercises/81a9b8ef
# def swap(string):
#     word_list = string.split()
#     swapped_list = []
#     temp_string = ""

#     for word in word_list:
#         if len(word) > 2:
#             temp_string += word[-1]
#             for i in range(len(word) - 1):
#                 if i > 0:
#                     temp_string += word[i]

#             temp_string += word[0]
#             swapped_list.append(temp_string)
#             temp_string = ""

#         elif len(word) == 1:
#             swapped_list.append(word)

#         else:
#             temp_string += word[-1]
#             temp_string += word[0]
#             swapped_list.append(temp_string)
#             temp_string = ""

#     new_string = ' '.join(swapped_list)
#     return new_string

# print(swap('Oh what a wonderful day it is')
#       == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True

# # Convert a String to a Number
# # https://launchschool.com/exercises/097dfb47?track=python
# def string_to_integer(string):
#     integer_value = 0
#     place_value = 1
#     multiply_value = 0

#     for char in reversed(string):
#         match char:
#             case '0':
#                 multiply_value = 0
#             case '1':
#                 multiply_value = 1
#             case '2':
#                 multiply_value = 2
#             case '3':
#                 multiply_value = 3
#             case '4':
#                 multiply_value = 4
#             case '5':
#                 multiply_value = 5
#             case '6':
#                 multiply_value = 6
#             case '7':
#                 multiply_value = 7
#             case '8':
#                 multiply_value = 8
#             case '9':
#                 multiply_value = 9

#         integer_value += multiply_value * place_value
#         place_value *= 10

#     return integer_value

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True

# # Convert a String to a Signed Number
# # https://launchschool.com/exercises/2de3afe3?track=python
# def string_to_signed_integer(string):
#     string_list = list(string)

#     DIGITS = {
#         '0': 0,
#         '1': 1,
#         '2': 2,
#         '3': 3,
#         '4': 4,
#         '5': 5,
#         '6': 6,
#         '7': 7,
#         '8': 8,
#         '9': 9,
#     }

#     value = 0

#     if string_list[0] == "+":
#         string_list.remove("+")

#         for char in string_list:
#             value = (10 * value) + DIGITS[char]

#         return value

#     elif string_list[0] == "-":
#         string_list.remove("-")

#         for char in string_list:
#             value = (10 * value) + DIGITS[char]

#         value *= -1

#         return value

#     else:
#         for char in string_list:
#             value = (10 * value) + DIGITS[char]

#         return value

# print(string_to_signed_integer("4321") == 4321)  # True
# print(string_to_signed_integer("-570") == -570)  # True
# print(string_to_signed_integer("+100") == 100)   # True

# # Convert a Number to a String
# # https://launchschool.com/exercises/6134db97?track=python
# def integer_to_string(number):
#     if number == 0:
#         return "0"

#     multiplier = 10
#     i = 1
#     current_value = 0
#     new_list = []

#     DIGITS = {
#         1: "1",
#         2: "2",
#         3: "3",
#         4: "4",
#         5: "5",
#         6: "6",
#         7: "7",
#         8: "8",
#         9: "9",
#         0: "0",

#     }

#     while True:
#         current_value = divmod(number, multiplier)[1]

#         if current_value < (1 * i):
#             new_list.append(DIGITS[0])
#         elif current_value < (2 * i):
#             new_list.append(DIGITS[1])
#         elif current_value < (3 * i):
#             new_list.append(DIGITS[2])
#         elif current_value < (4 * i):
#             new_list.append(DIGITS[3])
#         elif current_value < (5 * i):
#             new_list.append(DIGITS[4])
#         elif current_value < (6 * i):
#             new_list.append(DIGITS[5])
#         elif current_value < (7 * i):
#             new_list.append(DIGITS[6])
#         elif current_value < (8 * i):
#             new_list.append(DIGITS[7])
#         elif current_value < (9 * i):
#             new_list.append(DIGITS[8])
#         elif current_value >= (9 * i):
#             new_list.append(DIGITS[9])

#         if current_value == number:
#             break

#         multiplier *= 10
#         i *= 10

#     new_list = new_list[::-1]
#     number_string = ''.join(new_list)

#     return number_string

# # print(integer_to_string(0) == "0")                    # True
# # print(integer_to_string(4921) == "4921")              # True
# # print(integer_to_string(5000) == "5000")              # True
# # print(integer_to_string(1234567890) == "1234567890")  # True

# # Convert a Signed Number to a String
# # https://launchschool.com/exercises/634f48e3?track=python
# # Requires the above function to work
# def signed_integer_to_string(number):
#     if number > 0:
#         positive = "+"
#         string = integer_to_string(number)
#         positive_string = positive + string

#         return positive_string

#     elif number < 0:
#         negative = "-"
#         string = integer_to_string(number * -1)
#         negative_string = negative + string

#         return negative_string

#     else:
#         return integer_to_string(number)

# print(signed_integer_to_string(4321) == "+4321")  # True
# print(signed_integer_to_string(-123) == "-123")   # True
# print(signed_integer_to_string(0) == "0")         # True

# Cute Angles
# https://launchschool.com/exercises/3292ee85?track=python
DEGREES = "\u00B0"
MINUTES = "'"
SECONDS = '"'

def dms(number):
    number_list = str(number).split(".")

    if len(number_list) == 1:
        return f'{number_list[0] + DEGREES + "00" + MINUTES + "00" + SECONDS}'

    else:
        degrees_value = str(number_list[0])

        if number_list[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            minutes_value = str(60 * int(number_list[1]) // 10 - 1)
            seconds_value = "59"

        else:
            minutes_value = str(60 * float("." + number_list[1]))

            if float(minutes_value) < 10:
                minutes_value = "0" + str(minutes_value)
                minutes_list = str(minutes_value).split(".")

            else:
                minutes_list = str(minutes_value).split(".")

            if minutes_list[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                minutes_value = minutes_list[0]
                seconds_value = str(int(60 * float("." + minutes_list[1])))

            else:
                minutes_value = minutes_list[0]
                print(minutes_list[1])
                seconds_value = str(60 * float("." + minutes_list[1]))
                if int(float(seconds_value)) < 10:
                    seconds_value = "0" + str(int(float(seconds_value)))

        return f'{degrees_value}{DEGREES}{minutes_value}{MINUTES}{seconds_value}{SECONDS}'

# All of these examples should print True
print(dms(93.034773) == "93°02'05\"")
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")