# # Searching 101
# # https://launchschool.com/exercises/a1c4fed5
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
# # https://launchschool.com/exercises/407bf4aa
# def is_palindrome():
#     input_string = input('Please enter palindrome check text: ')
#     character_list = []
#     [character_list.append(character) for character in input_string]

#     reverse_list = character_list[::-1]

#     return reverse_list == character_list

# print(is_palindrome() == True)

# # Palindromic Strings (Part 2)
# # https://launchschool.com/exercises/4f333858
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
# # https://launchschool.com/exercises/8e9d667a
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
# # https://launchschool.com/exercises/097dfb47
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
# # https://launchschool.com/exercises/2de3afe3
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
# # https://launchschool.com/exercises/6134db97
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
# # https://launchschool.com/exercises/634f48e3
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

# # Cute Angles
# # https://launchschool.com/exercises/3292ee85
# DEGREES = "\u00B0"
# MINUTES = "'"
# SECONDS = '"'

# def dms(number):
#     while number < 0:
#         number += 360

#     while number > 360:
#         number -= 360

#     number_list = str(number).split(".")

#     if len(number_list) == 1:
#         return f'{number_list[0]}{DEGREES}00{MINUTES}00{SECONDS}'

#     else:
#         degrees_value = str(number_list[0])

#         if number_list[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
#             minutes_value = str(60 * int(number_list[1]) // 10 - 1)
#             seconds_value = "59"

#         else:
#             minutes_value = str(60 * float("." + number_list[1]))

#             if float(minutes_value) < 10:
#                 minutes_value = "0" + str(minutes_value)
#                 minutes_list = str(minutes_value).split(".")

#             else:
#                 minutes_list = str(minutes_value).split(".")

#             if minutes_list[1] in [
#                                 "1", "2", "3", "4",
#                                 "5", "6", "7", "8", "9"
#                                 ]:
#                 minutes_value = minutes_list[0]
#                 seconds_value = str(int(60 * float("." + minutes_list[1])))

#             else:
#                 minutes_value = minutes_list[0]
#                 print(minutes_list[1])
#                 seconds_value = str(60 * float("." + minutes_list[1]))
#                 if int(float(seconds_value)) < 10:
#                     seconds_value = "0" + str(int(float(seconds_value)))

#         return (
#                 f'{degrees_value}'
#                 f'{DEGREES}'
#                 f'{minutes_value}'
#                 f'{MINUTES}'
#                 f'{seconds_value}'
#                 f'{SECONDS}'
#                 )

# # All of these examples should print True
# print(dms(93.034773) == "93°02'05\"")
# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
# # Further exploration
# print(dms(-1) == "359°00'00\"")
# print(dms(400) == "40°00'00\"")
# print(dms(-40) == "320°00'00\"")
# print(dms(-420) == "300°00'00\"")

# # Combining Lists
# # https://launchschool.com/exercises/9db45ac4
# def union(list1, list2):
#     return set(list1) | set(list2)

# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

# # Halvsies
# # https://launchschool.com/exercises/6c0ff432

# def halvsies(numbers):
#     numbers_length = len(numbers)
#     return_list = []

#     if numbers_length % 2 == 1:
#         half = (numbers_length // 2 + 1)
#         return_list.append(numbers[0:half])
#         return_list.append(numbers[half::])

#     else:
#         half = numbers_length // 2
#         return_list.append(numbers[0:half])
#         return_list.append(numbers[half::])

#     return return_list

# # All of these examples should print True
# print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
# print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
# print(halvsies([5]) == [[5], []])
# print(halvsies([]) == [[], []])

# # Find the Duplicate
# # https://launchschool.com/exercises/b024fd71
# def find_dup(numbers):
#     number_dict = {}

#     for num in numbers:
#         if num in number_dict:
#             number_dict[num] += 1
#         else:
#             number_dict[num] = 1

#     for key, value in number_dict.items():
#         if value == 2:
#             return key

# print(find_dup([1, 5, 3, 1]) == 1) # True

# print(find_dup([
#                   18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
#                   38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
#                   14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
#                   78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
#                   89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
#                   41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
#                   55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
#                   85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
#                   40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
#                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
#               ]) == 73)       # True

# # Combine Two Lists
# # https://launchschool.com/exercises/513e4379
# def interleave(list1, list2):
#     combined_list = []

#     # for i in range(len(list1)):
#     #     combined_list.append(list1[i])
#     #     combined_list.append(list2[i])

#     # return combined_list
#     for item in zip(list1, list2):
#         combined_list += [*item]

#     return combined_list

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# expected = [1, "a", 2, "b", 3, "c"]
# print(interleave(list1, list2) == expected)      # True

# # Multiplicative Average
# # https://launchschool.com/exercises/f7b9d1a1
# def multiplicative_average(numbers):
#     product = 1

#     for number in numbers:
#         product *= number

#     quotient = product / len(numbers)

#     string_value = f'{quotient:.3f}'

#     # string_value = pad_zeroes(string_value)

#     return string_value

# # All of these examples should print True
# print(multiplicative_average([3, 5]) == "7.500")
# print(multiplicative_average([2, 5, 8]) == "26.667")
# print(multiplicative_average([2, 5]) == "5.000")
# print(multiplicative_average([1, 1, 1, 1]) == "0.250")
# print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

# # Multiply Lists
# # https://launchschool.com/exercises/fc642f09
# def multiply_lists(list1, list2):
#     product_list = []
#     product = 0

#     # for i in range(len(list1)):
#     #     product_list.append(list1[i] * list2[i])

#     # return product_list

#     return [num1 * num2 for num1, num2 in zip(list1, list2)]

# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_lists(list1, list2) == [27, 50, 77])  # True

# # List of Digits
# # https://launchschool.com/exercises/1c3a7301
# def digit_list(number):
#     number_string = str(number)
#     number_list = []

#     return [int(number_string[i]) for i in range(len(number_string))]

# print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
# print(digit_list(7) == [7])                       # True
# print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
# print(digit_list(444) == [4, 4, 4])               # True

# # How Many?
# # https://launchschool.com/exercises/6051b11c
# def count_occurrences(vehicles):
#     # comment out the following line for non-case sensitive version
#     vehicles = [vehicle.casefold() for vehicle in vehicles]
#     vehicle_dictionary = {}

#     for vehicle in vehicles:
#         if vehicle not in vehicle_dictionary:
#             vehicle_dictionary[vehicle] = 1
#         else:
#             vehicle_dictionary[vehicle] += 1

#     print_occurrences(vehicle_dictionary)

# def print_occurrences(vehicle_dictionary):
#     for vehicle, count in vehicle_dictionary.items():
#         print(f'{vehicle}: {count}')

# vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
#             'motorcycle', 'motorcycle', 'car', 'truck', 'suv']

# count_occurrences(vehicles)

# # List Average
# # https://launchschool.com/exercises/d6505dcf
# def average(numbers):
#     print(sum(numbers) // len(numbers))

# print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
# print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
# print(average([7]) == 7)                          # True

# # After Midnight (Part 1)
# # https://launchschool.com/exercises/86822507
# def time_of_day(number):
#     if number >= 0:
#         hours_and_minutes = {'hours': 0,
#                             'minutes': 0,

#         }

#         while number >= 60:
#             number -= 60
#             if hours_and_minutes['hours'] >= 24:
#                 hours_and_minutes['hours'] = 0

#             hours_and_minutes['hours'] += 1

#         hours_and_minutes['minutes'] += number

#     if number < 0:
#         hours_and_minutes = {'hours': 23,
#                             'minutes': 60,

#         }

#         while number <= -60:
#             number += 60
#             if hours_and_minutes['hours'] <= 0:
#                 hours_and_minutes['hours'] = 24

#             hours_and_minutes['hours'] -= 1

#         if hours_and_minutes['hours'] == 24:
#             hours_and_minutes['hours'] = 0
#             hours_and_minutes['minutes'] = 60

#         hours_and_minutes['minutes'] += number

#     hours = pad_zeroes(hours_and_minutes['hours'])
#     minutes = pad_zeroes(hours_and_minutes['minutes'])

#     return f'{hours}:{minutes}'

# def pad_zeroes(number):
#     if number < 10:
#         number_string = "0" + str(number)
#     else:
#         number_string = str(number)

#     return number_string

# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True

# # After Midnight (Part 2)
# # https://launchschool.com/exercises/44718e8c
# HOURS_PER_DAY = 24
# MINUTES_PER_HOUR = 60
# MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

# def after_midnight(time):
#     number = ((int(time[:2]) * MINUTES_PER_HOUR) + int(time[3:])) % MINUTES_PER_DAY

#     return number

# def before_midnight(time):
#     number = (MINUTES_PER_DAY - after_midnight(time)) % MINUTES_PER_DAY

#     return number

# print(after_midnight("00:00") == 0)     # True
# print(before_midnight("00:00") == 0)    # True
# print(after_midnight("12:34") == 754)   # True
# print(before_midnight("12:34") == 686)  # True
# print(after_midnight("24:00") == 0)     # True
# print(before_midnight("24:00") == 0)    # True

# # Double Char (Part 1)
# # https://launchschool.com/exercises/2797f3e7
# def repeater(string):
#     doubled = ''

#     for character in string:
#         doubled += character * 2

#     # return "".join([character * 2 for character in string])

#     return doubled



# print(repeater('Hello') == "HHeelllloo")              # True
# print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
# print(repeater('') == "")                             # True

# # Double Char (Part 2)
# # https://launchschool.com/exercises/157bb2c4
# CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

# def double_consonants(string):
#     new_string = ''

#     for character in string:
#         if character.lower() in CONSONANTS:
#             new_string += character * 2
#         else:
#             new_string += character

#     return new_string

# # All of these examples should print True
# print(double_consonants('String') == "SSttrrinngg")
# print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
# print(double_consonants('July 4th') == "JJullyy 4tthh")
# print(double_consonants('') == "")

# # Reverse Number
# # https://launchschool.com/exercises/eee9cc52
# def reverse_number(number):
#     digit_list = int(str(number)[::-1])

#     return digit_list

# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True

# # Counting Up
# # https://launchschool.com/exercises/d08b9889
# def sequence(number):
#     number_list = []

#     for num in range(1, number + 1):
#         number_list.append(num)

#     return number_list
#     # return list(range(1, number + 1))

# print(sequence(5) == [1, 2, 3, 4, 5])   # True
# print(sequence(3) == [1, 2, 3])         # True
# print(sequence(1) == [1])               # True

# # Name Swapping
# # https://launchschool.com/exercises/e744aa30
# def swap_name(full_name):
#     return ', '.join(full_name.split()[::-1])

# print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# # Sequence Count
# # https://launchschool.com/exercises/35e0285a
# def sequence(count, start_value):
#     # step_value = start_value
#     # number_list = []

#     # while count > 0:
#     #     number_list.append(start_value)
#     #     start_value += step_value
#     #     count -= 1

#     # return number_list

#     return [start_value * num for num in range(1, count + 1)]

# print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
# print(sequence(4, -7) == [-7, -14, -21, -28])     # True
# print(sequence(3, 0) == [0, 0, 0])                # True
# print(sequence(0, 1000000) == [])                 # True

# # Reversed Lists
# # https://launchschool.com/exercises/a598aef9
# def reverse_list(input_list):
#     new_list = []

#     while len(input_list) > 0:
#         new_list.append(input_list.pop())

#     for element in new_list:
#         input_list.append(element)

#     return input_list

# list1 = [1, 2, 3, 4]
# result = reverse_list(list1)
# print(result == [4, 3, 2, 1])               # True
# print(list1 is result)                      # True

# list2 = ["a", "b", "c", "d", "e"]
# result2 = reverse_list(list2)
# print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
# print(list2 is result2)                     # True

# list3 = ["abc"]
# result3 = reverse_list(list3)
# print(result3 == ['abc'])                   # True
# print(list3 is result3)                     # True

# list4 = []
# result4 = reverse_list(list4)
# print(result4 == [])                        # True
# print(list4 is result4)                     # True

# # Matching Parenthesis?
# # https://launchschool.com/exercises/9e90e4a5
# def is_balanced(string):
#     # parenthese_counter = {
#     #     'left': 0,
#     #     'right': 0,
#     # }

#     # for char in string:
#     #     if char == '(':
#     #         parenthese_counter['left'] += 1
#     #     elif char == ')':
#     #         parenthese_counter['right'] += 1

#     #         if parenthese_counter['right'] > parenthese_counter['left']:
#     #             return False

#     # return parenthese_counter['left'] == parenthese_counter['right']
#     parenthese_counter = {
#         'left_paren': 0,
#         'right_paren': 0,
#         'left_bracket': 0,
#         'right_bracket': 0,
#         'left_brace': 0,
#         'right_brace': 0,
#         'single_quotes': 0,
#         'double_quotes': 0,
#     }

#     for char in string:
#         match char:
#             case '(':
#                 parenthese_counter['left_paren'] += 1
#             case '[':
#                 parenthese_counter['left_bracket'] += 1
#             case '{':
#                 parenthese_counter['left_brace'] += 1
#             case '\'':
#                 parenthese_counter['single_quotes'] += 1
#             case '\"':
#                 parenthese_counter['double_quotes'] += 1

#             case ')':
#                 parenthese_counter['right_paren'] += 1
#                 if parenthese_counter['right_paren'] > parenthese_counter['left_paren']:
#                     return False
#             case ']':
#                 parenthese_counter['right_bracket'] += 1
#                 if parenthese_counter['right_bracket'] > parenthese_counter['left_bracket']:
#                     return False
#             case '}':
#                 parenthese_counter['right_brace'] += 1
#                 if parenthese_counter['right_brace'] > parenthese_counter['left_brace']:
#                     return False

#     return ((parenthese_counter['left_paren'] == parenthese_counter['right_paren'])
#         and (parenthese_counter['left_bracket'] == parenthese_counter['right_bracket'])
#         and (parenthese_counter['left_brace'] == parenthese_counter['right_brace'])
#         and (parenthese_counter['single_quotes'] % 2 == 0)
#         and (parenthese_counter['double_quotes'] % 2 == 0))


# # print(is_balanced("What (is) this?") == True)        # True
# # print(is_balanced("What is) this?") == False)        # True
# # print(is_balanced("What (is this?") == False)        # True
# # print(is_balanced("((What) (is this))?") == True)    # True
# # print(is_balanced("((What)) (is this))?") == False)  # True
# # print(is_balanced("Hey!") == True)                   # True
# # print(is_balanced(")Hey!(") == False)                # True
# # print(is_balanced("What ((is))) up(") == False)      # True

# print(is_balanced("{}") == True)
# print(is_balanced("[]") == True)
# print(is_balanced("()") == True)
# print(is_balanced("{[({})]}") == True)
# print(is_balanced("\"{[('')]}\"") == True)
# print(is_balanced("Hello [Python] (asdf).") == True)
# print(is_balanced("{[()stacks]} are {kool[()]}") == True)
# print(is_balanced("{[}]") == True)
# print(is_balanced("({[})") == False)
# print(is_balanced("][") == False)

# # Alphabetical Numbers
# # https://launchschool.com/exercises/eaf97eee
# def alphabetic_number_sort(number_list):
#     my_list = sorted([(0, "zero"), (1, "one"), (2, "two"), (3, "three"), (4, "four"),
#                 (5, "five"), (6, "six"), (7, "seven"), (8, "eight"), (9, "nine"),
#                 (10, "ten"), (11, "eleven"), (12, "twelve"), (13, "thirteen"),
#                 (14, "fourteen"), (15, "fifteen"), (16, "sixteen"),
#                 (17, "seventeen"), (18, "eighteen"), (19, "nineteen")],
#                 key=lambda number: number[1])

#     new_nums = []

#     for integer, word in my_list:
#         for num in number_list:
#             if num == integer:
#                 new_nums.append(num)

#     return new_nums

# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#               10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
#                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

# print(alphabetic_number_sort(input_list) == expected_result)
# # Prints True

# # Merge Sets
# # https://launchschool.com/exercises/f14b5d63
# def merge_sets(list1, list2):
#     set1 = convert_to_set(list1)
#     set2 = convert_to_set(list2)

#     merged_set = set1 | set2

#     return merged_set

# def convert_to_set(iterable):
#     return set(iterable)

# list1 = [3, 5, 7, 9]
# list2 = [5, 7, 11, 13]
# print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# # Prints True

# # Immutable Intersection
# # https://launchschool.com/exercises/af0ace37
# def intersection(list1, list2):
#     return frozenset(list1).intersection(frozenset(list2))

# list1 = [2, 4, 6, 8]
# list2 = [1, 3, 5, 7, 8]
# expected_result = frozenset({8})

# print(intersection(list1, list2) == expected_result) # True

# # Arrange a Dictionary
# # https://launchschool.com/exercises/8817379e
# def order_by_value(dictionary):
#     tuple_list = sorted(dictionary.items(), key=lambda item: item[1])

#     return [key for key, value in tuple_list]

# my_dict = {'p': 8, 'q': 2, 'r': 6}
# keys = ['q', 'r', 'p']
# print(order_by_value(my_dict) == keys)  # True

# # Unique Elements
# # https://launchschool.com/exercises/b00376c3
# def unique_from_first(list1, list2):
#     return set(list1).difference(set(list2))

# list1 = [3, 6, 9, 12]
# list2 = [6, 12, 15, 18]
# print(unique_from_first(list1, list2) == {9, 3})

# Leading Substrings
# https://launchschool.com/exercises/e01f3df2
# def leading_substrings(string):
#     substrings = []

#     for i in range(len(string)):
#         substrings.append(string[:i + 1])

#     return substrings

    # # Alternative solution with list comprehension
    # return [string[:i + 1] for i in range(len(string))]

# # All of these examples should print True
# print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# print(leading_substrings('a') == ['a'])
# print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

# # All Substrings
# # https://launchschool.com/exercises/39d24ce3
# # Requires the above function to work
# def substrings(string):
#     substrings_list = []

#     for i in range(len(string)):
#         sub_substrings = leading_substrings(string[i:])

#         for item in sub_substrings:
#             substrings_list.append(item)

#     return substrings_list

# expected_result = [
#     "a", "ab", "abc", "abcd", "abcde",
#     "b", "bc", "bcd", "bcde",
#     "c", "cd", "cde",
#     "d", "de",
#     "e",
# ]

# print(substrings('abcde') == expected_result)  # True

# # Palindromic Substrings
# # https://launchschool.com/exercises/bc977f27
# # Requires the above function to work
# def palindromes(string):
#     palindrome_list = []

#     for item in substrings(string):
#         if item == item[::-1] and len(item) > 1:
#             palindrome_list.append(item)

#     return palindrome_list

# print(palindromes('abcd') == [])                  # True
# print(palindromes('madam') == ['madam', 'ada'])   # True

# print(palindromes('hello-madam-did-madam-goodbye') ==
#                   [
#                       'll', '-madam-', '-madam-did-madam-',
#                       'madam', 'madam-did-madam', 'ada',
#                       'adam-did-mada', 'dam-did-mad',
#                       'am-did-ma', 'm-did-m', '-did-',
#                       'did', '-madam-', 'madam', 'ada', 'oo',
#                   ])    # True

# print(palindromes('knitting cassettes') ==
#                   [
#                       'nittin', 'itti', 'tt', 'ss',
#                       'settes', 'ette', 'tt',
#                   ])    # True

# # Inventory Item Transactions
# # https://launchschool.com/exercises/bbb4b01f
# def transactions_for(item_id, transaction_list):
#     return [transaction
#             for transaction in transaction_list
#             if transaction['id'] == item_id]


# transactions = [
#     {"id": 101, "movement": 'in',  "quantity":  5},
#     {"id": 105, "movement": 'in',  "quantity": 10},
#     {"id": 102, "movement": 'out', "quantity": 17},
#     {"id": 101, "movement": 'in',  "quantity": 12},
#     {"id": 103, "movement": 'out', "quantity": 20},
#     {"id": 102, "movement": 'out', "quantity": 15},
#     {"id": 105, "movement": 'in',  "quantity": 25},
#     {"id": 101, "movement": 'out', "quantity": 18},
#     {"id": 102, "movement": 'in',  "quantity": 22},
#     {"id": 103, "movement": 'out', "quantity": 15},
# ]

# print(transactions_for(101, transactions) ==
#       [
#           {"id": 101, "movement": "in",  "quantity":  5},
#           {"id": 101, "movement": "in",  "quantity": 12},
#           {"id": 101, "movement": "out", "quantity": 18},
#       ]) # True

# # Inventory Item Availability
# # https://launchschool.com/exercises/04b22878
# # Requires the above function to work
# def is_item_available(item_id, transaction_list):
#     inventory = 0
#     selected_transactions = transactions_for(item_id, transaction_list)

#     for transaction in selected_transactions:
#         if transaction['movement'] == 'in':
#             inventory += transaction['quantity']
#         else:
#             inventory -= transaction['quantity']

#     return inventory > 0

# transactions = [
#     {"id": 101, "movement": 'in',  "quantity":  5},
#     {"id": 105, "movement": 'in',  "quantity": 10},
#     {"id": 102, "movement": 'out', "quantity": 17},
#     {"id": 101, "movement": 'in',  "quantity": 12},
#     {"id": 103, "movement": 'out', "quantity": 20},
#     {"id": 102, "movement": 'out', "quantity": 15},
#     {"id": 105, "movement": 'in',  "quantity": 25},
#     {"id": 101, "movement": 'out', "quantity": 18},
#     {"id": 102, "movement": 'in',  "quantity": 22},
#     {"id": 103, "movement": 'out', "quantity": 15},
# ]

# print(is_item_available(101, transactions) == False)  # True
# print(is_item_available(103, transactions) == False)  # True
# print(is_item_available(105, transactions) == True)   # True

# # Inverting Dictionary
# # https://launchschool.com/exercises/90d18ae7
# def invert_dict(dictionary):
#     # temp_dict = dictionary.copy()

#     # dictionary.clear()

#     # for key, value in temp_dict.items():
#     #     dictionary[value] = key

#     # return dictionary

#     # Since I don't need to mutate the original dictionary
#     return {value: key for key, value in dictionary.items()}

# print(invert_dict({
#           'apple': 'fruit',
#           'broccoli': 'vegetable',
#           'salmon': 'fish',
#       }) == {
#           'fruit': 'apple',
#           'vegetable': 'broccoli',
#           'fish': 'salmon',
#       })  # True

# # Retain Specific Keys
# # https://launchschool.com/exercises/4b19afa8
# def keep_keys(dictionary, keys):
#     return {key: value for key, value in dictionary.items() if key in keys}

# input_dict = {
#     'red': 1,
#     'green': 2,
#     'blue': 3,
#     'yellow': 4,
# }

# keys = ['red', 'blue']
# expected_dict = {'red': 1, 'blue': 3}
# print(keep_keys(input_dict, keys) == expected_dict) # True

# # Delete Vowels
# # https://launchschool.com/exercises/bb9d55f5
# def remove_vowels(string_list):
#     VOWELS = 'aeiouAEIOU'
#     temp_string = ''

#     for i in range(len(string_list)):
#         for char in string_list[i]:
#             if char not in VOWELS:
#                 temp_string += char

#         string_list[i] = temp_string
#         temp_string = ''

#     return string_list

# # All of these examples should print True
# original = ['abcdefghijklmnopqrstuvwxyz']
# expected = ['bcdfghjklmnpqrstvwxyz']
# print(remove_vowels(original) == expected)        # True

# original = ['green', 'YELLOW', 'black', 'white']
# expected = ['grn', 'YLLW', 'blck', 'wht']
# print(remove_vowels(original) == expected)        # True

# original = ['ABC', 'AEIOU', 'XYZ']
# expected = ['BC', '', 'XYZ']
# print(remove_vowels(original) == expected)        # True

# # How Long Are You?
# # https://launchschool.com/exercises/74ff114b
# def word_lengths(string=''):
#     if string:
#         return [f'{word} {len(word)}' for word in string.split()]

#     return []

# # All of these examples should print True
# words = 'cow sheep chicken'
# expected_result = ['cow 3', 'sheep 5', 'chicken 7']
# print(word_lengths(words) == expected_result)        # True

# words = 'baseball hot dogs and apple pie'
# expected_result = ['baseball 8', 'hot 3', 'dogs 4',
#                   'and 3', 'apple 5', 'pie 3']
# print(word_lengths(words) == expected_result)        # True

# words = "It ain't easy, is it?"
# expected_result = ['It 2', "ain't 5", 'easy, 5',
#                   'is 2', 'it? 3']
# print(word_lengths(words) == expected_result)        # True

# big_word = 'Supercalifragilisticexpialidocious'
# print(word_lengths(big_word) == [f'{big_word} 34'])  # True

# print(word_lengths('') == [])                        # True
# print(word_lengths() == [])                          # True

# # List Element Multiplication
# # https://launchschool.com/exercises/827abcc2
# def multiply_items(list1, list2):
#     return [list1[i] * list2[i] for i in range(len(list1))]

# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

# # Sum of Sums
# # https://launchschool.com/exercises/8bee659d
# def sum_of_sums(numbers):
#     total_sum = 0

#     for i in range(len(numbers)):
#         total_sum += sum(numbers[:i + 1])

#     return total_sum

# print(sum_of_sums([3, 5, 2]) == 21)               # True
# # (3) + (3 + 5) + (3 + 5 + 2) --> 21

# print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

# print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

# print(sum_of_sums([4]) == 4)                      # True

# # Sum of Digits
# # https://launchschool.com/exercises/ae172c02
# def sum_digits(number):
#     return sum([int(char) for char in str(number)])

# print(sum_digits(23) == 5)              # True
# print(sum_digits(496) == 19)            # True
# print(sum_digits(123456789) == 45)      # True

# # Staggered Case (Part 1)
# # https://launchschool.com/exercises/5c5d7f1f
# def staggered_case(string):
#     string = string.lower()
#     staggered_string = ''

#     for i in range(len(string)):
#         if i % 2 == 0:
#             staggered_string += string[i].upper()
#         else:
#             staggered_string += string[i]

#     return staggered_string


# string = 'I Love Launch School!'
# result = "I LoVe lAuNcH ScHoOl!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_CaPs"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

# # Staggered Case (Part 2)
# # https://launchschool.com/exercises/bb605dc4
# def staggered_case(string):
#     string = string.lower()
#     staggered_string = ''
#     count = 0

#     for char in string:
#         if char.isalpha():
#             count += 1
#             staggered_string += char.lower() if count % 2 == 0 else char.upper()
#         else:
#             staggered_string += char

#     return staggered_string

# string = 'I Love Launch School!'
# result = "I lOvE lAuNcH sChOoL!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_cApS"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

# # Remove Consecutive Duplicates
# # https://launchschool.com/exercises/31152e2c
# def unique_sequence(numbers):
#     new_nums = []
#     previous_num = -1

#     for num in numbers:
#         if num != previous_num:
#             new_nums.append(num)
#             previous_num = num

#     return new_nums

#     # return [num
#     #         for idx, num in enumerate(numbers)
#     #         if idx == 0 or num != numbers[idx - 1]]

# original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
# expected = [1, 2, 6, 5, 3, 4]
# print(unique_sequence(original) == expected)      # True

# original = [1, 2, 1, 6, 6, 5, 6, 5, 3, 3, 3, 4]
# expected = [1, 2, 1, 6, 5, 6, 5, 3, 4]
# print(unique_sequence(original) == expected)      # True

# # Countdown
# # https://launchschool.com/exercises/267890f0
# def decrease(counter):
#     return counter - 1

# counter = 10

# for _ in range(10):
#     print(counter)
#     counter = decrease(counter)

# print('LAUNCH!')

# # Reverse a String
# # https://launchschool.com/exercises/418e1b23
# def reverse_string(string):
#     reversed_string = ''

#     for char in string[::-1]:
#         reversed_string += char

#     return reversed_string

# print(reverse_string("hello") == "olleh")

# # Multiply List
# # https://launchschool.com/exercises/f039d7ad
# def multiply_list(lst):
#     for i in range(len(lst)):
#         lst[i] *= 2

#     return lst

# print(multiply_list([1, 2, 3]) == [2, 4, 6])

# # Key Check
# # https://launchschool.com/exercises/b7b366ea
# def get_key_value(my_dict, key):
#     return key in my_dict

# print(get_key_value({"a": 1}, "b"))

# # Calendar Event Checker
# # https://launchschool.com/exercises/069c27d6
# events = {
#     "2023-08-13": ["Python debugging exercises"],
#     "2023-08-14": ["Read 'Automate the Boring Stuff'"],
#     "2023-08-15": ["Webinar: Python for Data Science"],
# }

# def is_date_available(date):
#     if date in events:
#         return False

#     return True

# print(is_date_available("2023-08-14"))  # should return False
# print(is_date_available("2023-08-16"))  # should return True

# # Mutable Default Arguments
# # https://launchschool.com/exercises/db5812ba
# def append_to_list(value, lst=None):
#     if lst == None:
#         lst = []

#     lst.append(value)
#     return lst

# print(append_to_list(1) == [1])
# print(append_to_list(2) == [2])

# # Shadow
# # https://launchschool.com/exercises/a79ce2b7
# def sum_of_numbers(numbers, factor):
#     return factor * sum(numbers)

# numbers = [1, 2, 3, 4]
# print(sum_of_numbers(numbers, 2) == 20)

# # Copy Issues
# # https://launchschool.com/exercises/385214e6
# import copy

# original = [[1], [2], [3]]
# copied = copy.deepcopy(original)

# original[0][0] = 99

# print(copied[0] == [1])

# # Set Modifications
# # https://launchschool.com/exercises/3c9bd095
# data_set = {1, 2, 3, 4, 5}

# for item in data_set:
#     data_set = {item for item in data_set if item % 2 != 0}

# print(data_set)

# # List Deduplication
# # https://launchschool.com/exercises/9c0dec0a
# data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# seen = set()
# unique_data = []

# for number in data:
#     if number not in seen:
#         unique_data.append(number)
#         seen.add(number)

# print(unique_data == [4, 2, 1, 3]) # order not guaranteed
# print(unique_data)

# # Rotation (Part 1)
# # https://launchschool.com/exercises/cb05fdb2
# import copy

# def rotate_list(something):
#     if isinstance(something, list):
#         if len(something) > 0:
#             rotated_list = something.copy()
#             rotated_list.append(rotated_list.pop(0))

#             return rotated_list

#         return []

#     return None

# # All of these examples should print True
# print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
# print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
# print(rotate_list(['a']) == ['a'])
# print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
# print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
# print(rotate_list([]) == [])

# # return `None` if the argument is not a list
# print(rotate_list(None) == None)
# print(rotate_list(1) == None)

# # the input list is not mutated
# lst = [1, 2, 3, 4]
# print(rotate_list(lst) == [2, 3, 4, 1])
# print(lst == [1, 2, 3, 4])

# # Rotation (Part 2)
# # https://launchschool.com/exercises/7c525401
# def rotate_rightmost_digits(number, idx):
#     number_list = list(str(number))
#     number_list.append(number_list.pop(-idx))

#     new_number = int(''.join(number_list))

#     return new_number

# print(rotate_rightmost_digits(735291, 2) == 735219)  # True
# print(rotate_rightmost_digits(735291, 3) == 735912)  # True
# print(rotate_rightmost_digits(735291, 1) == 735291)  # True
# print(rotate_rightmost_digits(735291, 4) == 732915)  # True
# print(rotate_rightmost_digits(735291, 5) == 752913)  # True
# print(rotate_rightmost_digits(735291, 6) == 352917)  # True
# print(rotate_rightmost_digits(1200, 3) == 1002)      # True

# Rotation (Part 3)
# https://launchschool.com/exercises/89604c6e
# def max_rotation(number):
#     number_list = list(str(number))

#     for i in range(len(number_list)):
#         number_list.append(number_list.pop(i))

#     maximum_rotation = int(''.join(number_list))

#     return maximum_rotation

# #   alternative version
#     # number_list = list(str(number))

#     # for i in range(len(number_list), 1, -1):
#     #     number = rotate_rightmost_digits(number, i)

#     # return number


# print(max_rotation(735291) == 321579)          # True
# print(max_rotation(3) == 3)                    # True
# print(max_rotation(35) == 53)                  # True
# print(max_rotation(8703529146) == 7321609845)  # True

# # Note that the final sequence here is `015`. The leading
# # zero gets dropped, though, since we're working with
# # an integer.
# print(max_rotation(105) == 15)                 # True

# # Stack Machine Interpretation
# # https://launchschool.com/exercises/b09d93c8
# def minilang(string):
#     stack = []
#     register = 0

#     for element in string.split():
#         match element:
#             case 'PUSH':
#                 stack.append(register)
#             case 'POP':
#                 register = stack.pop()
#             case 'ADD':
#                 register += stack.pop()
#             case 'SUB':
#                 register -= stack.pop()
#             case 'MULT':
#                 register *= stack.pop()
#             case 'DIV':
#                 register //= stack.pop()
#             case 'REMAINDER':
#                 register %= stack.pop()
#             case 'PRINT':
#                 print(round(register))
#             case _:
#                 register = int(element)


# minilang('PRINT')
# # 0

# minilang('5 PUSH 3 MULT PRINT')
# # 15

# minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# # 5
# # 3
# # 8

# minilang('5 PUSH POP PRINT')
# # 5

# minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

# minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # 6

# minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# # 12

# minilang('-3 PUSH 5 SUB PRINT')
# # 8

# minilang('6 PUSH')
# # (nothing is printed)

# # Word to Digit
# # https://launchschool.com/exercises/69f60f05
# NUMBERS = {
#     'zero': '0',
#     'one': '1',
#     'two': '2',
#     'three': '3',
#     'four': '4',
#     'five': '5',
#     'six': '6',
#     'seven': '7',
#     'eight': '8',
#     'nine': '9',
# }

# def word_to_digit(string):
#     # new_string = ''

#     # for word in string.split():
#     #     if word in NUMBERS:
#     #         new_string += f' {NUMBERS[word]}'
#     #     else:
#     #         new_string += f' {word}'

#     # return new_string.lstrip()

#     # One-liner version
#     # return ' '.join([NUMBERS.get(word, word) for word in string.split()])

#     string_list = [NUMBERS.get(word, word) for word in string.split()]

#     for i in range(len(string_list)):
#         string_list[i] = NUMBERS.get(string_list[i][:-1], string_list[i][:-1]) + string_list[i][-1]

#     new_string = ' '.join(string_list)

#     if new_string[-1] not in '.!?':
#         new_string += '.'

#     return new_string

# # message = 'Please call me at five five five one two three four'
# # print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# # Should print True
# # Further exploration
# message = 'Please call me at five, five, five, one, two, three, four, next sunday at five o\'clock'
# print(word_to_digit(message) == 'Please call me at 5, 5, 5, 1, 2, 3, 4, next sunday at 5 o\'clock.')
# # Should print True

# # Is It Prime?
# # https://launchschool.com/exercises/9e3d8de3
# import math
# def is_prime(number):
#     # Only works for smaller numbers
#     # PRIMES = [2, 3, 5, 7]

#     # if number == 1:
#     #     return False

#     # if number not in PRIMES:
#     #     for prime in PRIMES:
#     #         if number % prime == 0:
#     #             return False

#     # return True

#     # Should work for all numbers
#     if number == 1:
#         return False

#     for divisor in range(2, int(math.sqrt(number)) + 1):
#         if number % divisor == 0:
#             return False

#     return True

# # print(is_prime(1) == False)              # True
# # print(is_prime(2) == True)               # True
# # print(is_prime(3) == True)               # True
# # print(is_prime(4) == False)              # True
# # print(is_prime(5) == True)               # True
# # print(is_prime(6) == False)              # True
# # print(is_prime(7) == True)               # True
# # print(is_prime(8) == False)              # True
# # print(is_prime(9) == False)              # True
# # print(is_prime(29) == True)             # True
# # print(is_prime(23) == True)              # True
# # print(is_prime(24) == False)             # True
# # print(is_prime(997) == True)             # True
# # print(is_prime(998) == False)            # True
# # print(is_prime(3_297_061) == True)       # True
# # print(is_prime(23_297_061) == False)     # True
# print(is_prime(999998727899999)) # Takes a bit

# # Fibonacci Numbers (Procedural)
# # https://launchschool.com/exercises/b5a6df28
# def fibonacci(number):
#     f1 = 1
#     f2 = 1
#     n = 0

#     if number > 2:
#         for _ in range(number - 2):
#             n = f1 + f2
#             f1 = f2
#             f2 = n

#         return n

#     return 1

# print(fibonacci(1) == 1)                  # True
# print(fibonacci(2) == 1)                  # True
# print(fibonacci(3) == 2)                  # True
# print(fibonacci(4) == 3)                  # True
# print(fibonacci(5) == 5)                  # True
# print(fibonacci(6) == 8)                  # True
# print(fibonacci(12) == 144)               # True
# print(fibonacci(20) == 6765)              # True
# print(fibonacci(50) == 12586269025)       # True
# print(fibonacci(75) == 2111485077978050)  # True

# # Fibonacci Numbers (Recursion)
# # https://launchschool.com/exercises/0d9afda9
# def fibonacci(number):
#     if number <= 2:
#         return 1

#     return fibonacci(number - 1) + fibonacci(number - 2)

# print(fibonacci(1) == 1)         # True
# print(fibonacci(2) == 1)         # True
# print(fibonacci(3) == 2)         # True
# print(fibonacci(4) == 3)         # True
# print(fibonacci(5) == 5)         # True
# print(fibonacci(6) == 8)         # True
# print(fibonacci(12) == 144)      # True
# print(fibonacci(20) == 6765)     # True


# # Fibonacci Numbers (Memoization)
# # https://launchschool.com/exercises/030ec9a5
# fibs = {}
# # # fibs_v1 = {
# # #     1: 1,
# # #     2: 1,
# # # }

# def fibonacci(number):
#     if number <= 2:
#         return 1

#     if number in fibs:
#         return fibs[number]

#     return fibonacci(number - 1) + fibonacci(number - 2)

#     # # First idea, but it wasn't recursive
#     # while number not in fibs_v1:
#     #     fibs_v1[len(fibs_v1) + 1] = fibs_v1[len(fibs_v1)] + fibs_v1[len(fibs_v1) - 1]

#     # return fibs_v1.get(number)


# print(fibonacci(1) == 1)         # True
# print(fibonacci(2) == 1)         # True
# print(fibonacci(3) == 2)         # True
# print(fibonacci(4) == 3)         # True
# print(fibonacci(5) == 5)         # True
# print(fibonacci(6) == 8)         # True
# print(fibonacci(12) == 144)      # True
# print(fibonacci(20) == 6765)     # True

# # Fibonacci Number Location By Length
# # https://launchschool.com/exercises/37bb9fc0
# import sys

# def find_fibonacci_index_by_length(length):
#     sys.set_int_max_str_digits(50_000)

#     f1 = 1
#     f2 = 1
#     n = 2
#     count = 2

#     while len(str(f2)) < length:
#         count += 1
#         n = f1 + f2
#         f1 = f2
#         f2 = n

#     return count

# # All of these examples should print True
# # The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
# print(find_fibonacci_index_by_length(2) == 7)
# print(find_fibonacci_index_by_length(3) == 12)
# print(find_fibonacci_index_by_length(10) == 45)
# print(find_fibonacci_index_by_length(16) == 74)
# print(find_fibonacci_index_by_length(100) == 476)
# print(find_fibonacci_index_by_length(1000) == 4782)

# # # Next example might take a little while on older systems
# print(find_fibonacci_index_by_length(10000) == 47847)

# # Lettercase Percentage Ratio
# # https://launchschool.com/exercises/5800a75a
# def letter_percentages(string):
#     percentage_dict = {}
#     str_length = len(string)
#     count_dict = {
#         'lowercase': 0,
#         'uppercase': 0,
#         'neither': 0,
#     }
#     for character in string:
#         if character.isalpha() and character == character.lower():
#             count_dict['lowercase'] += 1
#         elif character.isalpha() and character == character.upper():
#             count_dict['uppercase'] += 1
#         else:
#             count_dict['neither'] += 1

#     percentage_dict['lowercase'] = f'{(count_dict["lowercase"] / str_length) * 100:.2f}'
#     percentage_dict['uppercase'] = f'{(count_dict["uppercase"] / str_length) * 100:.2f}'
#     percentage_dict['neither'] = f'{(count_dict["neither"] / str_length) * 100:.2f}'

#     return percentage_dict

# expected_result = {
#     'lowercase': "50.00",
#     'uppercase': "10.00",
#     'neither': "40.00",
# }
# print(letter_percentages('abCdef 123') == expected_result)

# expected_result = {
#     'lowercase': "37.50",
#     'uppercase': "37.50",
#     'neither': "25.00",
# }
# print(letter_percentages('AbCd +Ef') == expected_result)

# expected_result = {
#     'lowercase': "0.00",
#     'uppercase': "0.00",
#     'neither': "100.00",
# }
# print(letter_percentages('123') == expected_result)

# # Triangle Sides
# # https://launchschool.com/exercises/2c5c3272
# def is_valid(side_list):
#     if sum(side_list[:2]) <= side_list[2]:
#         return False

#     return True

# def triangle(num1, num2, num3):
#     side_list = sorted([num1, num2, num3])

#     if is_valid(side_list):
#         triangle_set = set(side_list)

#         if len(triangle_set) == 3:
#             return 'scalene'
#         elif len(triangle_set) == 2:
#             return 'isosceles'

#         return 'equilateral'

#     return 'invalid'

# # first version
# # def triangle(num1, num2, num3):
# #     side_list = sorted([num1, num2, num3])

# #     if sum(side_list[:2]) <= side_list[2]:
# #         return 'invalid'

# #     triangle_set = set(side_list)

# #     if len(triangle_set) == 3:
# #         return 'scalene'
# #     elif len(triangle_set) == 2:
# #         return 'isosceles'
# #     else:
# #         return 'equilateral'

# print(triangle(3, 3, 3) == "equilateral")  # True
# print(triangle(3, 3, 1.5) == "isosceles")  # True
# print(triangle(3, 4, 5) == "scalene")      # True
# print(triangle(0, 3, 3) == "invalid")      # True
# print(triangle(3, 1, 1) == "invalid")      # True

# # Tri-Angles
# # https://launchschool.com/exercises/5fa18f7b
# def is_valid(angle_list):
#     for angle in angle_list:
#         if angle == 0:
#             return False

#     if sum(angle_list) == 180:
#         return True

#     return False

# def triangle(num1, num2, num3):
#     angle_list = [num1, num2, num3]

#     if is_valid(angle_list):
#         for angle in angle_list:
#             if angle == 90:
#                 return 'right'
#             elif angle > 90:
#                 return 'obtuse'

#         return 'acute'

#     return 'invalid'

# print(triangle(60, 70, 50) == "acute")      # True
# print(triangle(30, 90, 60) == "right")      # True
# print(triangle(120, 50, 10) == "obtuse")    # True
# print(triangle(0, 90, 90) == "invalid")     # True
# print(triangle(50, 50, 50) == "invalid")    # True

# # Unlucky Days
# # https://launchschool.com/exercises/2fb67370
# import datetime

# DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
#                 'Saturday', 'Sunday']
# THIRTEENTH = 13

# def friday_the_13ths(year):
#     counter = 0

#     for month in range(1, 13):
#         if DAYS_OF_WEEK[datetime.date(year, month, THIRTEENTH).weekday()] == 'Friday':
#             counter += 1

#     return counter

# print(friday_the_13ths(1986) == 1)      # True
# print(friday_the_13ths(2015) == 3)      # True
# print(friday_the_13ths(2017) == 2)      # True

# # Next Featured Number Higher than a Given Value
# # https://launchschool.com/exercises/07af1741
# MAX_FEATURED = 9876543201
# ERROR = "There is no possible number that fulfills those requirements."

# def next_featured(number):
#     featured_number = number + 1

#     while featured_number % 7 != 0:
#         featured_number = add_one(featured_number)

#     while not is_valid(featured_number):
#         featured_number = add_seven(featured_number)

#         if featured_number > MAX_FEATURED:
#             return ERROR

#     return featured_number

# def add_one(number):
#     return number + 1

# def add_seven(number):
#     return number + 7

# def is_valid(number):
#     if number % 2 == 0 or number % 7 != 0:
#         return False

#     num_list = list(str(number))

#     if len(num_list) != len(set(num_list)):
#         return False

#     return True

# print(next_featured(12) == 21)                  # True
# print(next_featured(20) == 21)                  # True
# print(next_featured(21) == 35)                  # True
# print(next_featured(997) == 1029)               # True
# print(next_featured(1029) == 1043)              # True
# print(next_featured(999999) == 1023547)         # True
# print(next_featured(999999987) == 1023456987)   # True
# print(next_featured(9876543186) == 9876543201)  # True
# print(next_featured(9876543200) == 9876543201)  # True
# print(next_featured(9876543201) == ERROR)       # True

# # Sum Square - Square Sum
# # https://launchschool.com/exercises/c5b25237
# def sum_square_difference(number):
#     square_sum = (sum(range(number + 1))) ** 2
#     sum_square = sum([i ** 2 for i in range(number + 1)])

#     return square_sum - sum_square

# print(sum_square_difference(3) == 22)          # True
# # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

# print(sum_square_difference(10) == 2640)       # True
# print(sum_square_difference(1) == 0)           # True
# print(sum_square_difference(100) == 25164150)  # True

# # Bubble Sort
# # https://launchschool.com/exercises/37f73d3a
# def bubble_sort(lst):
#     while True:
#         for idx in range(len(lst) - 1):
#             if lst[idx] > lst[idx + 1]:
#                 lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]

#         if is_sorted(lst):
#             break

# def is_sorted(lst):
#     for idx in range(len(lst) - 1):
#         if lst[idx + 1] < lst[idx]:
#             return False

#     return True

# lst1 = [5, 3]
# bubble_sort(lst1)
# print(lst1 == [3, 5])                   # True

# lst2 = [6, 2, 7, 1, 4]
# bubble_sort(lst2)
# print(lst2 == [1, 2, 4, 6, 7])          # True

# lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#         'Kim', 'Bonnie']
# bubble_sort(lst3)

# expected = ["Alice", "Bonnie", "Kim", "Pete",
#             "Rachel", "Sue", "Tyler"]
# print(lst3 == expected)                 # True

# # Transpose 3x3 Matrix
# # https://launchschool.com/exercises/8a772030
# def transpose(matrix):
#     new_matrix = [[], [], []]

#     for item in matrix:
#         for idx, value in enumerate(item):
#             new_matrix[idx].append(value)

#     return new_matrix

    # # one liner
    # return [[item[i] for item in matrix] for i in range(len(matrix))]

# matrix = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# new_matrix = transpose(matrix)

# print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
# print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

# # Transpose MxN Matrix
# # https://launchschool.com/exercises/b2831239
# def transpose(matrix):
    # new_matrix = []

    # for _ in range(len(matrix[0])):
    #     new_matrix.append([])

    # for item in matrix:
    #     for idx, value in enumerate(item):
    #         new_matrix[idx].append(value)

#     # return new_matrix
#     return [[item[i] for item in matrix] for i in range(len(matrix[0]))]

# # All of these examples should print True
# print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
# print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
# print(transpose([[1]]) == [[1]])

# matrix_3_by_5 = [
#     [1, 2, 3, 4, 5],
#     [4, 3, 2, 1, 0],
#     [3, 7, 8, 6, 2],
# ]
# expected_result = [
#     [1, 4, 3],
#     [2, 3, 7],
#     [3, 2, 8],
#     [4, 1, 6],
#     [5, 0, 2],
# ]

# print(transpose(matrix_3_by_5) == expected_result)


# matrix_5_by_3 = [
#     [1, 4, 3],
#     [2, 3, 7],
#     [3, 2, 8],
#     [4, 1, 6],
#     [5, 0, 2],
# ]
# expected_result = [
#     [1, 2, 3, 4, 5],
#     [4, 3, 2, 1, 0],
#     [3, 7, 8, 6, 2],
# ]

# print(transpose(matrix_5_by_3) == expected_result)

# # Rotating Matrices
# # https://launchschool.com/exercises/564614de
# def rotate90(matrix):
#     new_matrix = []

#     for _ in range(len(matrix[0])):
#         new_matrix.append([])

#     for item in matrix[::-1]:
#         for idx, value in enumerate(item):
#             new_matrix[idx].append(value)

#     return new_matrix

# matrix1 = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# matrix2 = [
#     [3, 7, 4, 2],
#     [5, 1, 0, 8],
# ]

# new_matrix1 = rotate90(matrix1)
# new_matrix2 = rotate90(matrix2)
# new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# # These examples should all print True
# print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
# print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
# print(new_matrix3 == matrix2)

# Merge Sorted Lists
# https://launchschool.com/exercises/64bea0a1
def merge(list1, list2):
    copy1 = sorted(list1.copy())
    copy2 = sorted(list2.copy())
    new_list = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            new_list.append(copy1.pop(0))
        else:
            new_list.append(copy2.pop(0))

    while copy1:
        new_list.append(copy1.pop(0))

    while copy2:
        new_list.append(copy2.pop(0))

    return new_list

# # All of these examples should print True
# print(merge([9, 5, 1], [2, 8, 6]) == [1, 2, 5, 6, 8, 9])
# print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
# print(merge([], [1, 4, 5]) == [1, 4, 5])
# print(merge([1, 4, 5], []) == [1, 4, 5])

# names1 = ['Alice', 'Kim', 'Pete', 'Sue']
# names2 = ['Bonnie', 'Rachel', 'Tyler']
# names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
#                   'Rachel', 'Sue', 'Tyler']
# print(merge(names1, names2) == names_expected)

# Merge Sort
# https://launchschool.com/exercises/f62ab8aa
# def merge_sort(lst):
#     # Keeping this code, just because
#     # list1 = lst[:]

#     # list1 = [list1[:len(list1) // 2], list1[len(list1) // 2:]]

#     # list1[0] = [list1[0][:len(list1[0]) // 2], list1[0][len(list1[0]) // 2:]]
#     # list1[1] = [list1[1][:len(list1[1]) // 2], list1[1][len(list1[1]) // 2:]]

#     # list1[0][0] = [list1[0][0][:len(list1[0][0]) // 2], list1[0][0][len(list1[0][0]) // 2:]]
#     # list1[0][1] = [list1[0][1][:len(list1[0][1]) // 2], list1[0][1][len(list1[0][1]) // 2:]]

#     # list1[1][0] = [list1[1][0][:len(list1[1][0]) // 2], list1[1][0][len(list1[1][0]) // 2:]]
#     # list1[1][1] = [list1[1][1][:len(list1[1][1]) // 2], list1[1][1][len(list1[1][1]) // 2:]]


#     # list1[0][0] = merge(list1[0][0][0], list1[0][0][1])
#     # list1[0][1] = merge(list1[0][1][0], list1[0][1][1])

#     # list1[1][0] = merge(list1[1][0][0], list1[1][0][1])
#     # list1[1][1] = merge(list1[1][1][0], list1[1][1][1])

#     # list1[0] = merge(list1[0][0], list1[0][1])
#     # list1[1] = merge(list1[1][0], list1[1][1])

#     # list1 = merge(list1[0], list1[1])

#     # return list1

#     if len(lst) == 1:
#         return lst

#     sublist1 = lst[:len(lst) // 2]
#     sublist2 = lst[len(lst) // 2:]

#     sublist1 = merge_sort(sublist1)
#     sublist2 = merge_sort(sublist2)

#     return merge(sublist1, sublist2)

# # All of these examples should print True
# print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
# print(merge_sort([5, 3]) == [3, 5])
# print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
# print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

# original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#             'Kim', 'Bonnie']
# expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
#             'Sue', 'Tyler']
# print(merge_sort(original) == expected)

# original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
#             43, 5, 25, 35, 18, 46]
# expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
#             35, 37, 43, 46, 51, 54]
# print(merge_sort(original) == expected)

# Binary Search
# https://launchschool.com/exercises/97414944
def binary_search(lst, search_item):
    copy_list = lst[:]
    idx_counter = 0

    while len(copy_list) > 1:
        half = len(copy_list) // 2

        if search_item > copy_list[half]:
            idx_counter += half
            copy_list = copy_list[half:]

        elif search_item < copy_list[half]:
            copy_list = copy_list[:half]

        else:
            idx_counter += half

            return idx_counter

    return idx_counter + len(copy_list) // 2 if search_item == copy_list[0] else -1

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)

# # Egyptian Fractions
# # https://launchschool.com/exercises/17162736


# from fractions import Fraction

# # Using the egyptian function
# # Your results may differ for these first 3 examples
# print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
# print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
# print(egyptian(Fraction(3, 1)))
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# # Using the unegyptian function
# # All of these examples should print True
# print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
# print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
# print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
# print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
# print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
# print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
# print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
# print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))