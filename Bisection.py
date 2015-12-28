"""Implementation of the bisection method

This method is implemented by the class Bisection.

Author: Daniel Ruhnke
"""

class Bisection:
	""" Bisection class

	The bisection method finds the root of a function between two end points within 
	a certain tolerance. The user may update the function, tolerance, start and end points, 
	or the max iterations. When the method is actually run it will return a float that 
	is a prediction of the root within the tolerance.
	"""

	def __init__(self, function, start, end, tol, numIter):
		""" Sets up all the necessary attributes to exectute the bisection method.

		Arguments:
		function -- the function to be evaluated, must take an argument as the variable 
		in the function and return the result
		start -- the starting point to be evaluated
		end -- the ending point to be evaluated
		tol -- the tolerance which the result must fall within the actual result to be 
		returned
		numIter -- the maximum number of iterations that will be executed before 
		the function returns a failure

		Preconditions:
		Function must take a variable and return a result. Tolerance must be non-negative 
		number. Start point must be before end point. Max iterations must be a positive 
		number.
		"""
		assert tol >= 0, "Tolerance must be non-negative"
		assert start < end, "End point must be after start point"
		assert numIter > 0, "Max iterations must be at least 1"
		self.function = function
		self.start = start
		self.end = end
		self.tol = tol
		self.numIter = numIter