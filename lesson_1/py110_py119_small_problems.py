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
#         return f'{number_list[0] + DEGREES + "00" + MINUTES + "00" + SECONDS}'

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

#             if minutes_list[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
#                 minutes_value = minutes_list[0]
#                 seconds_value = str(int(60 * float("." + minutes_list[1])))

#             else:
#                 minutes_value = minutes_list[0]
#                 print(minutes_list[1])
#                 seconds_value = str(60 * float("." + minutes_list[1]))
#                 if int(float(seconds_value)) < 10:
#                     seconds_value = "0" + str(int(float(seconds_value)))

#         return f'{degrees_value}{DEGREES}{minutes_value}{MINUTES}{seconds_value}{SECONDS}'

# # All of these examples should print True
# print(dms(93.034773) == "93°02'05\"")
# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
# # Further exploration
# print(dms(-1))   # 359°00'00"
# print(dms(400))  # 40°00'00"
# print(dms(-40))  # 320°00'00"
# print(dms(-420)) # 300°00'00"

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

# Arrange a Dictionary
# https://launchschool.com/exercises/8817379e
def order_by_value(dictionary):
    tuple_list = sorted(dictionary.items(), key=lambda item: item[1])

    return [key for key, value in tuple_list]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True