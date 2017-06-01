#
"""Make a function filter that works the same way as the built-in filter function:"""
from math import sqrt

def is_square(n):
	return sqrt(n).is_integer()

def filter(is_square, list1):
	return [ num for num in list1 if is_square(num) ]

filter(is_square, [1, 2, 3, 4, 5, 6])
