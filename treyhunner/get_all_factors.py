"""Create a function which takes a set of numbers and makes a dictionary containing 
   the numbers as keys and all factors as values."""

# 
def get_factors(number):
    return [n for n in range(1, number + 1) if number % n == 0]
	
	
def get_all_factors(numbers):
	return {key: get_factors(key) for key in numbers}

get_all_factors({62, 293, 314})
get_all_factors({1, 2, 3, 4})