### Searching 101
Write a program that solicits six (6) numbers from the user and prints a message
that describes whether the sixth number appears among the first five.

- Input: A list of integers, received from the user
- Output: A string describing if the 6th integer is in the first 5.

Rules:
- Explicit
    - 6 numbers
    - Numbers input by user
    - Message must be printed
- Implicit
    - 6th number does not need to be in the first 5

Questions:
- None so far

Data Structures:
- Will be using a list to iterate over the integers

Programmatic Algorithm:
1. Start:
    - "numbers list" = empty list
    - While the length of "numbers list" is less than 6, solicit integer from user
    - If input is not an integer, resolicit an integer
    - Add user input integer to "numbers list"

2. Assign the final (6th) number to "sixth number" variable
3. Iterate over the list to determine whether "sixth number" is the same as any of the first five.
4. Return and print a string with the answer


### Palindromic Strings (Part 1)
Write a function that returns True if the string passed as an argument is a
palindrome, False otherwise. A palindrome reads the same forwards and backwards.
For this problem, the case matters and all characters matter.

- Input: A string
- Output: A True or False boolean value

Rules:
- Explicit
    - Case matters
    - All characters matter
        - Spaces, punctuation, etc.
- Implicit
    - Strings can contain numbers
    - Strings can contain punctuation
    - Strings can contain spaces

Questions:
- None so far

Data Structures:
- Will use a list for the initial string, and another list to check the reverse

Programmatic Algorithm:
1. Start:
    - define function "is palindrome"
    - "input string" = string from input
    - "character list" = list of characters from input string
    - "reverse list" = a reverse sliced copy of "character list"

2. return the value of "character list" == "reverse list"


### Palindromic Strings (Part 2)
Write another function that returns True if the string passed as an argument is
a palindrome, or False otherwise. This time, however, your function should be
case-insensitive, and should ignore all non-alphanumeric characters. If you
wish, you may simplify things by calling the is_palindrome function you wrote in
the previous exercise.

- Input: A string
- Output: A True or False boolean value

Rules:
- Explicit
    - Case doesn't matter
    - Only alphanumeric characters matter
        - Spaces, punctuation, etc. are irrelevant
- Implicit
    - Strings can contain numbers
    - Strings can contain punctuation
    - Strings can contain spaces

Questions:
- None so far

Data Structures:
- A list to remove irrelevant characters from the initial string

Programmatic Algorithm:
1. Start:
    - define function "is real palindrome"
    - "new string" = a joined list of relevant characters from the original string
    - "reverse string" = a string that is a reverse sliced copy of "new string"

2. return the value of "new string" == "reverse string"


### Running Totals
Write a function that takes a list of numbers and returns a list with the same
number of elements, but with each element's value being the running total from
the original list.

- Input: A list of numbers
- Output: A new list with each element being the running total of the original list

Rules:
- Explicit
    - Must be in a function
    - Function takes one argument
- Implicit
    - Empty lists should return an empty list

Questions:
- None

Data Structures:
- List to hold new elements that will be the running count
- A variable to hold the count of the current iteration

Programmatic Algorithm:
1. Start:
    - define function "running total"
    - "running total list" = empty list
    - "running count" = 0

2. For each element in the parameter, sum the total to that index and set
    "running count" to total
3. Append "running count" to "running total list"
4. Return "running total list"


### Letter Counter (Part 1)
Write a function that takes a string consisting of zero or more space-separated
words and returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

- Input: A string
- Output: A dictionary of key:value pairs with the length as the key and the
    value as the number of words of that length (including punctuation)

Rules:
- Explicit
    - Spaces don't count
    - Other punctuation counts as part of a word's length (apostrophes, commas, etc.)
- Implicit
    - Empty strings should return an empty dictionary

Questions:
- None

Data Structures:
- A list of words from the string argument after they've been separated
- A dictionary to hold the key value pairs

Programmatic Algorithm:
1. Start
    - define function "word sizes"
    - "word list" = list of words from parameter, separated by spaces
    - "word size dictionary" = {}
2. For word in "word list", "word size dictionary"[len(word)] += 1
3. Return "word size dictionary"


### Letter Counter (Part 2)
Modify the word_sizes function from the previous exercise to exclude non-letters
when determining word size. For instance, the word size of "it's" is 3, not 4.

- Input: A string
- Output: A dictionary of key:value pairs with the length as the key and the
    value as the number of words of that length (excluding punctuation)

Rules:
- Explicit
    - Punctuation doesn't count
- Implicit
    - Empty strings should return an empty dictionary
    - Punctuation nor special characters used as letters count as length,
        but they don't break the word either (e.g. "w@ll" has a length of 3)

Questions:
- None so far

Data Structures:
- List to break the string apart and remove unnecessary characters
- A variable to hold the length of the current word
- A dictionary to hold the key:value pairs
- A variable to hold the new string

Programmatic Algorithm:
1. Start
    - define function "word sizes"
    - "word list" = list of words from parameter, separated by spaces
    - "word size dictionary" = {}
    - "temp string" = ""
2. For word in "word list", if character in word is a letter, add it to temp string
3. Append "temp string" to "word list"
4. For word in "word list", "word size dictionary"[len(word)] += 1
5. Return "word size dictionary"


### Letter Swap
Given a string of words separated by spaces, write a function that swaps the
first and last letters of every word.

You may assume that every word contains at least one letter, and that the string
will always contain at least one word. You may also assume that each string
contains nothing but words and spaces, and that there are no leading, trailing,
or repeated spaces.

- Input: A string of words
- Output: A string of words with the first and last letter of each word reversed

Rules:
- Explicit:
    - Swap first and last letter of each word
    - Each string has no leading, trailing, or repeated spaces
    - All strings have a length of at least 1
- Implicit:
    - Strings cannot be empty

Questions:
- None

Data Structures:
- A list to split the string for iterating
- A list for holding swapped strings
- A temporary string for holding the reversed string before appending it to the
    swapped list

Programmatic Algorithm:
1. Start
    - define function "swap"
    - "word list" = list of words from the parameter string
    - "swapped list" = empty list
    - temp_string = empty string
2. For word in "word list", add last character to "temp string"
    - - "temp string += word[-1]"
3. Add all characters after the first character to "temp string"
    - Use the range function to iterate over the word, for the length of the word
        minus one (since the last character is added already)
    - Ignore characters on iteration 0 (word[0] is added after)
4. Add first character to "temp string"
    - "temp string += word[0]"
5. Append temp string to "swapped list"
6. Join "swapped list"

Notes:
- For some reason, I mixed up the syntax to slice the string (used a comma
  instead of a colon), and this caused me to resort to the range function to
  iterate over the word, instead of just concatenating with slicing. It works,
  but it is quite the amalgamation...


### Convert a String to a Number
Write a function that takes a string of digits and returns the appropriate
number as an integer. You may not use any of the standard conversion functions
available in Python, such as int. Your function should calculate the result by
using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry about
invalid characters; assume all characters are numeric.

- Input: A string of numbers
- Output: An integer value of the string argument

Rules:
- Explicit:
    - Not allowed to use standard conversion functions such as int()
    - Calculate result using the characters in the string
    - All characters in the string are numeric
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to split the string

Programmatic Algorithm:
1. Start
    - define function "string to integer"
    - "number list" = number for number in string
    - "integer value" = 0
    - "place value" = 1
2. for number in "number list":
3. "integer value" += number * 1
4. "integer value" += number * 10
5. "integer value" += number * 100...
6. return "integer value"

Notes:
- Used a match case statement, but I liked the LS method of using a dictionary.
  Less code and the method for creating the integer uses a lot less memory it
  seems. I wonder if this is because the match case statement is checking the
  match value against every case statement until it finds the match, whereas
  the dictionary simply uses the value of the key.
  Incidentally, I spaced when writing the programmatic algorithm, thinking I
  could just multiply the number despite not being able to use int().


### Convert a String to a Signed Number
In the previous exercise, you developed a function that converts simple numeric
strings to integers. In this exercise, you're going to extend that function to
work with signed numbers.

Write a function that takes a string of digits and returns the appropriate number
as an integer. The string may have a leading + or - sign; if the first character
is a +, your function should return a positive number; if it is a -, your
function should return a negative number. If there is no sign, return a positive
number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python,
such as int. You may, however, use the string_to_integer function from the
previous exercise.

- Input: A string of numbers
- Output: An integer value of the string argument

Rules:
- Explicit:
    - Not allowed to use standard conversion functions such as int()
    - Calculate result using the characters in the string
    - String may contain a + or -, but won't always include one
    - if the first character is a +, the function should return a positive
        number; if it is a -, the function should return a negative number
- Implicit:
    - Positive numbers should not have a + sign when returned

Questions:
- None

Data Structures:
- A dictionary to hold key:value pairs
- A list to hold the string values to remove any + or - before looping

Programmatic Algorithm:
1. Start
    - define function "string to signed integer"
    - "value" = 0
    - "string list" = list(string)
2. if "string list[0]" == "+":
3. remove "+" from "string list"
4. for char in "string list":
5. value = (10 * value) + DIGITS[char]
6. return value
7. elif "string list[0]" == "-":
8. remove "-" from "string list"
9. for char in "string list":
10. value = (10 * value) + DIGITS[char]
11. value *= -1
12. return value
13. else:
14. for char in "string list":
15. value = (10 * value) + DIGITS[char]
16. return value

Notes:
- I opted to use 1 function, with if/elif statements and rewrote the LS code, as,
  I wanted to try using a dictionary instead of match/case statement. The LS
  version called the previous function in the solution to this problem, which
  seems much better imo.


### Convert a Number to a String
In the previous two exercises, you developed functions that convert simple
numeric strings to signed integers. In this exercise and the next, you're going
to reverse those functions.

Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3,
and so on) to the string representation of that integer.

You may not use any of the standard conversion functions available in Python,
such as str. Your function should do this the old-fashioned way and construct
the string by analyzing and manipulating the number.

- Input: A non-negative integer value
- Output: A string representation of the integer value

Rules:
- Explicit:
    - Not allowed to use standard conversion functions such as str()
    - Only positive integer values
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to store each place in the integer
- A dictionary for values and their string representations
- A new list to append values to and eventually join

Programmatic Algorithm:
1. Start
    - define function "integer to string"
    - if number == 0:
        - return "0"
    - "multiplier" = 10
    - i = 1
    - "current value" = 0
    - "new_list" = []
    - "DIGITS"
2. while True:
    - "current_value" = divmod(number, multiplier)[1]
    - if "current_value" < (x * i):
    - append DIGITS[y] to "new_list"
6. if "current_value" == number:
    - break
8. multiplier *= 10
9. i *= 10
10. set "new_list" = to a reverse slice of itself
11. set "number_string" = "new_list" joined

Notes:
- Haven't used the divmod() function before, so this was new. I wasn't really
  sure how I should go about using it at first and so it regrettably turned
  into a bit of a hack and slash while trying to figure out how to proceed
  with the tuples. Looking at the LS solution, I'm not sure why I used a
  dictionary instead of a list or simply the string "0123456789"... Naturally,
  due to my inexperience, my solution is immensely more memory intensive.

  Additionally, I think the variables in my solution are somewhat unclear or
  confusing.

  Furthermore, because my programmatic algorithm was completely wrong, I
  decided to rewrite it to reflect my solution. This is backwards, but it's
  still good practice.

### Convert a Signed Number to a String
In the previous exercise, you developed a function that converts non-negative
numbers to strings. In this exercise, you're going to extend that function by
adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string
representation.

You may not use any of the standard conversion functions available in Python,
such as str. You may, however, use integer_to_string from the previous exercise.

- Input: An integer value
- Output: A signed string representation of the integer value

Rules:
- Explicit:
    - Not allowed to use standard conversion functions such as str()
    -
- Implicit:
    - String representation should contain a + or - at the front, unless the
        value is 0

Questions:
- None

Data Structures:
- A list to store each place in the integer
- A dictionary for values and their string representations
- A new list to append values to and eventually join

Programmatic Algorithm:
1. Start
    - define function "signed integer to string"
    - if number > 0:
        - positive = "+"
        - string = integer_to_string(number)
        - positive_string = positive + string
        - return positive_string
    - "multiplier" = 10
    - elif number > 0:
        - negative = "-"
        - string = integer_to_string(number * -1)
        - negative_string = negative + string
        - return negative_string
    - else:
        - return integer_to_string(number)
2. while True:
    - "current_value" = divmod(number, multiplier)[1]
    - if "current_value" < (x * i):
    - append DIGITS[y] to "new_list"
6. if "current_value" == number:
    - break
8. multiplier *= 10
9. i *= 10
10. set "new_list" = to a reverse slice of itself
11. set "number_string" = "new_list" joined

Notes:
- Pretty quick solve. LS used f-strings, which may or may not be "better", but I
    do prefer the use of f-strings, as it circumvents the somewhat unnecessary
    use of variables.


### Cute Angles
Write a function that takes a floating point number representing an angle
between 0 and 360 degrees and returns a string representing that angle in
degrees, minutes, and seconds. You should use a degree symbol (°) to represent
degrees, a single quote (') to represent minutes, and a double quote (") to
represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:
DEGREE = "\u00B0"

- Input: A floating point number representing an angle between 0 and 360 degrees
- Output: A string representing the floating point number in degrees, minutes,
    and seconds

Rules:
- Explicit:
    - Returns a string
    - Use a degree symbol (°) to represent degrees, a single quote (') to
        represent minutes, and a double quote (") to represent seconds
- Implicit:
    -

Questions:
- I'm not familiar with DMS calculations, so I don't understand why 254.6 is
    converted to 254°35'59" instead of 254°36'00". Maybe if there are 0 seconds
    the conversion is such that you subtract a minute and add 59 seconds?

Data Structures:
- A list to split at decimals

Programmatic Algorithm:
1. Start
    - DEGREES = "\u00B0"
    - MINUTES = '"'
    - SECONDS = "'"
    - define function "dms"
    - "number list" = parameter number split at decimal
2. If the length of "number list" is 1:
    - return f'{number list[0] + DEGREES + "00" + MINUTES + "00" + SECONDS}'
3. Else:
    - "degrees value" = "number list[0]" as a string
    - if "number list[0]" in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
        - "minutes value" = str((60 * (numbers list[1] / 100)) - 1)
        - "seconds value" = "59"
    - else:
        - "minutes value" = str(60 * (numbers list[1] / 10))
        - "minutes list" = "minutes value" split at decimal
        - "seconds value" = str(60 * (minutes list[1] / 10))
    return f'{degrees value + DEGREES + minutes value + MINUTES + seconds value + SECONDS}'

Notes:
- Well, I'm not proud of the code... But I didn't give up, so that's something.
  It's far more hideous than anything I've written thus far, I believe, but
  it does work...
  Incidentally, it uses less memory than the LS version, but I think that's
  because it uses if statements to cover so many different outliers...

  Using constants for the 60 minutes in an hour and 60 seconds in a minute,
  like LS did, is probably best practice.

  LS use of another function to add zeroes was somewhat funny, because when I
  was adding zeroes I thought "there's no way this is how I should be adding
  them."

  Subtracting the int(parameter) from the float(parameter), instead of using
  lists to split it, should have been obvious. I'll chop up missing it to being
  rusty from the weekend...

  Edit: Added further exploration. Took about 1 minute.

### Combining Lists
Write a function that takes two lists as arguments and returns a set that
contains the union of the values from the two lists. You may assume that both
arguments will always be lists.

- Input: Two lists
- Output: A set containing the union of the values of both lists

Rules:
- Explicit:
    - Arguments will always be lists
    -
- Implicit:
    - None

Questions:
- None

Data Structures:
- A new list to concatenate the 2 lists
- A set to coerce and return

Programmatic Algorithm:
1. Start
    - define function "union"
    - "new list" = list1 + list2
    - "new set" = set("new list")
2. return "new set"

Notes:
- Did the above first, but refactored because this looked nicer.


### Halvsies
Write a function that takes a list as an argument and returns a list that
contains two elements, both of which are lists. Put the first half of the
original list elements in the first element of the return value and put the
second half in the second element. If the original list contains an odd number
of elements, place the middle element in the first half list.

- Input: A list
- Output: A list containing the list parameter split in half

Rules:
- Explicit:
    - If the input list is odd length, the first list should be the longer list
    -
- Implicit:
    - If an empty list is input, it should return a list containing 2 empty lists
    - if the length of the input list is 1, it should return a a list with a
        list containing that value, along with an empty list

Questions:
- None

Data Structures:
- A new list to append the lists to and then return

Programmatic Algorithm:
1. Start
    - define function "halvsies"
    - if the length of the list is odd:
        - append list containing the elements up to the half way point + 1, to
            the return list
    - else:
        - append list containing remaining elements from the half way point, to
            the return list
    - return return list


### Find the Duplicate
Given an unordered list and the information that exactly one value in the list
occurs twice (every other value occurs exactly once), determine which value
occurs twice. Write a function that finds and returns the duplicate value.

You may assume that the input list will always have exactly one duplicate value.

- Input: A list of numbers
- Output: An integer of the duplicate value

Rules:
- Explicit:
    - The input list will always have exactly one duplicate value
    -
- Implicit:
    - Cannot be an empty list

Questions:
- None

Data Structures:
- A dictionary to hold key:values of the number and its count

Programmatic Algorithm:
1. Start
    - define function "find dup"
    - number_dict = {}
    - for each number in numbers:
        - if the number is in number dict:
            - add 1 to its key
        - else:
            - set key equal to 1
    - for each key:value pair in number_dict.items():
        - if value is 2:
            - return key

Notes:
- I noticed that while the LS version used a set for the "seen" values, probably
  to drill in the fact that sets can hold only unique values, a list, etc.
  works as well since you're only checking if the element is in the collection.


### Combine Two Lists
Write a function that combines two lists passed as arguments and returns a new
list that contains all elements from both list arguments, with each element
taken in alternation.

You may assume that both input lists are non-empty, and that they have the same
number of elements.

- Input: Two lists
- Output: A list containing the elements of both lists in alternating order

Rules:
- Explicit:
    - Lists can not be empty
    - Lists have the same number of elements
- Implicit:
    - The first element should be element 1 of list 1

Questions:
- None

Data Structures:
- A new list to append values and return

Programmatic Algorithm:
1. Start
    - define function "interleave"
    - combined_list = []
    - for i in range len(list1):
        - combined_list.append(list1[i])
        - combined_list.append(list2[i])

Notes:
- Should have used extend to add the elements with a single line, like the LS
  method. Regardless, pretty simple. The further exploration with the zip
  method only took a moment as well.


### Multiplicative Average
Write a function that takes a list of positive integers as input, multiplies all
of the integers together, divides the result by the number of entries in the
list, and returns the result as a string with the value rounded to three decimal
places.

- Input: A list containing 2 integers
- Output: A string representation of the quotient of the product of all numbers
    in the original list, rounded to 3 decimal places

Rules:
- Explicit:
    - None
- Implicit:
    - No empty lists
    - Input lists will have at least 2 values

Questions:
- None

Data Structures:
- A list to split the value at the decimal?

Programmatic Algorithm:
1. Start
    - define function "multiplicative_average"
    - product = 1
    - for number in numbers:
        - product *= number
    - quotient = product / length of numbers
    - string_value = str(round(quotient, 3))
    - return string_value

Notes:
- Could have solved with some abhorrent code, but I didn't want to spend a lot of
  time on this so I looked at the LS code. I haven't used find() before, but
  it seems like a good way to solve something like this, instead of defaulting
  to trying to split the number at the decimal and solve it from there as I've
  been doing. Also, the Format Specification Mini-Language was interesting to
  see. Seems very useful.


### Multiply Lists
Write a function that takes two list arguments, each containing a list of
numbers, and returns a new list that contains the product of each pair of numbers
from the arguments that have the same index. You may assume that the arguments
contain the same number of elements.

- Input: Two lists of numbers
- Output: A list containing the products of the corresponding indexes from each
    list

Rules:
- Explicit:
    - Lists are the same length
    - No empty lists
- Implicit:
    - None

Questions:
- None

Data Structures:
- A new list to append to and return

Programmatic Algorithm:
1. Start
    - define function "multiply lists"
    - product_list = []
    - product = 0
    - for i in range(len(list1)):
        - product_list.append(list1[i] * list2[i])
    - return product_list


### List of Digits
Write a function that takes one argument, a positive integer, and returns a list
of the digits in the number.

- Input: A postive integer
- Output: A list containing each digit in the input integer

Rules:
- Explicit:
    - None
- Implicit:
    - Input list has length of at least 1

Questions:
- None

Data Structures:
- A list to append to and return

Programmatic Algorithm:
1. Start
    - Too simple to waste time on

Notes:
- I originally started with a normal for loop, but figured that since the LS
  solution have been using a lot of list comprehension lately, I should change
  mine to list comprehension as well. Not sure why I used range. I guess it made
  more sense at the time. Still works just as good, just very slightly longer.


### How Many?
Write a function that counts the number of occurrences of each element in a
given list. Once counted, print each element alongside the number of occurrences.
Consider the words case sensitive e.g. ("suv" != "SUV").

- Input: A list of vehicles
- Output: All of the vehicles printed with their appearance count

Rules:
- Explicit:
    - Count should be printed alongside the vehicle
    - Vehicle names are case sensitive (SUV != suv)
- Implicit:
    - None

Questions:
- None

Data Structures:
- A dictionary to hold key:value pairs of vehicles and their count

Programmatic Algorithm:
1. Start
    - define function "count occurrences"
    - vehicles_dictionary = {}
2. for vehicle in vehicles:
    - if vehicle not in vehicles_dictionary:
        - vehicles_dictionary[vehicle] = 1
    - else:
        - vehicles_dictionary[vehicle] += 1
3. - for vehicle, count in vehicles_dictionary.items():
        - print(f'{vehicle}: {count}')

Notes:
- Originally had it all in one function, but I need to get into the habit of
    extracting processes to other functions for readability, etc.


### List Average
Write a function that takes one argument, a list of integers, and returns the
average of all the integers in the list, rounded down to the integer component
of the average. The list will never be empty, and the numbers will always be
positive integers.

- Input: A list of integers
- Output: The floored mean of the numbers

Rules:
- Explicit:
    - No empty lists
    - Numbers always positive
- Implicit:
    - None

Questions:
- None

Data Structures:
- None

Programmatic Algorithm:
1. Start
    - print the sum of the numbers list floor divided by the length of the
        numbers list


### After Midnight (Part 1)
The time of day can be represented as the number of minutes before or after
midnight. If the number of minutes is positive, the time is after midnight. If
the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns
the time of day in 24-hour format (hh:mm). Your function should work with any
integer input.

You may not use Python's datetime module.

- Input: A number
- Output: The time of day in 24-hour format (hh:mm)

Rules:
- Explicit:
    - Cannot use datetime module
    - Number can be positive or negative
    - Ignore daylight savings
- Implicit:
    - Output should be a string
    - Number can be 0

Questions:
- None

Data Structures:
- A dictionary to hold key:value pairs of the hour and minute

Programmatic Algorithm:
1. Start
    - define function "time of day"
2. if number is greater than or equal to 0:
    - "hours and minutes" = {"hours": 0,
                            "minutes": 0,
                        }
    - while number is greater than or equal to 60:
        - subtract 60 from number and reassign new number to number
        - if "hours and minutes"[hours] is greater than 24:
            - "hours and minutes"[hours] = 0
        - add one to "hour and minutes"[hour]
    - "hours and minutes"[minutes] = number
3. if number is less than 0:
    - "hours and minutes" = {"hours": 24,
                            "minutes": 60,
                        }
    - while number is less than or equal to -60:
        - add 60 to number and reassign new number to number
        - if "hours and minutes"[hours] is greater than 0:
            - "hours and minutes"[hours] = 24
        - subtract one from "hour and minutes"[hour]
    - "hours and minutes"[minutes] = number

4. hours = pad_zeroes("hours and minutes"[hours])
5. minutes = pad_zeroes("hours and minutes"[minutes])
6. return f'{hours}:{minutes}'
7. define function "pad zeroes"
8. if number is less than 10:
        - stringify number and add zero to front
    - else:
        - stringify number
9. return number

Notes:
- This one took a bit to fix all the small bugs with >= problems, etc. Looking at
  the LS solution, I definitel should have used constants for minutes/hour and
  hours/day instead of having all of these magic numbers in mine. Also, I should
  have used Format Specification Mini-Language inside of the pad_zeroes()
  function instead of how I did it.


### After Midnight (Part 2)
As seen in the previous exercise, the time of day can be represented as the
number of minutes before or after midnight. If the number of minutes is positive,
the time is after midnight. If the number of minutes is negative, the time is
before midnight.

Write two functions that each take a time of day in 24 hour format, and return
the number of minutes before and after midnight, respectively. Both functions
should return a value in the range 0 through 1439.

You may not use Python's datetime module.

- Input: A string of the time of day in 24 hour format
- Output: The number of minutes before and after midnight

Rules:
- Explicit:
    - Cannot use datetime module
    - Must write two functions, one for before midnight, and one for after
    midnight
    - Ignore daylight savings
- Implicit:
    - Output should be a number

Questions:
- None

Data Structures:
- None

Programmatic Algorithm:
1. Start
    - define function "after midnight"
    - MINUTES_PER_HOUR = 60
2. if time == "00:00" or time == "24:00":
        - return 0
3. number = multiply the first 2 digits of time by MINUTES_PER_HOUR
4. Add the last 2 digits of time to number
5. return number
6. define function "before midnight"
    - MINUTES_PER_DAY = 1440
7. number = "after midnight"(time)
8. number = MINUTES_PER_DAY -= number
9. return number

Notes:
- Originally I used an if statement to catch the '24:00' and '00:00' outliers,
  but I wasn't satisfied with this and opted to refactor to use modulo, as I
  should be doing anyways. I feel like the mental block is just my lack of
  experience using modulo.


### Double Char (Part 1)
Write a function that takes a string, doubles every character in the string,
then returns the result as a new string.

- Input: A string
- Output: A string with every character from the original string doubled

Rules:
- Explicit:
    - None
- Implicit:
    - An empty string should output an empty string
    - Spaces should also be doubled

Questions:
- None

Data Structures:
- A new string

Programmatic Algorithm:
1. Start
    - define function "repeater"
    - doubled = ""
2. for character in string:
3. doubled += character * 2
4. return doubled

Notes:
- Wrote it with a for loop, and then wrote it using list comprehension and join,
  just to use both methods. Funny that LS used the same exact code basically.


### Double Char (Part 2)
Write a function that takes a string, doubles every consonant in the string, and
returns the result as a new string. The function should not double vowels
('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.

- Input: A string
- Output: A string with every consonant doubled

Rules:
- Explicit:
    - All characters are ascii character
- Implicit:
    - Empty strings return an empty string

Questions:
- None

Data Structures:
- A new string

Programmatic Algorithm:
1. Start
    - define function "double consonants"
    - CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
    - new_string
2. for character in string:
    - if character.lower() in CONSONANTS:
        - new_string += character * 2
    - else:
        - new_string += character
3. return new_string


### Reverse Number
Write a function that takes a positive integer as an argument and returns that
number with its digits reversed.

- Input: A positive integer
- Output: That number with its digits reversed

Rules:
- Explicit:
    - Only positive integers
    - Single digit integers are possible
- Implicit:
    - Leading 0's should be deleted, naturally

Questions:
- None

Data Structures:
- A list to store the digits and reverse it

Programmatic Algorithm:
1. Start
    - define function "reverse_number"
    - digit_list = [character for character in str(number)]
2. reverse digit_list
3. join digit_list
4. coerce digit_list to int
5. return digit_list

Notes:
- Should have just sliced the stringified integer backwards like LS. Removed my
  code and rewrote it because this is way better. Need to get into the habit of
  slicing strings.


### Counting Up
Write a function that takes an integer argument and returns a list containing all
integers between 1 and the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.

- Input: A positive integer
- Output: A list of all numbers preceding that integer

Rules:
- Explicit:
    - List contains all numbers up to and including the input integer
    - Ascending order
    - Input is always a positive integer
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to hold the integers and return

Programmatic Algorithm:
1. Start
    - define function 'sequence'
    - number_list = []
2. for num in range(1, number + 1)
    - number_list.append(num)
3. return number_list

Notes:
- Need to practice writing more concise code like LS solutions. Most of what I
  write can be condensed. That being said, I haven't used range() much outside
  of looping, so it's still kind of new to me.


### Name Swapping
Write a function that takes a string argument consisting of a first name, a
space, and a last name. The function should return a new string consisting of the
last name, a comma, a space, and the first name.

- Input: A string containing a first and last name
- Output: A string with the first and last name swapped and separated by a comma
    and a space

Rules:
- Explicit:
    - Names don't include suffixes, etc.

- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to store the names

Programmatic Algorithm:
1. Start
    - define function 'swap_name'
    - name_list = [name for name in full_name.split()]
2. return name_list[1] + ', ' + name_list[0]

Notes:
- Originally wrote it with the above algorithm, but wanted to practice writing
  more consise code, and so I refactored it to the current version. Matches LS
  as well.


### Sequence Count
Create a function that takes two integers as arguments. The first argument is a
count, and the second is the starting number of a sequence that your function
will create. The function should return a list containing the same number of
elements as the count argument. The value of each element should be a multiple
of the starting number.

You may assume that count will always be an integer greater than or equal to 0.
The starting number can be any integer. If the count is 0, the function should
return an empty list.

- Input: Two integers - A count and a startign number
- Output: A list containing the same number of elements as the count argument,
    with each element being a multiple of the starting number.

Rules:
- Explicit:
    - Count integer will always be >= 0
    - Starting number can be any integer
    - If the count is 0, return an empty list
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to hold the integers and return

Programmatic Algorithm:
1. Start
    - define function 'sequence'
    - step_value = start_value
    - number_list = []
2. while count > 0:
    - number_list.append(start_value)
    - start_value += step_value
    - count -= 1
3. return number_list

Notes:
- my method worked, but again it was too long. Refeactored to make it as short
  as possible, but got hung up on the 0 count.


### Reversed Lists
Write a function that takes a list as an argument and reverses its elements, in
place. That is, mutate the list passed into the function. The returned object
should be the same object used as the argument.

You may not use the list.reverse method nor may you use a slice ([::-1]).

- Input: A list
- Output: The input list reversed, not a new list

Rules:
- Explicit:
    - Cannot use reverse slicing or reverse methods
- Implicit:
    - An empty list should return an empty list

Questions:
- I assume we're not allowed to use reversed() either?

Data Structures:
- A new list to append elements to and return

Programmatic Algorithm:
1. Start
    - define function 'reverse_list'
    - new_list = []
2. while len(input_list) > 0:
    - new_list = input_list.pop()
3. for element in new_list:
    - input_list.append(element)
4. return input_list

Notes:
- LS method seems good, but my method of popping to another list and appending
  seems fine as well. Khaled Jaafar did what I wanted to do originally with
  the range function, but I didn't think of using the insert() method like he
  did.


### Matching Parenthesis?
Write a function that takes a string as an argument and returns True if all
parentheses in the string are properly balanced, False otherwise. To be properly
balanced, parentheses must occur in matching '(' and ')' pairs.

- Input: A string
- Output: True or False based on whether or not the parentheses in the string are
    balanced

Rules:
- Explicit:
    - To be properly balanced, parentheses must occur in matching '(' and ')'
    pairs.
- Implicit:
    - None

Questions:
- None

Data Structures:
- A dictionary to hold the counts of each parentheses type

Programmatic Algorithm:
1. Start
    - define function 'is_balanced'
    - parentheses_counter = {'left': 0,
                            'right': 0,
                            }
2. for char in string:
    - if char == '(':
        - parentheses_counter['left'] += 1
    - elif char == ')':
        - parentheses_counter['right'] += 1
        - if parentheses_counter['right'] > parentheses_counter['left']:
            - return False
3. return parentheses_counter['left'] == parentheses_counter['right']

Notes:
- Was easy enough. I did the further exploration and opted to use match:case
  statements. All of my test cases passed except for is_balanced("{[}]") == False.
  However, like Cody Reimers pointed out in his comment, "the further exploration
  didn't ask to validate grouping, just that each individual pair of symbols were
  properly balanced," and I was coding with the same thought process. As such,
  I changed the "is_balanced("{[}]") == False" line to "is_balanced("{[}]") == True".

  Admittedly, it's a bit verbose, perhaps, but I think match:case statements
  look nice and are easy to read.


### Alphabetical Numbers
Write a function that takes a list of integers between 0 and 19 and returns a
list of those integers sorted based on the English word for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve,
thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen

```Python
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True
```

- Input: A list of numbers from 0-19
- Output: A list of integers sorted by their English word equivalent

Rules:
- Explicit:
    - None
- Implicit:
    - None

Questions:
- Should the output be a new list?
- Can the input list be shorter than 20 numbers?

Data Structures:
- A list of tuples?

Programmatic Algorithm:
1. Start
    - define function "alphabetic_number_sort"
    - tuple_list = [(1, "one"), (2, "two"), (3, "three"), ...]
    - new_nums = []
2. sort tuple list by tuple index[1]
3. for integer, word in tuple_list:
    - for num in number_list:
        - if num equals integer:
            - new_nums.append(num)
4. return new_nums

Notes:
- Not sure why, but I got hung up on the looping process and was having trouble
  debugging it. I really think I just suck at coding on Mondays...

  Incidentally, I opted to use a list of tuples instead of just a list of
  manually sorted names because 1. it felt like cheating, and 2. I didn't feel
  like manually sorting the names for the list (although I could have just ran
  sorted() on it with the names out of order and then copy pasted it I suppose).


### Merge Sets
Given two lists, convert them to sets and return a new set which is the union of
both sets.

- Input: Two lists
- Output: A new set that is the union of the 2 lists after they've been converted
    to sets

Rules:
- Explicit:
    - Must return a new set
- Implicit:
    - None

Questions:
- None

Data Structures:
- Sets, obviously

Programmatic Algorithm:
1. Start
    - define function "merge_sets"
2. set1 = convert_to_set(list1)
3. set2 = convert_to_set(list2)
4. merged_set = set1 | set2
5. return merged_set
6. define function "convert_to_set(iterable)"
    - return set(iterable)

Notes:
- Pretty simple. I opted to extract the set conversion to another function instead
  of doing it all in one function


### Immutable Intersection
Transform two lists into frozen sets and find their common elements.

- Input: Two lists
- Output: A frozen set containing the intersection of the two lists after they've
    been converted to frozen sets

Rules:
- Explicit:
    - Lists must be transformed into frozen sets
- Implicit:
    - None

Questions:
- Can there be more than one common element?

Data Structures:
- Frozen sets

Programmatic Algorithm:
1. Start
    - define function "intersection"
    - frozen1 = frozenset(list1)
    - frozen2 = frozenset(list2)
2. return frozen1.intersection(frozen2)

Notes:
- I used the intersection method, but I could just have easily used the `&`
  operator.


### Arrange a Dictionary
Given a dictionary, return its keys sorted by the values associated with each
key.

- Input: A dictionary
- Output: A list containing the keys of the dictionary, sorted by the values of
    the dictionary

Rules:
- Explicit:
    - None
- Implicit:
    - Must return a list of keys

Questions:
- None

Data Structures:
- A list to append to and return

Programmatic Algorithm:
1. Start
    - define function "order_by_value"
    - tuple_list = a list of tuples that contain the key:value pairs extracted
        from dictionary.items(), which is sorted by the values of said dictionary
2. return a list that contains each element at index[1] for each item in tuple_list

Notes:
- Still getting used to using `sorted()` and `.sort`. William Pognonec had a
  solution that I thought was interesting:

```Python
def order_by_value(d):
    return sorted(d, key=lambda x: d[x])
```
  I didn't understand why it was returning a list until I realized that `sorted()`
  is like coercing the keys into a list object on its own. It's still weird to
  me because it seems like the `sorted()` function is sorting tuples, but it
  seems that when you call `sorted()` on a dictionary, it defaults to the
  dictionary's keys.


### Unique Elements
From two list arguments, determine the elements that are unique to the first
list. The return value should be a set.

- Input: Two lists
- Output: A set containing the unique elements from the first list

Rules:
- Explicit:
    - Should return a set
- Implicit:
    - None

Questions:
- None

Data Structures:
- A set to add to and return

Programmatic Algorithm:
1. Start
    - define function 'unique_from_first'
2. return list1 and list 2 coerced to sets and then the difference
    method used on them


### Leading Substrings
Write a function that takes a string argument and returns a list of substrings
of that string. Each substring should begin with the first letter of the word,
and the list should be ordered from shortest to longest.

- Input: A string
- Output: A list of substrings from that string

Rules:
- Explicit:
    - Each substring should start with the first letter of the string
    - Ordered from shortest to longest
- Implicit:
    - A string with a length of one should return the single character in a list

Questions:
- None

Data Structures:
- A list to append to and return

Programmatic Algorithm:
1. Start
    - define function 'leading_substrings'
    - substrings = []
2. for i in range(len(string)):
        - append string[0:i] to substrings
3. return substrings

Notes:
- Pretty simple solve. I saw the LS code did it in one line, so I rewrote mine
  in one line for fun. I still feel like having the whole code block is easier
  to read than just a single line, but the single line does feel nice to type.


###
Write a function that returns a list of all substrings of a string. Order the
returned list by where in the string the substring begins. This means that all
substrings that start at index position 0 should come first, then all substrings
that start at index position 1, and so on. Since multiple substrings will occur
at each position, return the substrings at a given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous
exercise:

- Input: A string
- Output: A list of ALL substrings within the string

Rules:
- Explicit:
    - Should use solution from previous problem
    - Order the returned list by where in the string the substring begins
    - return the substrings at a given index from shortest to longest.
- Implicit:
    - None

Questions:
- None

Data Structures:
-

Programmatic Algorithm:
1. Start
    - define function 'substrings'
    - substrings_list = []
2. for i in range(len(string)):
        sub_substrings = leading_substrings(string[i:])
3. for item in sub_substrings:
        - append item to substrings_list
4. return substrings_list

Notes:
- Pretty much solved it the same way that the LS solution does. Only took about
  5 minutes.


### Palindromic Substrings
Write a function that returns a list of all palindromic substrings of a string.
That is, each substring must consist of a sequence of characters that reads the
same forward and backward. The substrings in the returned list should be sorted
by their order of appearance in the input string. Duplicate substrings should be
included multiple times.

You may (and should) use the substrings function you wrote in the previous
exercise.

For the purpose of this exercise, you should consider all characters and pay
attention to case; that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are
not. In addition, assume that single characters are not palindromes.

- Input: A string
- Output: A list of all substrings that are palindromes

Rules:
- Explicit:
    - Should use the substrings function you wrote in the previous exercise.
    -
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to hold the palindromes

Programmatic Algorithm:
1. Start
    - define fucntion 'palindromes'
    - palindrome_list = []
2. for item in substrings(item):
        - if the item is the same forwards as it is backwards, and its length is
            greater than 1, append it to palindrome_list
3. return palindrome_list

Notes:
- This was surprisingly simple, due to the fact that we have the other 2
  functions already written. Definitely a good example of breaking down a larger
  problem.

  Edit: After looking at the LS discussion section, they ironically also wrote
  "This series of exercises is a good example of how to break down a problem into
  manageable chunks. Go over these three exercises again, with that perspective
  in mind."


### Inventory Item Transactions
Write a function that takes two arguments, an inventory item ID and a list of
transactions, and returns a list containing only the transactions for the
specified inventory item.

- Input: A list of dictionaries
- Output: A list of dictionaries for a particular item ID

Rules:
- Explicit:
    - None
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to append to and return

Programmatic Algorithm:
1. Start
    - define function 'transactions_for'
2. return item for item in transactions if the item's id is equal to the input ID


### Inventory Item Availability
Building on the previous exercise, write a function that returns True or False
based on whether or not an inventory item (an ID number) is available. As before,
the function takes two arguments: an item ID and a list of transactions. The
function should return True only if the sum of the quantity values of the item's
transactions is greater than zero. Notice that there is a movement property in
each transaction object. A movement value of 'out' will decrease the item's
quantity.

You may (and should) use the transactions_for function from the previous
exercise.

- Input: A list of dictionaries
- Output: True or False based on whether or not an inventory item (an ID number)
    is available.

Rules:
- Explicit:
    - Should use the transactions_for function from the previous exercise.
    - Should return True only if the sum of the quantity values of the item's
        transactions is greater than zero.
- Implicit:
    - total movement in should be greater than total movement out to ensure
        inventory

Questions:
- None

Data Structures:
-

Programmatic Algorithm:
1. Start
    - define function 'is_item_available'
    - inventory = 0
    - new_list = transactions_for(item_id, transaction_list)
2. for item in new_list:
    - if item['movement'] == 'in':
        - inventory += item['quantity']
    - else:
        - inventory -= item['quantity']
3. return inventory > 0

Notes:
- My solution was exactly the same as the LS solution, with just slightly
  different variable names. Another quick solve.


### Inverting Dictionary
Given a dictionary where both keys and values are unique, invert this dictionary
so that its keys become values and its values become keys.

- Input: A dictionary
- Output: The same dictionary with its keys and values swapped

Rules:
- Explicit:
    - All keys and values are unique
- Implicit:
    - None

Questions:
- None

Data Structures:
- A copy of the original dictionary

Programmatic Algorithm:
1. Start
    - define function 'invert_dict'
    - temp_dict = dictionary.copy()
2. clear dictionary
3. for key, value in temp_dict.items()
        - dictionary[value] = key
4. return dictionary

Notes:
- I was under the impression that I needed to use the same dictionary, but then
  I realized it wanted the return value, so it didn't matter.


### Retain Specific Keys
Given a dictionary and a list of keys, produce a new dictionary that only
contains the key/value pairs for the specified keys.

- Input: A dictionary
- Output: A new dictionary with the specified key:value pairs

Rules:
- Explicit:
    - Must return a new dictionary
- Implicit:
    - None

Questions:
- None

Data Structures:
- A dictionary to add key:value pairs to and return

Programmatic Algorithm:
1. Start
    - define function 'keep_keys'
2. return {key: value for key, value in dictionary.items() if key in keys}

Notes:
- Took about 10 seconds


### Delete Vowels
Write a function that takes a list of strings and returns a list of the same
string values, but with all vowels (a, e, i, o, u) removed.

- Input: A list of strings
- Output: A list of strings with all the vowels removed

Rules:
- Explicit:
    - List may contain only 1 string, but no less
- Implicit:
    - Must remove capital and lowercase vowels
    - A string of all vowels should become an empty string

Questions:
- None

Data Structures:
- A temporary string

Programmatic Algorithm:
1. Start
    - define function 'remove_vowels'
    - VOWELS = 'aeiouAEIOU'
    - temp_string = ''
2. for i in range(len(string_list)):
        - for char in string_list[i]:
            - if char not in VOWELS:
                - temp_string += char

        - string_list[i] = temp_string
        - temp_string = ''
3. return string_list

Notes:
- My version worked, but I think the LS version is definitely better.


### How Long Are You?
Write a function that takes a string as an argument and returns a list that
contains every word from the string, with each word followed by a space and the
word's length. If the argument is an empty string or if no argument is passed,
the function should return an empty list.

You may assume that every pair of words in the string will be separated by a
single space.

- Input: A string
- Output: A list containing every word from the string, with each word followed
    by a space and the word's length

Rules:
- Explicit:
    - Every pair of words will be separated by a space
    - If the argument is an empty string or if no argument is passed, the
        function should return an empty list.
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to append to and return

Programmatic Algorithm:
1. Start
    - define function 'word_lengths(str='')'
2. if string:
    - word_list = string.split(' ')
2. for i in range(len(word_list)):
        - word_list[i] = word_list[i] + ' ' + str(len(word_list[i]))
3. return word_list
4. return []


Notes:
- Did the above at first, but wanted to use an f-string, so I reformatted to
  the current version.


### List Element Multiplication
Given two lists of integers of the same length, return a new list where each
element is the product of the corresponding elements from the two lists.

- Input: Two lists of integers of the same length
- Output: A new list where each element is the product of the corresponding
    elements from the two lists

Rules:
- Explicit:
    - Must return a new list
- Implicit:
    - Lists cannot be empty

Questions:
- None

Data Structures:
- A list to append to and return

Programmatic Algorithm:
1. Start
    - define function 'multiply_items'
    - return [[list1[i] * list2[i] for i in range(len(list1))]

Notes:
- I think my solution is good, but I also think the use of zip() in the LS
    solution was nice.


### Sum of Sums
Write a function that takes a list of numbers and returns the sum of the sums of
each leading subsequence in that list. Examine the examples to see what we mean.
You may assume that the list always contains at least one number.

- Input: A list of numbers
- Output: An integer that is the sum of the sums of each leading subsequence in
    that list

Rules:
- Explicit:
    - The list always contains at least one number.
- Implicit:
    - None

Questions:
- None

Data Structures:
- None

Programmatic Algorithm:
1. Start
    - define function 'sum_of_sums'
    - total_sum = 0
2. for i in range(len(numbers)):
        - total_sum += sum(numbers[:i + 1])
3. return total_sum

Notes:
- I think my solution is just as good as the LS solution.


### Sum of Digits
Write a function that takes one argument, a positive integer, and returns the
sum of its digits.

- Input: A positive integer
- Output: An integer that is the sum of all digits in the original integer

Rules:
- Explicit:
    - Integer is always positive
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to store, sum, and return values

Programmatic Algorithm:
1. Start
    - define function 'sum_digits'
2. return sum([int(char) for char in str(number)])

Notes:
- Getting better at these one-liners.


### Staggered Case (Part 1)
Write a function that takes a string as an argument and returns that string with
a staggered capitalization scheme. Every other character, starting from the
first, should be capitalized and should be followed by a lowercase or
non-alphabetic character. Non-alphabetic characters should not be changed, but
should be counted as characters for determining when to switch between upper and
lower case.

- Input: A string
- Output: A string with every other character capitalized

Rules:
- Explicit:
    - Every other character, starting from the first, should be capitalized and
        should be followed by a lowercase or non-alphabetic character.
    - Non-alphabetic characters should not be changed, but should be counted as
        characters for determining when to switch between upper and lower case.
- Implicit:
    - None

Questions:
- None

Data Structures:
- A new string

Programmatic Algorithm:
1. Start
    - define function 'staggered_case'
    - string = string.lower()
    - staggered_string = ''
2. for i in range(len(string)):
        - if i % 2 == 0:
            - staggered_string += string[i].upper()
        - else:
            - staggered_string += string[i]
3. return staggered_string

Notes:
- My solution is okay, but I should get more practice working with enmuerate().


### Staggered Case (Part 2)
Modify the function from the previous exercise so it ignores non-alphabetic
characters when determining whether it should uppercase or lowercase each letter.
The non-alphabetic characters should still be included in the return value; they
just don't count when toggling the desired case.

- Input: A string
- Output: A string with every other character capitalized, ignoring
    non-alphabetic characters

Rules:
- Explicit:
    - Non-alphabetic characters should still be included in the return value
- Implicit:
    - None

Questions:
- None

Data Structures:
- A counter to keep track of upper/lower

Programmatic Algorithm:
1. Start
    - define function 'staggered_case'
    - staggered_string = ''
    - count = 0
2. for each character in string:
    - if the character is alphabetical:
        - add 1 to count
        - if the count mod 2 is 0:
            - staggered_string plus equals the lowercase character
        - else:
            - staggered_string plus equals the uppercase character
    - else:
        - add the character to staggered_string
3. return staggered_string

Notes:
- My solution is basically the same as the LS solution. I thought of using a
  boolean to flip between upper and lower, but I couldn't think of how to flip
  it back and forth in the moment and so I opted to use a counter instead.
  Looking at the `upper = not upper` in their code, makes me wonder how I
  overlooked something so simple.

  Edit: Reformatted one section to be a single if/else line, instead of having
  it take up multiple lines.


### Remove Consecutive Duplicates
Given a sequence of integers, filter out instances where the same value occurs
successively, retaining only the initial occurrence. Return the refined sequence.

- Input: A list of numbers
- Output: A list of numbers that contains no consecutive duplicates

Rules:
- Explicit:
    - Duplicates can still be present in the final list, just not if they are
        consecutive
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to append to and return
- A variable to track the previous number

Programmatic Algorithm:
1. Start
    - define function 'unique_sequence'
    - new_nums = []
    - previous_num = -1
2. for num in numbers:
        - if num != previous_num:
            - append num to new_nums
            - previous_num = num
3. return new_nums

Notes:
- My solution is fine, but again, I like the enumerate solution that LS used.


### Countdown
Our countdown to launch isn't behaving as expected. Why? Change the code so that
our program successfully counts down from 10 to 1 before launching.

Notes:
- `decrease(counter)`` ==> `counter = decrease(counter)``


### Reverse a String
You have a function that is supposed to reverse a string passed as an argument.
However, it's not producing the expected output. Explain the bug, and provide a
solution.

Notes:
- `string = char + string` is concatenating each character in the string to the
  front of the string, so you end up with ollehhello. I would just create a new
  variable and iterate over the reverse sliced string and concatenate each
  character that way. Or just return the reverse slice of the string from the
  get go, like LS solution #2.


### Multiply List
You want to multiply all elements of a list by 2. However, the function is not
returning the expected result. Explain the bug, and provide a solution.

Notes:
- The problem here arises from modifying the `item` variable, which isn't the
  actual list element. Swapping to a range function and modifying each index
  works.


### Key Check
You have a function that should check whether a key exists in a dictionary and
returns its value. However, it's raising an error. Why is that? How would you
fix this code?

Notes:
- An easy debug. I checked with the `in` operator, but you can also use
  .get(key, None). I believe it's throwing an error because, it's not checking
  whether the key exists, but rather, it's checking for the value of a key that
  doesn't exist.


### Calendar Event Checker
We have a list of events and want to check whether a specific date is available
(i.e., no events planned for that date). However, the function always returns the
wrong value.

Notes:
- Kind of a weird debug.. You just swap the `True` and `False` to make it work.
  Although, `return date not in events` looks better imo.


### Mutable Default Arguments
We want to create a function that appends a given value to a list. However, the
function seems to be behaving unexpectedly:

Notes:
- I've not seen this interaction before. It looks like what's happening is that
  the default parameter is not reset each time the function is called?

  Edit: Upon checking the LS discussion, that's precisely what is happening.
  "In Python, *mutable* default arguments are shared between function calls. This
  means that if you modify the default argument, its state will persist across
  function calls."


### Shadow
We defined a function intending to multiply the sum of numbers by a factor.
However, the function raises an error. Why? How would you fix this code?

Notes:
- The problem is that the function is the same name as a built in function, and
  so the interpreter(?) thinks you're trying to pass too many arguments into the
  built-in `sum()` function.


### Copy Issues
We have a list of lists and want to duplicate it. After making the copy, we
modify the original list, but the copied list also seems to be affected:

Notes:
- `copy.copy()` only copies the outermost object, so the nested lists are still
  the original objects. Using `copy.deepcopy()` fixes this.


### Set Modifications
We want to remove certain items from a set while iterating over it, but the code
below throws an error. Why is that and how can we fix it?

Notes:
- Apparently you can't change the size of a set while iterating over it.
  Similarly to how lists have list comprehension, sets of set comprehension,
  and this can be used to solve the problem.


### List Deduplication
A developer is trying to remove duplicates from a list. They use a set for
deduplication, but the order of elements is lost. How can we preserve the order?

Notes:
- William Pognonec had an interesting solution. He used the inherent uniqueness
  of dictionary keys by creating a new dictionary with the `.fromkeys()` method
  and simply coerced it to a list.


### Rotation (Part 1)
Write a function that rotates a list by moving the first element to the end of
the list. Do not modify the original list; return a new list instead.

If the input is an empty list, return an empty list.
If the input is not a list, return None.
Review the test cases below, then implement the solution accordingly.

- Input: An object?
- Output: If the input is a list, return a rotated list, or else, return None

Rules:
- Explicit:
    - If the input is an empty list, return an empty list.
    - If the input is not a list, return None.
    - Do not modify the original list.
- Implicit:
    - None

Questions:
- None

Data Structures:
- A copy of a list

Programmatic Algorithm:
1. Start
    - import copy
    - define function 'rotate_list'
2. if something is a list:
        - if the length of something is > 0:
            - rotated_list = something.deepcopy()
            - pop idx 0 from rotated_list and append to end of list
            - return rotated_list
        - return []
3. return None

Notes:
- My solution was fine, but I did like the LS solution. It looks much cleaner.


### Rotation (Part 2)
Write a function that rotates the last count digits of a number. To perform the
rotation, move the first of the digits that you want to rotate to the end and
shift the remaining digits to the left.

- Input: An integer and an index
- Output: The integer with the negative index at the end

Rules:
- Explicit:
    - None
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to convert, pop, join, and return

Programmatic Algorithm:
1. Start
    - define function 'rotate_rightmost_digits'
2. stringify number
3. listify number
4. pop negative index of list and append to list
5. join list
6. coerce string to int
7. return new number

Notes:
- The LS solution seems a bit convoluted.


### Rotation (Part 3)
Take the number 735291 and rotate it by one digit to the left, getting 352917.

Next, keep the first digit fixed in place and rotate the remaining digits to get
329175. Keep the first two digits fixed in place and rotate again to get 321759.
Keep the first three digits fixed in place and rotate again to get 321597.

Finally, keep the first four digits fixed in place and rotate the final two
digits to get 321579. The resulting number is called the maximum rotation of the
original number.

Write a function that takes an integer as an argument and returns the maximum
rotation of that integer. You can (and probably should) use the
rotate_rightmost_digits function from the previous exercise.

- Input: A number
- Output: The maximum rotation of the input number

Rules:
    - Just move each index to the end, one at a time

Questions:
- None

Data Structures:
- A list to pop and append to, and return

Programmatic Algorithm:
1. Start
    - define function 'max_rotation'
2. for i in range length of number list:
        - pop number_list[i] and append to number_list
3. maximum rotation = the joined list coerced to an int
4. return maximum_rotation

Notes:
- The explanation for this rotation problem is unreasonably over-complex. All
  you're doing is moving each index to the end. There's no point in even using
  the previous function.

  That being said, I wrote a second version to fit what LS did, just because.


### Stack Machine Interpretation
Write a function that implements a miniature stack-and-register-based
programming language that has the following commands (also called operations or
tokens):

n: Place an integer value, n, in the register. Do not modify the stack.
PUSH : Push the current register value onto the stack. Leave the value in the
register.

ADD : Pop a value from the stack and add it to the register value, storing the
result in the register.

SUB : Pop a value from the stack and subtract it from the register value, storing
the result in the register.

MULT : Pop a value from the stack and multiply it by the register value, storing
the result in the register.

DIV : Pop a value from the stack and divide the register value by the popped
stack value, storing the integer result back in the register.

REMAINDER : Pop a value from the stack and divide the register value by the
popped stack value, storing the integer remainder of the division back in the
register.

POP : Remove the topmost item from the stack and place it in the register.

PRINT : Print the register value.

All operations are integer operations (which is only important with DIV and
REMAINDER).

Programs will be supplied to your language function via a string argument. Your
function may assume that all arguments are valid programs -- i.e., they will not
do anything like trying to pop a non-existent value from the stack, and they
won't contain any unknown tokens.

Initialize the stack and register to the values [] and 0, respectively.

- Input: A string of operations and values
- Output: The corresponding input operations, values, etc.

Rules:
- See above

Questions:
- Are integer values in the string just being assigned to the register?

Data Structures:
- A list to store the split string and iterate over elements

Programmatic Algorithm:
1. Start
    - define function 'minilang'
    - string_list = split input string
    - stack = []
    - register = 0
2. for i in range(len(string_list)):
    - match string_list[i]:
        - case 'PUSH':
            - stack.append(register)
        - case 'POP':
            - register = stack.pop()
        - case 'ADD':
            - register += stack.pop()
        - case 'SUB':
            - register -= stack.pop()
        - case 'MULT':
            - register *= stack.pop()
        - case 'DIV':
            - register //= stack.pop()
        - case 'REMAINDER':
            - register %= stack.pop()
        - case 'PRINT':
            - print(register)
        - case _:
            - register = int(string_list[i])
Notes:
- Once I fully understood the explanation it was easy to solve. Originally I
  did a `for i in range()` loop and used the length of the listified string
  object, but changed it after seeing the LS solution. It was basically the
  exact same as mine, just with one less line of code.


### Word to Digit
Write a function that takes a string as an argument and returns that string with
every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four',
'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit
character.

You may assume that the string does not contain any punctuation.

- Input: A string
- Output: A string with words that are numbers replaced by numbers

Rules:
- Explicit:
    - String has no punctuation
- Implicit:
    - Rest of the string stays the same

Questions:
- None

Data Structures:
- A dictionary for the numbers

Programmatic Algorithm:
1. Start
    - define function 'word_to_digit'
    - new_string = ''
    - NUMBERS = {
        'one': '1',
        'two': '2',
        ...
    }
2. for word in string.split():
    - if word in NUMBERS:
        - new_string += f' {NUMBERS[word]}'
    - else:
        - f' {word}'
3. return new_string.lstrip()

Notes:
- Pretty simple. Refactored to a one liner after solving.

  Further exploration: Wasn't really sure how I could solve this using regex
  without a lot of extra work, and it didn't seem worth it to be honest.


### Is It Prime?
A prime number is a positive number that is evenly divisible only by itself and
1. Thus, 23 is prime since its only divisors are 1 and 23. However, 24 is not
prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. Note that the
number 1 is not prime.

Write a function that takes a positive integer as an argument and returns true
if the number is prime, false if it is not prime.

You may not use any of Python's add-on packages to solve this problem. Your task
is to programmatically determine whether a number is prime without relying on
functions that already do that for you.

- Input: A number
- Output: True or False, based on whether or not the number is prime

Rules:
- Explicit:
    - Determine whether a number is prime without relying on functions that
        already do that for you
- Implicit:
    - None

Questions:
- Are the underscores supposed to be commas?

Data Structures:
-

Programmatic Algorithm:
1. Start
    - define function 'is_prime'
    - PRIMES = [2, 3, 5, 7]
    - number = int(number)
2. if number == 1:
        return False
3. if number not in PRIMES:
    - for prime in PRIMES:
        - if number % prime == 0:
            - return False
4. return True

Notes:
- Does not work for larger numbers like 999,998,727,899,993. LS solution works
  for all numbers


### Fibonacci Numbers (Procedural)
The Fibonacci series is a sequence of numbers in which each number is the sum of
the previous two numbers. The first two Fibonacci numbers are 1 and 1. The third
number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth
is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:

```Python
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)
```
Write a function called fibonacci that computes the nth Fibonacci number, where
nth is an argument passed to the function:


- Input: A number
- Output: Its fibonacci number

Rules:
- Explicit:
    - Doesn't use recursion
- Implicit:
    - None

Questions:
- None

Data Structures:
- Just a simple for loop.

Programmatic Algorithm:
1. Start
    - define function 'fibonacci'
    - f1 = 1
    - f2 = 1
    - n = 0
2. if number > 2:
        - for _ in range(number - 2):
        - n = f1 + f2
        - f1 = f2
        - f2 = n
    - return n
3. return 1

Notes:
- Not too hard. Although I'd like to use recursion. I assume that's next though.


### Fibonacci Numbers (Recursion)
In the previous exercise, we developed a procedural solution for computing the
nth Fibonacci number.

This sequence can also be computed using a recursive function. A recursive
function is one in which the function calls itself. For example, the following
function is a recursive function that computes the sum of all integers between 1
and n:

```Python
def sum_recursive(n):
    if n == 1:
        return 1

    return n + sum_recursive(n - 1)
```

Recursive functions are a bit difficult to understand for novice programmers,
but it's worth putting in a little time early on to see what recursion looks
like. Recursion can, in some situations, greatly simplify some algorithms.

A recursive function has three primary qualities:

It must have a base case. This is a condition that tells the function to stop
recursing and begin the process of returning to the first call to the function.
This is often the simplest case - the condition for which you already know the
answer. In sum_recursive, the base case occurs when n == 1. At this point, we
know the answer: sum_recursive(1) == 1. Thus, we can return the value 1.
The function must call itself except when handling the base case.
Each recursive call must be "closer" to the base case than the current call. For
instance, in sum_recursive(3), we call sum_recursive(2), which is closer to the
base case. Likewise, sum_recursive(2) subsequently calls sum_recursive(1), which
is the base case.
You may recall from the previous exercise that the Fibonacci sequence follows a
simple set of rules:

```Python
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)
```

If you study this set of rules, you can see that the algorithm is defined
recursively:

The base case occurs when the argument is 1 or 2; both of these arguments result
in a value of 1.
The Fibonacci function calls itself. In fact, it calls itself twice.
Except when dealing with the base case, each call to the Fibonacci function
comes closer to the base case. In this case, both F(n - 1) and F(n - 2) are
closer to the base case than F(n).
Given this recursive algorithm, try to write a recursive function that computes
the nth Fibonacci number, where nth is an argument passed to the function.

- Input: A number
- Output: Its fibonacci number

Rules:
- Explicit:
    - Use recursion
- Implicit:
    - None

Questions:
- None

Data Structures:
- None

Programmatic Algorithm:
1. Start
    - define function 'fibonacci'
2. if number <= 2:
        - return 1
3. return fibonacci(number - 1) + fibonacci(number - 2)

Notes:
- Was honestly pretty easy, but mostly due to the instructions, which remind you
  that the Fibonacci sequence rules are:
  F(1) = 1
  F(2) = 1
  F(n) = F(n - 1) + F(n - 2)    (where n > 2)


### Fibonacci Numbers (Memoization)
For this exercise, your objective is to refactor the recursive fibonacci
function to use memoization.

- Input: A number
- Output: It's fibonacci number

Rules:
- Explicit:
    - Use memoization to speed up the recursion
- Implicit:
    - None

Questions:
- I'm not really sure I understand the problem in its entirety, or rather, if my
  solution is considered recursive. Although, I'm using a dictionary, and it
  does talk about saving the data in an object...

Data Structures:
- A dictionary to store key:value pairs

Programmatic Algorithm:
1. Start
    - FIBS = {
        1: 1,
        2: 1,
    }
    - define function 'fibonacci'
    - while number not in fibs:
        - fibs[len(fibs) + 1] = fibs[len(fibs)] + fibs[len(fibs) - 1]
    - return fibs.get(number)

Notes:
- My method was still procedural. I wasn't 100% clear on what LS meant until I
  I saw their solution. In any case, I created another procedural version, so
  it was still good practice.


### Fibonacci Number Location By Length
As we've seen in the last few exercises, the Fibonacci series is a
computationally simple series, However, the results grow at an incredibly rapid
rate. For example, the 100th Fibonacci number is 354,224,848,179,261,915,075 --
that's enormous, especially considering that it takes six iterations just to
find the first 2-digit Fibonacci number.

Write a function that calculates and returns the index of the first Fibonacci
number that has the number of digits specified by the argument. The first
Fibonacci number has an index of 1. You may assume that the argument is always
an integer greater than or equal to 2.

- Input: A number
- Output: The index of the first Fibonacci number that has the number of digits
    specified by the argument

Rules:
- Explicit:
    - Argument is always an integer greater than or equal to 2
- Implicit:
    - None

Questions:
- None

Data Structures:
- A while loop to get looping until we hit our goal

Programmatic Algorithm:
1. Start
    - sys.set_int_max_str_digits(50_000)
    - f1 = 1
    - f2 = 1
    - n = 2
2. while len(str(f2)) < length:
        - count += 1
        - n = f1 + f2
        - f1 = f2
        - f2 = n
3. return count

Notes:
- Curious to know if this is possible to do with recursion or if it's simply too
  memory intensive.


### Lettercase Percentage Ratio
Write a function that takes a string and returns a dictionary containing the
following three properties:

・The percentage of characters in the string that are lowercase letters
・The percentage of characters that are uppercase letters
・The percentage of characters that are neither
All three percentages should be returned as strings whose numeric values lie
between "0.00" and "100.00", respectively. Each value should be rounded to two
decimal points.

You may assume that the string will always contain at least one character.


- Input: A string
- Output: A dictionary containing the percentages of characters that are
    lowercase letters, uppercase letters, and the percentage of characters that
    are neither

Rules:
- Explicit:
    - The string will always contain at least one character.
- Implicit:
    - Spaces count as characters

Questions:
- None

Data Structures:
- A dictionary to hold key:value pairs and return

Programmatic Algorithm:
1. Start
    - define function 'letter_percentages'
    - percentage_dict = {}
    - count_dict = {
        'lowercase': 0,
        'uppercase': 0,
        'neither': 0,
    }
    - str_length = len(string)
2. for character in string:
        - if character.isalpha() and character == character.lower():
            - count_dict['lowercase'] += 1
        - elif character.isalpha() and character == character.upper():
            - count_dict['uppercase'] += 1
        - else:
            - count_dict['neither'] += 1
4. percentage_dict['lowercase'] = (count_dict['lowercase'] / str_length) * 100
5. percentage_dict['uppercase'] = (count_dict['uppercase'] / str_length) * 100
6. percentage_dict['neither'] = (count_dict['neither'] / str_length) * 100
7. return percentage_dict

Notes:
- Pretty simple. Used format mini-lang for the formatting. Probably some
  unnecessary code in the if statements, but i's not a big deal.


### Triangle Sides
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must be
greater than the length of the longest side, and every side must have a length
greater than 0. If either of these conditions is not satisfied, the triangle is
invalid.

Write a function that takes the lengths of the three sides of a triangle as
arguments and returns one of the following four strings representing the
triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

- Input: Three numbers
- Output: A string denoting the type of triangle the numbers are

Rules:
- Explicit:
    - To be a valid triangle, the sum of the lengths of the two shortest sides
        must be greater than the length of the longest side and every side must
        have a length greater than 0
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to sort the numbers and validate side lengths
- A set to check triangle type

Programmatic Algorithm:
1. Start
    - define function 'triangle'
    - side_list = sorted([num1, num2, num3])
2. if sum(side_list[:2]) <= side_list[2]:
        - return 'invalid'
3. triangle_set = set(side_list)
4. if len(triangle_set) == 3:
        - return 'scalene'
5. elif len(triangle_set) == 2:
        - return 'isosceles'
6. else:
        - return equilateral


Notes:
- Did a slight refactoring and used a helper function for best practices(?).
  Overall, simple solve.


### Tri-Angles
A triangle is classified as follows:

Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.
To be a valid triangle, the sum of the angles must be exactly 180 degrees, and
every angle must be greater than 0. If either of these conditions is not
satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments and
returns one of the following four strings representing the triangle's
classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have to worry
about floating point errors. You may also assume that the arguments are in
degrees.

- Input: Three numbers that are the degrees of each angle in a triangle
- Output: A string denoting the type of triangle the numbers are

Rules:
- Explicit:
    - To be a valid triangle, the sum of the angles must be exactly 180 degrees,
        and every angle must be greater than 0
    - Assume that all angles have integer values, so you do not have to worry
        about floating point errors.
    - You may also assume that the arguments are in degrees.
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to hold the numbers

Programmatic Algorithm:
1. Start
    - define function 'trianlge'
    - angle_list = [num1, num2, num3]
2. define function 'is_valid'
        - for angle in angle_list:
            - if angle == 0:
                - return False
        - if sum(angle_list) == 180:
            - return True
        - return False
3. if is_valid(angle_list):
    for angle in angle_list:
        if angle == 90:
            return 'right'
        elif angle > 90:
            return 'obtuse'
    return 'acute'
4. return 'invalid'

Notes:
- Quick solve

### Unlucky Days
Some people believe that Fridays that fall on the 13th day of the month are
unlucky days. Write a function that takes a year as an argument and returns the
number of Friday the 13ths in that year. You may assume that the year is greater
than 1752, which is when the United Kingdom adopted the modern Gregorian
Calendar. You may also assume that the same calendar will remain in use for the
foreseeable future.

- Input: A number representing a year
- Output: The number of Friday the 13ths in that year

Rules:
- Explicit:
    - Assume that the year is greater than 1752
    - Assume that the same calendar will remain in use for the foreseeable
        future.
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to hold days of the week

Programmatic Algorithm:
1. Start
    - import datetime
    - DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']
    - THIRTEENTH = 13
    - define function 'friday_the_13ths'
    - counter = 0
    - month = 1
2. while month <= 12:
        - if datetime.date(year, month, THIRTEENTH).weekday() == 4:
            - counter += 1
        - month += 1
3. return counter

Notes:
- Pretty simple. Just needed to watch a small clip about different datetime
  module methods to understand what I was working with. Was using a month
  variable and incrementing it with each iteration, but then I saw the LS
  solution and obviously should have just used a range, so I refactored.

### Next Featured Number Higher than a Given Value
A featured number (something unique to this exercise) is an odd number that is a
multiple of 7, with all of its digits occurring exactly once each. For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next featured number greater than the integer. Issue an error message if there is no next featured number.

NOTE: The largest possible featured number is 9876543201.

- Input: A number
- Output: The next *featured number*

Rules:
- Explicit:
    - An odd number that is a multiple of 7
    - All of its digits occurring exactly once each
- Implicit:
    - None

Questions:
- None

Data Structures:
- A list to check length, etc.
- A set to compare length against the featured number

Programmatic Algorithm:
1. Start
    - define function 'next_featured'
    - featured_number = number
2. while not is_valid(featured_number):
        - featured_number = add_seven(number)
3. define function 'add_seven'
        return number + 7
4. define function 'is_valid'
        - if number % 2 == 0:
            - return False
        - string_num = str(number)
        - set_num = set(string_num)
        - if len(string_num) != len(set_num):
            - return False
        - return True
Notes:
- I opted to add both add_one() and add_seven() helper functions to speed up
  the computing, as if I simply started at 0 and added 7 it would take a while.
  This way, I start at the number, wait for it to be divisible by 7, and then,
  because I know it's a multiple of 7, I can start adding seven from there.

  Seeing the LS solution, the 14 trick makes a lot of sense. Wish I'd thought
  of that.


### Sum Square - Square Sum
Write a function that computes the difference between the square of the sum of
the first count positive integers and the sum of the squares of the first count
positive integers.

- Input: A number
- Output: A number that is the difference between the square of the sum of the
    first count positive integers and the sum of the squares of the first count
    positive integers

Rules:
- Explicit:
    - None
- Implicit:
    - None

Questions:
- None

Data Structures:
- A range

Programmatic Algorithm:
1. Start
    - define function 'sum_square_difference'
    - square_sum = (sum(range(number))) ** 2
    - sum_square = 0
2. for i in range(number):
        - sum_square += i ** 2

Notes:
- Refactored sum_square to a one liner with list comprehension.


### Bubble Sort
Bubble Sort is one of the simplest sorting algorithms available. It is not an
efficient algorithm, so developers rarely use it in real code. However, it is an
excellent exercise for student developers. In this exercise, you will write a
function that sorts a list using the bubble sort algorithm.

A bubble sort works by making multiple passes (iterations) through a list. On
each pass, the two values of each pair of consecutive elements are compared. If
the first value is greater than the second, the two elements are swapped. This
process is repeated until a complete pass is made without performing any swaps.
At that point, the list is completely sorted.


- Input: A list
- Output: The sorted list

Rules:
- Explicit:
    - Must bubble sort
- Implicit:
    - List can be strings
    - Must mutate the original list

Questions:
- None

Data Structures:
-

Programmatic Algorithm:
1. Start
    - define function 'bubble_sort'
2. while True:
        - for i in range(len(numbers) - 1):
            - if things[i] > things[i + 1]:
                - greater = things[i]
                - lesser = things[i + 1]
                - things[i] = lesser
                - things[i + 1] = greater
        - if is_sorted(things):
            - break
3. def is_sorted(things):
        - for i in range(len(things) - 1):
            - if things[i + 1] < things[i]:
                - return False
        - return True

Notes:
- I used a helper function to check if the list was sorted, but I like the
  method that LS used with the `swapped` variable.


### Transpose 3x3 Matrix
A 3x3 matrix can be represented by a list of nested lists: an outer list that
contains three sub-lists that each contain three elements.

The transpose of a 3x3 matrix is the matrix that results from exchanging the
rows and columns of the original matrix.

Write a function that takes a list of lists that represents a 3x3 matrix and
returns the transpose of the matrix. You should implement the function on your
own, without using any external libraries.

Take care not to modify the original matrix -- your function must produce a new
matrix and leave the input matrix list unchanged.

- Input: A 3x3 matrix (A list containing 3 nested lists with 3 elements each)
- Output: The transposition of the input matrix

Rules:
- Explicit:
    - Do not modify the original list
    - Do not use external libraries
- Implicit:
    - The input list will always be a matrix

Questions:
- None

Data Structures:
- A list with 3 nested lists

Programmatic Algorithm:
1. Start
    - define function 'transpose'
    - new_matrix = [[], [], []]
2. for item in matrix:
        - for idx, value in enumerate(item):
            - new_matrix.append(value)
3. return new_matrix

Notes:
- My solution is okay, but I don't like the creation of a new empty matrix
  beforehand. It feels like cheating. Because of this, I decided to try and
  refactor to a one liner since I knew it was possible, but I got stuck and
  couldn't figure out what was wrong. I was getting
  `[[1], [5], [8], [4], [7], [2], [3], [9], [6]]` and my code was
  `[[item[i]] for item in matrix for i in range(len(matrix))]`. Turns out I just
  needed to move the bracket slightly further to the right...


### Transpose MxN Matrix
In the previous exercise, you wrote a function that transposed a 3x3 matrix
represented by a list of lists.

Matrix transposes are not limited to 3x3 matrices, or even square matrices. Any
matrix can be transposed simply by switching columns with rows.

Modify your transpose function from the previous exercise so that it works with
any MxN matrix with at least one row and one column.

- Input: A matrix
- Output: The transposition of the input matrix

Rules:
- Explicit:
    - Do not modify the original list
    - Do not use external libraries
- Implicit:
    - The input list will always be a matrix

Questions:
- None

Data Structures:
- A list with as many nested lists as there are elements in each nested list of
    the input matrix

Programmatic Algorithm:
1. Same as last solution, except:
2. new_matrix = []
3. for _ in range(len(matrix[0])):
        - new_matrix.append([])

Notes:
- The same as the last problem basically. The difference in the one liner is
  that, in the previous solution I used `range(len(matrix))` but since we want
  the length of the items instead of either of the two (since it's no longer
  square), we just add an index to make it `range(len(matrix[0]))`.


### Rotating Matrices
As we saw in the previous exercises, a matrix can be represented by a list of
lists.

A 90-degree rotation of a matrix produces a new matrix in which each side of the
matrix is rotated clockwise by 90 degrees.

A 90-degree rotation of a non-square matrix is similar.

Write a function that takes an arbitrary MxN matrix, rotates it clockwise by
90-degrees as described above, and returns the result as a new matrix. The
function should not mutate the original matrix.

Notes:
- This is the same as the last one, you just throw a negative slice in and call
  it a day.


### Merge Sorted Lists
Write a function that takes two sorted lists as arguments and returns a new list
that contains all the elements from both input lists in ascending sorted order.
You may assume that the lists contain either all integer values or all string
values.

You may not provide any solution that requires you to sort the result list. You
must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.

- Input: Two lists
- Output: A list containing all elements from the previous to lists, but sorted

Rules:
- Explicit:
    - Not allowed to sort the final list
    - All elements must be placed into the list one at a time
    - Assume that the lists contain either all integer values or all string
        values
- Implicit:
    - An input list can be empty

Questions:
- None

Data Structures:
- A list

Programmatic Algorithm:
1. Start
    - define function 'merge(list1, list2)'
2. for each index in list1 and list2
3. if the item at the index is less than every other item
4. append it to a new list
5. and delete it from the old list


Notes:
-

