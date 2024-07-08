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