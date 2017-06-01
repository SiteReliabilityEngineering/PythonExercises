"""Make a function that accepts a list of names and returns a new list 
   containing all names that start with a vowel. It should work like this:"""

names = ["Alice", "Bob", "Christy", "Jules"]

def vowel_names(names):
	return [ name for name in names if name[0].capitalize() in 'AEIOU' ]

vowel_names(names)

names = ["Scott", "Arthur", "Jan", "Elizabeth"]
vowel_names(names)