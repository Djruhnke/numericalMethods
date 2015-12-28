# numericalMethods
Python Package of numerical methods.

This package, called numericalMethods, is for Python users to easily implement various numerical methods.

Types of methods and a short description of their use as they are implemented are listed below:

##Bisection Method
This method finds the root of a function within a certain interval. It relies on the Mean Value Theorem (MVT) to assess if the root is to the left or the right of the midpoint and resets the endpoints of the interval accordingly. If the midpoint falls within the tolerance of zero it is considered the root and returned.

An example instantiation of this class is 
>bisection = Bisection(f, a, b, tol, iter) 
where:
f is the function being evaluated
a is the start point of the interval
b is the end point of the interval
tol is the tolerance of what is considered zero
iter is the maximum number of iterations
