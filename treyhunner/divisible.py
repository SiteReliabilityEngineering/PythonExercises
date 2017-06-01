#
"""Make a list of all numbers between 100 and 300 that are divisble by both 6 and 10."""


def divisibleby_6_10():
	return [ divi for divi in range(100, 301) if divi % 6 == 0 and divi % 10 == 0 ]

divisibleby_6_10()