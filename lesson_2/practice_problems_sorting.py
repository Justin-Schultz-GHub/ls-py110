# lst = [10, 9, -6, 11, 7, -16, 50, 8]
# # sorted_list = sorted(lst)
# # reverse_sorted_list = sorted(lst, reverse=True)
# # print(sorted_list)
# # print(reverse_sorted_list)

# Expected result
# # [-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
# # [50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort

# lst.sort()
# print(lst)

# lst.sort(reverse=True)
# print(lst)

# lst = [10, 9, -6, 11, 7, -16, 50, 8]
# lst.sort(key=str)
# print(lst)
# lst.sort(key=str, reverse=True)
# print(lst)

# # Expected result
# # [-16, -6, 10, 11, 50, 7, 8, 9]          # Ascending sort
# # [9, 8, 7, 50, 11, 10, -6, -16]          # Descending sort

# books = [
#     {
#         'title': 'One Hundred Years of Solitude',
#         'author': 'Gabriel Garcia Marquez',
#         'published': '1967',
#     },
#     {
#         'title': 'The Book of Kells',
#         'author': 'Multiple Authors',
#         'published': '800',
#     },
#     {
#         'title': 'War and Peace',
#         'author': 'Leo Tolstoy',
#         'published': '1869',
#     },
# ]

# def get_published(book):
#     return int(book['published'])

# books.sort(key=get_published)

# # My solution
# books.sort(key=lambda books: int(books['published']))
# print(books)


# Expected result
# [
#     {
#         'title': 'The Book of Kells',
#         'author': 'Multiple Authors',
#         'published': '800'
#     },
#     {
#         'title': 'War and Peace',
#         'author': 'Leo Tolstoy',
#         'published': '1869'
#     },
#     {
#         'title': 'One Hundred Years of Solitude',
#         'author': 'Gabriel Garcia Marquez',
#         'published': '1967'
#     }
# ]

# lst = [[1], [2]]

# lst[0].append([9])
# lst                 # [[1, [9]], [2]]

# print(lst[0][1][0])

