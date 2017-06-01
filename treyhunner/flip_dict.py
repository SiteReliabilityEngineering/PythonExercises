#
"""Make a function flip_dict, that flips dictionary keys and values."""
#
def flip_dict(dict1):
	return { value: key for key, value in dict1.iteritems() }