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