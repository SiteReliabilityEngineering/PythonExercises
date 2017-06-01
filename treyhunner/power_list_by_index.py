"""Make a function, power_list, that accepts a list of numbers and returns a new list that contains each 
   number raised to the i-th power where i is the index of that number in the given list. For example:"""

#

numbers = [78, 700, 82, 16, 2, 3, 9.5]

def power_list(numbers):
	return [ value ** key for (key, value) in enumerate(numbers) ]