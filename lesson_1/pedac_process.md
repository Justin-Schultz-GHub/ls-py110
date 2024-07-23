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