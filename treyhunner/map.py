#
"""Make a function map that works the same way as the built-in map function:"""

def square(n):
	return n * n

def map(square, list1):
	return [ square(num) for num in list1 ]