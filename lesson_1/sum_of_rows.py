# 1 # 2                 # 2
# 2 # 4 6               # 10
# 3 # 8 10 12           # 30
# 4 # 14 16 18 20       # 68
# 5 # 22 24 26 28 30    # 130

# 1. Create an empty 'row' list to hold rows
# 2. Create a 'row' list and add it to the overall 'row' list
# 3. Repeat step 2 until all rows are created
# 4. Sum the final row
# 5. Return the sum

def sum_of_row(row_number):
    rows = []
    starting_int = 2

    for row_length in range(1, row_number + 1):
        row = create_row(starting_int, row_length)
        rows.append(row)
        starting_int = row[-1] + 2

    return sum(rows[-1])

def create_row(starting_int, row_length):
    row = []
    row.append(starting_int)

    while len(row) < row_length:
        next_integer = starting_int + (2 * (len(row)))
        row.append(next_integer)

    return row

print(sum_of_row(1) == 2)
print(sum_of_row(3) == 30)
print(sum_of_row(5) == 130)
print(sum_of_row(11))
print(sum_of_row(21))
print(sum_of_row(101))
# print(sum_of_row(10101)) # Don't run this line. Too long, breaks instance
