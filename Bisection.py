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
		Function must take a variable and return a result. Tolerance must be a positive 
		number. Start point must be before end point. Max iterations must be a positive 
		number.
		"""
		assert tol > 0, "Tolerance must be positive"
		assert start < end, "End point must be after start point"
		assert numIter > 0, "Max iterations must be at least 1"
		self.function = function
		self.start = start
		self.end = end
		self.tol = tol
		self.numIter = numIter

	def findRoot(self):
		""" Finds and returns the root of the function using the bisection method. 
		If the max number of iterations are reached without convergence within the 
		tolerance then a message is printed and None is returned."""
		i = 0
		a = self.start
		b = self.end
		while i < self.numIter:
			p = (a + b) / 2
			if abs(self.function(p)) < self.tol:
				return p
			elif self.function(p) * self.function(b) < 0:
				a = p
			elif self.function(p) * self.function(a) < 0:
				b = p
			i += 1
		print("Function did not converge within max number of iterations.")
		return None

	def setFunction(self, function):
		""" Sets a new function to be evaluated.

		Arguments:
		function -- the new function to be evaluated, must take an argument as the variable 
		in the function and return the result

		Preconditions:
		Function must take a variable and return a result.
		"""
		self.function = function

	def setInterval(self, a, b):
		""" Sets a new interval for the function to be evaluated on.

		Arguments:
		a -- the new start point of the interval
		b -- the new end point of the interval

		Preconditions:
		Start point must be before end point.
		"""
		assert a < b, "End point must be after start point"
		self.start = a
		self.end = b

	def setTolerance(self, tol):
		""" Sets a new tolerance for the method.

		Arguments:
		tol -- the new tolerance which the result must fall within the actual result to be 
		returned

		Preconditions:
		Tolerance must be a positive number.
		"""
		assert tol > 0, "Tolerance must be positive"
		self.tol = tol

	def setMaxIterations(self, numIter):
		""" Sets a new number of max iterations.

		Arguments:
		numIter -- the maximum number of iterations that will be executed before 
		the function returns a failure

		Preconditions:
		Max iterations must be a positive number.
		"""
		assert numIter > 0, "Max iterations must be at least 1"
		self.numIter = numIter