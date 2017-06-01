#
"""Create a function that accepts a list of strings and returns a dictionary containing 
   the strings as keys and a list of corresponding ASCII character codes as values."""
   
words = ["hello", "bye", "yes", "no", "python"]
{ x: [ord(y) for y in x] for x in words}