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
    to drill in the fact that sets can hold only unique values, but a list, etc.
    works as well since you're only checking if the element is in the collection.

