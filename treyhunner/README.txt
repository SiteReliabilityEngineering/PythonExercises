https://gist.github.com/treyhunner/f1de66dd94c39fe16af1
https://docs.google.com/document/d/1H3xwbaPHTRF21ROXhO0IFm7iPNyISIH7HCQ4hzbn-P4/edit

List Comprehensions
Power List By Index

Make a function, power_list, that accepts a list of numbers and returns a new list that contains each number raised to the i-th power where i is the index of that number in the given list. For example:

>>> power_list([3, 2, 5])
[1, 2, 25]
>>> numbers = [78, 700, 82, 16, 2, 3, 9.5]
>>> power_list(numbers)
[1, 700, 6724, 4096, 16, 243, 735091.890625]

Hint

Use enumerate
Starting with a vowel

Make a function that accepts a list of names and returns a new list containing all names that start with a vowel. It should work like this:

>>> names = ["Alice", "Bob", "Christy", "Jules"]
>>> vowel_names(names)
['Alice']
>>> names = ["Scott", "Arthur", "Jan", "Elizabeth"]
>>> vowel_names(names)
['Arthur', 'Elizabeth']

Divisible

Make a list of all numbers between 100 and 300 that are divisble by both 6 and 10.
Filter

Make a function filter that works the same way as the built-in filter function:

>>> from math import sqrt
>>> def is_square(n):
...     return sqrt(n).is_integer()
...
>>> filter(is_square, [1, 2, 3, 4, 5, 6])
[1, 4]

Map

Make a function map that works the same way as the built-in map function:

>>> def square(n):
...     return n * n
...
>>> map(square, [1, 2, 3, 4, 5, 6])
[1, 4, 9, 16, 25, 36]

Flatten a Matrix

Create a function flatten, that will take a matrix (a list of lists) and return a flattened version of the matrix.

>>> matrix = [[row * 3 + incr for incr in range(1, 4)] for row in range(4)]
>>> matrix
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
>>> flatten(matrix)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

Hint

You can use a nested list comprehension
More Comprehensions
ASCII Strings

Create a function that accepts a list of strings and returns a dictionary containing the strings as keys and a list of corresponding ASCII character codes as values.

>>> words = ["hello", "bye", "yes", "no", "python"]
>>> get_ascii_codes(words)
{'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111], 'python': [112, 121, 116, 104, 111, 110], 'no': [110, 111], 'bye': [98, 121, 101]}

Flipped Dictionary

Make a function flip_dict, that flips dictionary keys and values.

Example usage:

>>> flip_dict({'Python': "2015-09-15", 'Java': "2015-09-14", 'C': "2015-09-13"})
{'2015-09-13': 'C', '2015-09-15': 'Python', '2015-09-14': 'Java'}

Factors

Create a function which takes a set of numbers and makes a dictionary containing the numbers as keys and all factors as values.

>>> get_all_factors({1, 2, 3, 4})
{1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4]}
>>> get_all_factors({62, 293, 314})
{314: [1, 2, 157, 314], 293: [1, 293], 62: [1, 2, 31, 62]}

Hint

You can use this function to find the factors of any number:

def get_factors(number):
    return [n for n in range(1, number + 1) if number % n == 0]

resources.rst
Related Resources

    Dive into Python 3: Comprehensions (3.3, 3,4, 3.5)
    Python Practice Book: Working With Data
    Python Cookbook: Data Structures and Algorithms

