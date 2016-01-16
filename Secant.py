"""Implementation of the secant method

This method is implemented by the class Secant.

Author: Daniel Ruhnke
"""

class Secant:
	""" Secant class

	The secant method finds the point where x = f(x) within a certain 
	tolerance. The user may update the function, tolerance, two initial conditions, or the max 
	iterations. When the method is actually run it will return a float that is a 
	prediction of the fixed point within the tolerance.
	"""

	def __init__(self, function, IC1, IC2, tol, numIter):
		""" Sets up all the necessary attributes to exectute the secant method.

		Arguments:
		function -- the function to be evaluated, must take an argument as the variable 
		in the function and return the result
		IC1 -- the first initial condition to start the execution of the method
		IC2 -- the second initial condition to start the execution of the method
		tol -- the tolerance which the result must fall within the actual result to be 
		returned
		numIter -- the maximum number of iterations that will be executed before 
		the function returns a failure

		Preconditions:
		Function must take a variable and return a result. Tolerance 
		must be a positive number. Max iterations must be a positive number.
		"""
		assert tol > 0, "Tolerance must be positive"
		assert numIter > 0, "Max iterations must be at least 1"
		self.function = function
		self.IC1 = IC1
		self.IC2 = IC2
		self.tol = tol
		self.numIter = numIter

	def findFixedPoint(self):
		""" Finds and returns a fixed point of the function using the secant method. 
		If the max number of iterations are reached without convergence within the 
		tolerance then a message is printed and None is returned.
		"""
		i = 1
		p0 = self.IC1
		q0 = self.function(self.IC1)
		p1 = self.IC2
		q1 = self.function(self.IC2)
		while i < self.numIter:
			p = p1 - q1 * (p1 - p0) / (q1 - q0)
			if abs(p - p1) < self.tol:
				return p
			i += 1
			p0 = p1
			q0 = q1
			p1 = p
			q1 = self.function(p)
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

	def setIC(self, IC1, IC2):
		""" Sets a new initial condition for the method.

		Arguments:
		IC1 -- the new first initual condition to start the execution of the method
		IC2 -- the new second initial condition to start the execution of the method
		"""
		self.IC1 = IC1
		self.IC2 = IC2

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