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

# Palindromic Strings (Part 2)
# https://launchschool.com/exercises/4f333858?track=python
def is_real_palindrome(string):
    new_string = ''.join([character.lower() for character in string if character.isalpha() == True or character.isdigit() == True])
    reverse_string = new_string[::-1]

    return new_string == reverse_string

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# # # case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# # only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True