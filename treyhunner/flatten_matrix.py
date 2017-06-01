#
"""Create a function flatten, that will take a matrix (a list of lists) 
   and return a flattened version of the matrix."""
   
# we create the matrix
matrix = [[row * 3 + incr for incr in range(1, 4)] for row in range(4)]

#we flatten the matrix

def flatten(matrix):
	return [ dim2 for dim1 in range(len(matrix)) for dim2 in matrix[dim1] ]
	
flatten(matrix)
		