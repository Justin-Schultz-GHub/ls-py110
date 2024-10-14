### Tic Tac Toe Attack Square

Algorithm:
If the computer has markers in 2 squares and the 3rd is empty, mark that square

If not, check if the player has markers in 2 squares. If it does, and the 3rd is
empty, mark that square

if neither of these are possible, check square 5. If it's empty, mark it

If the computer has markers on at least 1 square, and the player has no markers
on the other squares, mark a square


### Twenty One
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
   - repeat until bust or stay
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.


### Count Unique Pairs

- Input: String
- Output: An integer signifying how many unique pairs of letters there are in
    the string

Rules:
- Explicit:
    - A pair unique letter is when two different letters appear in sequence
- Implicit:
    - Strings are at least one character long

Programmatic Algorithm:
- pair_substrings = []
- unique_pairs = []
- for every letter in our string, up until the second to last letter, add letter,
    and the next letter following it, to our pair_substrings list
- for each pair in pair_substrings
    - if pair[0] != pair[1]:
        - add to unique_pairs
- return len(unique_pairs)


### Expanded Form

- Input: An integer
- Output: The string representation of the expanded form of said integer

Rules:
- Explicit:
    - All numbers are whole and greater than 0


Programmatic Algorithm:
- numbers = list(str(num))
- for i in range(len(numbers) + 1, 0, -1:
    - numbers i


Notes:
-


### Every Third

- Input: A list and a starting index
- Output: A list with every third element from the starting index, including the
    element at the starting index


Data Structures:
- A list to append to and return

Programmatic Algorithm:
1. Start
    - def function 'every_third(lst, start)'
    - sliced_list = lst[start:]
    - thirds_list = []

2. thirds_list.append(sliced_list[0])
3. for index, element in enumerate(sliced_list):
    if index % 3 == 0:
        thirds_list.append(element)
4. return thirds_list


Notes:
-



### Expanded Form

- Input: An integer
- Output: A string representation of the expanded for of said integer

Rules:
- Explicit:
    - All numbers will be whole numbers greater than 0

Data Structures:
- A string, maybe a list

Programmatic Algorithm:
1. Start
    - def function 'expanded_form'
    - str_num = str(num)
    - numbers_list = []
2. for i in range(len(str_num)):
    - if str_num[i] != '0':
        - append the current index, plus as many zeroes as the length, minus the
        value of i + 1
3. return the joined list with addition signs and spaces.


Notes:
- Tricky because the 0's get ignored


### Split Strings

- Input: A string
- Output: A list of two character substrings from the original string

Rules:
- Explicit:
    - If the string contains an odd number of characters then it should replace
        the missing second character of the final pair with an underscore ('_').

Data Structures:
- A list to append to and return

Programmatic Algorithm:
1. Start
    - def function 'solution'
    - char_pairs = []
2. for index, char in enumerate(s):
        if indx % 2 == 0 and index != len(s) - 1:
            char_pairs.append(s[i:i + 2])
        elif  i % 2 == 0 and index == len(s) - 1:
            char_pairs.append(s[i] + '_')
3. return char_pairs

Notes:
- Since it only needs to have an underscore if the length of the string is odd,
  just checking the length of the string at the start is probably the simplest.
  If its length is odd, you just add an underscore to the end of the string
  before iterating.


### Moving Zeros To The End
Write an algorithm that takes a list and moves all of the zeros to the end,
preserving the order of the other elements.

- Input: A list of integers
- Output: A list of the same numbers, with the zeroes moved to the end

Rules:
- Explicit:
    - The order of the other elements must be preserved
- Implicit:
    - The list is never empty

Programmatic Algorithm:
1. Start
    - def function 'move_zeros'
2. zeroes = lst.count(0)
3. while 0 in lst:
    lst.pop(lst.index(0))
5. for _ in range(zeroes):
    lst.append(0)
6. return lst

Notes:
- Interestingly, someone had this as a solution on CodeWars:
```Python
def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array
```
  It seems that .remove() functions differently from .pop() here since it
  operates on values instead of indexes, which allows it to properly handle the
  removal and appends without skipping indexes.


### Create Phone Number
Write a function that accepts a list of 10 integers (between 0 and 9), that
returns a string of those numbers in the form of a phone number.

- Input: A list of 10 integers (between 0 and 9)
- Output: A string representation of those numbers as a phone number


Programmatic Algorithm:
1. Start
    - def function 'create_phone_number'
    - str_nums = ''.join([str(num) for num in numbers])

    return f'({str_nums[0:3]}) {str_nums[3:6]}-{str_nums[6:10]}'


Notes:
- The Code Wars top solution was really clever. It even works if there are too
  many integers in the list, using only the first 10.


### Consecutive Strings

- Input: A list and an integer (k)
- Output: The first longest string consisting of k consecutive strings from the
    list

Rules:
- Explicit:
    - consecutive strings : follow one after another without an interruption
    - n being the length of the string array, if n = 0 or k > n or k <= 0
        return "" (return Nothing in Elm, "nothing" in Erlang).
- Implicit:
    - Consecutives don't wrap back to the beginning of the list if it reaches
        the end
    - All list elements are strings

Programmatic Algorithm:
1. Start
    - def function 'longest_consec'
    - longest_consec_len = -1
2. for i in range(len(strarr) - k):
    if len(''.join(strarr[i:i+k])) > longest_consec_len:
        longest_consec_len = len(''join(strarr[i:i+k]))
3. for i in range(len(strarr) - k):
    if len(''.join(strarr[i:i+k])) == longest_consec_len:
        return ''join(strarr[i:i+k])

Notes:
- Ended up refactoring the above algorithm because it was kind of repetetive.


### Count the smiley faces!
Given a list (lst) as an argument complete the function count_smileys that,
should return the total number of smiling faces.

- Input: A list of faces
- Output: An integer representing how many are smiley faces

Rules:
- Explicit:
    - Valid smiley face examples: :) :D ;-D :~)
    - Invalid smiley faces: ;( :> :} :]
    - In case of an empty lst return 0.
    - Input will always be a list.
    - Order of the face (eyes, nose, mouth) elements will always be the same.
    - Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
    - A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
    - Every smiling face must have a smiling mouth that should be marked with either ) or D

Programmatic Algorithm:
1. Start
    - def function 'count_smileys'
    - VALID_EYES = [':', ';']
    - VALID_NOSES = ['-', '~']
    - VALID_MOUTHS = [')', 'D']
    - VALID_FACES = [eye + mouth
                for eye in VALID_EYES
                for mouth in VALID_MOUTHS] + [eye + nose + mouth
                for eye in VALID_EYES
                for nose in VALID_NOSES
                for mouth in VALID_MOUTHS]
    - smiley_counter = 0
2. for face in lst:
        if face in VALID_FACES:
            smiley_counter += 1

3. return smiley_counter

Notes:
- I originally used the above code, but after looking at a solution on Code Wars
  that was really similar to mine, I realized I could have just added an empty
  string to the VALID_NOSES list and removed 2+ lines of code.


### Highest Scoring Word
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet:
a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the
original string.

All letters will be lowercase and all inputs will be valid.

- Input: A string
- Output: The substring with the highest value

Rules:
- Explicit:
    - All letters are lowercase
    - If two words score the same, return the word that appeared first
- Implicit:
    - Strings have no punctuation

Data Structures:
- A dictionary to grab values (1-26) from keys (letters)

Programmatic Algorithm:
1. Start
    - define function 'high'
    - letter_value_dict = {chr(i): i - 96 for i in range(ord('a'), ord('z') + 1)}
    - substrings = [A list of words in the input string split by spaces]
    - highest_value = 0
    - high_word = ''
2. for each word in the list:
    - word_value = 0
    - for each letter in the word:
        - get its value from the dictionary and add it to word value
    - if word_value is > highest_value:
        - highest_value = word_value
        - high_word = word
3. return high_word

Notes:
- Wasn't sure how I could use a range to get a-z at first and it showed my I
  could print a-z with a similar ord/chr structure, so I just put it into a
  comprehension with slight modifications. It's quite simple after seeing it.
  Incidentally, you don't need to subtract 96 from i for the dictionary values,
  it simply looks better.


### Data Reverse
A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be
reversed, for example:

```Python
11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
```
should become:

```Python
10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
```
The total number of bits will always be a multiple of 8.

The data is given in a list as such:
```Python
[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
```

- Input: A list of numbers
- Output: That list of numbers, with each 8-bit segment reversed

Rules:
- Explicit:
    - The total number of bits will always be a multiple of 8.
- Implicit:
    - Numbers are always 1s and 0s it seems

Data Structures:
- A list of nested lists

Programmatic Algorithm:
1. Start
    - define function 'data_reverse'
    - numbers = [A list of lists, with the nested lists containing 8-bits]
    - reversed_nums = []
2. for i in range(length of numbers):
    numbers[i] = reversed(numbers[i])
3. for list in numbers:
    reversed_nums += list
4. return reversed_nums


Notes:
-


### Playing with passphrases
Everyone knows passphrases. One can choose passphrases from poems, songs, movies
names and so on but frequently they can be guessed due to common cultural
references. You can get your passphrases stronger by different means. One is the
following:

choose a text in capital letters including or not digits and non alphabetic
characters,

1. shift each letter by a given number but the transformed letter must be a
    letter (circular shift)
2. replace each digit by its complement to 9
3. keep such as non alphabetic and non digit characters
4. downcase each letter in odd position, upcase each letter in even position
    (the first character is in position 0)
5. reverse the whole result.
Example:
your text: "BORN IN 2015!", shift 1

1 + 2 + 3 -> "CPSO JO 7984!"

4 "CpSo jO 7984!"

5 "!4897 Oj oSpC"


- Input: A string and an integer
- Output: The string with each letter shifted by the integer value, and each
    number shifted by its complement to 9, with odd index lowercased, even
    indexes uppercased, and the whole string reversed

Rules:
- Implicit:
    - Strings can have punctuation
    - Integer is always positive

Questions:
-

Data Structures:
-

Programmatic Algorithm:
1. Start
    - define function 'play_pass'
    - int_shift_value = num
    - letter_shift_value = num
    - string_list = [char.lower() for char in passcode]
2. while int_shift_value > 9:
    - int_shift_value -= 9
3. for i in range(length of string_list):
    - if string_list[i] is letter:
        - letter_value = ord(string_list[i])
        - letter_value += letter_shift_value

        - while letter_value > 122
            - letter_value -= 26

        - string_list[i] = chr(letter_value)

    - if string_list[i] is integer
        - int_value = abs(int(string_list[i]) - 9)

        - string_list[i] = chr(letter_value)

    - if i % 2 == 0:
        - uppercase string_list

4. reverse string_list
5. return joined string_list


Notes:
-


###

- Input:
- Output:

Rules:
- Explicit:
    -
- Implicit:
    -

Questions:
-

Data Structures:
-

Programmatic Algorithm:
1. Start
    -


Notes:
-


### Rotation (Part 3)
Take the number 735291 and rotate it by one digit to the left, getting 352917.
Next, keep the first digit fixed in place and rotate the remaining digits to
get 329175. Keep the first two digits fixed in place and rotate again to get
321759. Keep the first three digits fixed in place and rotate again to get
321597. Finally, keep the first four digits fixed in place and rotate the final
two digits to get 321579. The resulting number is called the maximum rotation
of the original number.

Write a function that takes an integer as an argument and returns the maximum
rotation of that integer. You can (and probably should) use the
rotate_rightmost_digits function from the previous exercise.

- Input: An integer
- Output: The max rotation of that integer

Rules:
- Explicit:
    -
- Implicit:
    -

Questions:
-

Data Structures:
- A list to append to and pass to rotate_list()

Programmatic Algorithm:
1. Start
    - define function 'rotate_rightmost_digits'
    - num_str = str(num)
2. return int(num_str[:num_str[len(num_str) - (count)] + ''.join(rotate_list(list(num_str[len(num_str) - (count):]))))
3.


Notes:
-


### Egyptian Fractions
Write two functions: one that takes a Rational number as an argument, and
returns a list of the denominators that are part of an Egyptian Fraction
representation of the number, and another that takes a list of numbers in the
same format, and calculates the resulting Rational number. You will need to use
the Fraction class provided by the fractions module.

- Input: A fraction
- Output: A list of denominators that add up to the numerator of the input
    fraction when using the denominator of the input fraction as a numerator?

Rules:
- Explicit:
    - A Unit Fraction is a rational number where the numerator is 1.
    - An Egyptian Fraction is the sum of a series of distinct unit fractions
- Implicit:
    -

Questions:
-

Data Structures:
-

Programmatic Algorithm:
1. Start
    -


Notes:
-


### PY119 Practice Problems: Problem 1
Create a function that takes a list of numbers as an argument. For each number,
determine how many numbers in the list are smaller than it, and place the
answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs
multiple times in the list, it should only be counted once.


- Input: A list of numbers
- Output: A list of numbers that corresponds to how many numbers are smaller
    than each number in the input list

Rules:
- Explicit:
    - When counting numbers, only count unique values.

Data Structures:
- A list to append to and return
- A set to store values and check membership against

Programmatic Algorithm:
1. Start
    - define function 'smaller_numbers_than_current(lst)'
    - lst_set = set(lst)
    - smaller_number_list
2. for each number in the list:
    - count = 0
    - check number against all other numbers
        -
    - if other number is smaller:
        - count += 1


Notes:
-


### PY119 Practice Problems: Problem 2

- Input: A list of integers
- Output: The minimum sum of 5 consecutive numbers from the input list

Rules:
- Explicit:
    - If the list contains fewer than 5 elements, the function should return
        None.

Data Structures:
-

Programmatic Algorithm:
1. Start
    - define function 'minimum_sum(lst)'
    - my_list = []
2. for every 5 numbers, calculate the total of those numbers
3. if that total is less than current total:
    - new total = current total

4. for i in range(len(lst) - 6):
    my_list.append(lst[i:i+5])

Notes:
-


### PY119 Practice Problems: Problem 3
Create a function that takes a string argument and returns a copy of the string
with every second character in every third word converted to uppercase. Other
characters should remain the same.

- Input: A string
- Output: A new string that is the input string with every second character in
    every third word converted to uppercase

Rules:
- Explicit:
    - Other characters should remain the same
- Implicit:
    - No empty strings

Questions:
-

Data Structures:
-

Programmatic Algorithm:
1. Start
    - define function 'to_weird_case(string)
    - string_list = string.split()
2. for every 3rd word:
    - make every second character uppercase


Notes:
-



### PY119 Practice Problems: Problem 4
Create a function that takes a list of integers as an argument and returns a
tuple of two numbers that are closest together in value. If there are multiple
pairs that are equally close, return the pair that occurs first in the list.

- Input: A list of integers
- Output: A tuple containing the pair of numbers closest in value together

Rules:
- Explicit:
    - If there are multiple pairs that are equally close, return the pair that
        occurs first in the list.

Questions:
-

Data Structures:
- A list to append tuples to

Programmatic Algorithm:
1. Start
    - define function 'closest_numbers(lst)'
    - my_num = sum(lst)
    - closest_tuple =

2. for i in range(len(lst) - 1):
    - for num in lst[i:]:
        - if abs(lst[i] - num) < my_num:
            - my num = abs(lst[i] - num)
            - closest_tuple = (lst[i], num)

Notes:
- Had a problem with this that wasted a lot of time because I had my_num
  changing from an int to a bool. This happened because on the
  `my_num = abs(lst[i] - num)` line, I left the ` < my_num` when I copy pasted
  it and so it was `my_num = abs(lst[i] - num) < my_num`... Wasted a bunch of
  time debugging this and so it took me ~26 mins.



### Alphabet Symmetry
Consider the word "abode".
The letter `a` is in position 1 and `b` is in position 2.
In the alphabet, `a` and `b` are also in positions 1 and 2.

The letters `d` and `e` in "abode" occupy the positions they would occupy in the
alphabet, which are positions 4 and 5.

Given an array of words, return an array of the number of letters that occupy
their positions in the alphabet for each word. For example,

solve(["abode","ABc","xyzD"]) // [4, 3, 1]

Input will consist of alphabetic characters, both uppercase and lowercase.
No spaces.

Programmatic Algorithm:
1. Start
    - define function 'solve(lst)'
    - create an empty list called `my_list`
2. for each word in `my_list`:
    - initialize a count variable to 0
    - for each index, letter in enumerate(word):
        - if index == ord(letter.lower) - 97:
            - add one to count
    - append count to `my_list`
3. return my_list


Notes:
-


### PY119 Practice Problems: Problem 5
Create a function that takes a string argument and returns the character that
occurs most often in the string. If there are multiple characters with the same
greatest frequency, return the one that appears first in the string. When
counting characters, consider uppercase and lowercase versions to be the same.


- Input: A string
- Output: The character in the input string that occurs most frequently

Rules:
- Explicit:
    - Uppercase and lowercase characters are the same
    - If there are multiple characters with the same greatest frequency, return
        the one that appears first in the string.
- Implicit:
    - There are no empty strings in the input

Data Structures:
- A dictionary to key track of keys (characters) and their values (counts)

Programmatic Algorithm:
1. Start
    - define function 'most_common_char(string)'
    - characters = {}
2. for each character in string:
    - create key that is equal to the character, and set its value to 0
3. for each character in characters:
    - count how many of that character are in string, and assign that value to
        its corresponding key
4. return max(sorted(characters, characters.values))


Notes:
-


### PY119 Practice Problems: Problem 6
Create a function that takes a string argument and returns a dict object in
which the keys represent the lowercase letters in the string, and the values
represent how often the corresponding letter occurs in the string.

- Input: A string
- Output: A dictionary whose keys are the lowercase letters in the input string,
    and the values are their frequency in the input string

Rules:
- Explicit:
    - None
- Implicit:
    - Spaces aren't counted as characters
    - Input can be an empty string

Questions:
- None

Data Structures:
- A dictionary to hold keys (lowercase characters) and values (count)

Programmatic Algorithm:
1. Start
    - define function 'count_letters(string)'
    - letters = {}
    - my_list = list(string)
2. while ' ' in my_list:
    - my_list.remove(' ')
3. new_string = ''.join(my_list)
4. for char in new_string:
    - if char == char.lowercase():
        - letters.setdefault(char, 0)
5. for key in letters.keys():
    - letters[key] = new_string.count(key)
6. return letters

Notes:
-



### PY119 Practice Problems: Problem 7
Create a function that takes a list of integers as an argument and returns the
number of identical pairs of integers in that list. For instance, the number of
identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. For
instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2.
The first list contains two complete pairs while the second has an extra 2 that
isn't part of the other two pairs.

- Input: A list of integers
- Output: An integer representing the number of identical pairs of integers in
    the input list

Rules:
- Explicit:
    - If the list is empty or contains exactly one value, return 0.
- Implicit:
    -

Questions:
-

Data Structures:
- A dictionary to hold keys (integers) and values (counts)

Programmatic Algorithm:
1. Start
    - define function 'pairs(lst)'
    - number_pairs = {}
2. if len(lst) <= 1:
    - return 0
3. for number in lst:
    - number_pairs.setdefault(number, lst.count(number) // 2)


Notes:
-



### PY119 Practice Problems: Problem 8
Create a function that takes a non-empty string as an argument. The string
consists entirely of lowercase alphabetic characters. The function should
return the length of the longest vowel substring. The vowels of interest are
"a", "e", "i", "o", and "u".

- Input: A non-empty string made up of lowercase letters
- Output: An integer representing the length of the longest vowel substring

Rules:
- Explicit:
    - The vowels of interest are "a", "e", "i", "o", and "u".

Questions:
-

Data Structures:
- A list to hold all substrings
- A variable to hold the length

Programmatic Algorithm:
1. Start
    - define function 'longest_vowel_substring(string)'
    - substrings = [a list of all substrings in the input string]
    - max_length = 0
    - VOWELS = ['a', 'e', 'i', 'o', 'u']
2. for substring in substrings:
    - if all(substring) in VOWELS and length of substring > max_length:
        - max_length = length of substring
3. return max_length

Notes:
-



### PY119 Practice Problems: Problem 9
Create a function that takes two string arguments and returns the number of
times that the second string occurs in the first string. Note that overlapping
strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.

- Input: Two strings
- Output: An integer representing how many times the second string occurs in
    the first

Rules:
- Explicit:
    - Overlapping strings don't count: 'babab' contains 1 instance of 'bab', not
        2.
    - You may assume that the second argument is never an empty string.

Data Structures:
-

Programmatic Algorithm:
1. Start
    - define function 'count_substrings(string1, string2)'
    - return the count of string2 in string1


Notes:
- Is there an error in this problem, or is it testing our knowledge of the
  count method?


### PY119 Practice Problems: Problem 10
Create a function that takes a string of digits as an argument and returns the
number of even-numbered substrings that can be formed. For example, in the case
of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and
'2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a
separate substring.

- Input: A string of digits
- Output: An integer representing the number of even-numbered substrings in the
    input string

Rules:
- Explicit:
    - If a substring occurs more than once, you should count each occurrence as
        a separate substring.
- Implicit:
    - Never an empty string

Data Structures:
- A list to hold all substrings

Programmatic Algorithm:
1. Start
    - define function 'even_substrings(string)'
    - substrings = [all substrings in the input string]
    - count = 0
2. for each substring:
    - if int(substring[-1]) % 2 == 0:
        - count += 1
3. return count


Notes:
-



### PY119 Practice Problems: Problem 11
Create a function that takes a nonempty string as an argument and returns a
tuple consisting of a string and an integer. If we call the string argument s,
the string component of the returned tuple t, and the integer component of the
tuple k, then s, t, and k must be related to each other such that s == t * k.
The values of t and k should be the shortest possible substring and the largest
possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase
alphabetic letters.

- Input: A non-empty string
- Output: A tuple that consists of a string and integer that represent the
    shortest possible substring with the largest possible repeat count

Rules:
- Explicit:
    - You may assume that the string argument consists entirely of lowercase
        alphabetic letters.

Data Structures:
- A list to hold substrings
- Variables to hold the count, length, and string

Programmatic Algorithm:
1. Start
    - define function 'repeated_substring(string)'
    - substrings = [all substrings in string]
    - length = 0
    - count = 0
    - return_string = ''
2. for each substring in substrings:
    - if length of substring is > length, and its occurences in string are > count:
        - length = len(substring)
        - count = string.count(substring)
        - return_string = substring
3. return (return_string, count)


Notes:
-


### PY119 Practice Problems: Problem 12
Create a function that takes a string as an argument and returns True if the
string is a pangram, False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least once.
For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram
since it uses every letter at least once. Note that case is irrelevant.

- Input: A string
- Output: True or False, based on whether or not the input string is a pangram

Rules:
- Explicit:
    - Pangrams are sentences that contain every letter of the alphabet at least
        once.
    - Case is irrelevant.
- Implicit:
    - No empty input strings

Data Structures:
- A set/list to hold all values of my string
- A list of all letters

Programmatic Algorithm:
1. Start
    - define function 'is_pangram(string)'
    - ALPHABET = [all letters of the alphabet]
    - string_characters = list(set([all letters in the string]))
2. return all(letter in string_characters for letter in ALPHABET)


Notes:
-


### PY119 Practice Problems: Problem 13
Create a function that takes two strings as arguments and returns True if some
portion of the characters in the first string can be rearranged to match the
characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic
characters. Neither string will be empty.

- Input: Two strings
- Output: True or False based on whether or not some portion of the characters
    in the first string can be rearranged to match the characters in the second

Rules:
- Explicit:
    - String arguments only contain lowercase alphabetic characters
    - Neither string will be empty

Programmatic Algorithm:
1. Start
    - define function 'unscramble(string1, string2)'
2. return all(string2.count(char) >= string1.count(char) for char in string1)


Notes:
- Sloppy. Kind of turned into a hack and slash while debugging. Couldn't figure
 out why this line wasn't working properly with test case 3:
  `return all(string1.count(char) >= string2.count(char) for char in string2 if`
    `all(char in string1 for char in string2))`

  ChatGPT showed me that my syntax was wrong and suggested correcting it to:
  `return all(char in string1 for char in string2)`
    `and all(string1.count(char) >= string2.count(char) for char in string2)`

- ChatGPT explanation:
  Character Check: The inner all checks if every character in `string2` is in
  `string1`. The characters in `string2` are: `p, y, t, h, o, n, r, u, l, e, s`.
  Only `p, h, r, u, l`, and `a` are in `string1`, which means that not all
  characters from `string2` are in `string1`. This inner all condition would
  actually return `False`, but since it's within the comprehension, it doesn't
  stop the count check for the characters that are found.

  'Since not all characters in `string2` are present in
  `string1`, it should return `False`. However, because the inner condition and
  the count checks are combined in a way that can lead to misleading results, the
  final return value might not be what you expect.'



### PY119 Practice Problems: Problem 14
Create a function that takes a single integer argument and returns the sum of
all the multiples of 7 or 11 that are less than the argument. If a number is a
multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and
22. The sum of these multiples is 75.

If the argument is negative, return 0.

- Input: An integer
- Output: An integer that is the sum of all the multiples of 7 or 11 that are
    less than the argument

Rules:
- Explicit:
    - If the argument is negative, return 0.
Data Structures:
- Two lists. One for multiples of 7 and one for multiples of 11.
- A set to combine the two lists and remove any numbers that are multiples of
    both

Programmatic Algorithm:
1. Start
    - define function 'seven_eleven(number)'
    - sevens = [all multiples of seven that are less than the input number]
    - elevens = [all multiples of eleven that are less than the input number]
2. return sum(set(sevens + elevens))

Notes:
-



### PY119 Practice Problems: Problem 15
Create a function that takes a string argument that consists entirely of
numeric digits and computes the greatest product of four consecutive digits in
the string. The argument will always have more than 4 digits.

- Input: A string consisting of digits
- Output: The greatest product of four consecutive digits in the string

Rules:
- Explicit:
    - The argument will always have more than 4 digits.

Data Structures:
- A list to hold all substrings with a length of 4

Programmatic Algorithm:
1. Start
    - define function 'greatest_product(string)'
    - substrings_of_4 = [each substring in the input string with a length of 4]
2. for each substring in substrings_of_4:
    - convert each character to an integer and find their product.
3. return the largest product

Notes:
- This took me way more time than it needed to. I was thinking I needed to
  return the substring that gave the largest product and so it led to me
  overcomplicating it and kind of hacking and slashing. It was a lot easier than
  I was thinking it should be. Should have been 5-10 mins.


### PY119 Practice Problems: Problem 16
Create a function that returns the count of distinct case-insensitive
alphabetic characters and numeric digits that occur more than once in the input
string. You may assume that the input string contains only alphanumeric
characters.

- Input: A string
- Output: An integer representing the count of distinct case-insensitive
    alphabetic characters and numeric digits that occur more than once in the
    input string

Rules:
- Explicit:
    - Assume that the input string contains only alphanumeric characters.
- Implicit:
    - No empty input strings

Questions:
- None

Data Structures:
- A list to hold elements

Programmatic Algorithm:
1. Start
    - define function 'distinct_multiples(string)'
    - distincts = set([All distinct characters that appear more than once in the input string])
2. return the length of distincts

Notes:
-



### PY119 Practice Problems: Problem 17
Create a function that takes a list of integers as an argument. The function
should determine the minimum integer value that can be appended to the list so
the sum of all the elements equal the closest prime number that is greater than
the current sum of the numbers. For example, the numbers in [1, 2, 3] sum to 6.
The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to
sum to 7.

Notes:
The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.

- Input: A list of integers
- Output: An integer that represents the minimum integer value that can be
    appended to the list so the sum of all the elements equal the closest prime
    number that is greater than the current sum of the numbers.

Rules:
- Explicit:
    - The list will always contain at least 2 integers.
    - All values in the list must be positive (> 0).
    - There may be multiple occurrences of the various numbers in the list.

Data Structures:
- A list to get all of the primes up to our number

Programmatic Algorithm:
1. Start
    - define function 'nearest_prime_sum(lst)'
    - primes = [A list of prime numbers that stops when the last element is
                greater than the sum of the input list]
    - nearest_prime = primes[-1]
2. subtract nearest prime from the sum of the input list, and the absolute value
    of that, is our integer, so we return it

Notes:
-


###
- Input:
- Output:

Rules:
- Explicit:
    -
- Implicit:
    -

Questions:
-

Data Structures:
-

Programmatic Algorithm:
1. Start
    -


Notes:
-



- Input:
- Output:

Rules:
- Explicit:
    -
- Implicit:
    -

Questions:
-

Data Structures:
-

Programmatic Algorithm:
1. Start
    -

