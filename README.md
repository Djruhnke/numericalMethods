# numericalMethods
Python Package of numerical methods.

This package, called numericalMethods, is for Python users to easily implement various numerical methods.

Types of methods and a short description of their use as they are implemented are listed below:

##Bisection Method
This method finds the root of a function within a certain interval. It relies on the Mean Value Theorem (MVT) to assess if the root is to the left or the right of the midpoint and resets the endpoints of the interval accordingly. If the midpoint falls within the tolerance of zero it is considered the root and returned.

An example instantiation of this class is 
```bisection = Bisection(f, a, b, tol, iter)``` 
where:

f is the function being evaluated

a is the start point of the interval

b is the end point of the interval

tol is the tolerance of what is considered zero

iter is the maximum number of iterations

##Fixed Point Iteration
This method finds a fixed point of a function. It needs an initial condition to begin iteration where p = IC. To iterate the method, it checks if p is equivalent to f(p) and if it isn't then p = f(p).

An example instantiation of this class is 
```fixedPoint = FixedPoint(f, IC, tol, iter)```
where:

f is the function being evaluated

IC is the initial condition

tol is the tolerance of what is considered equivalent

iter is the maximum number of iterations

##Newton Method
This method finds a fixed point of a function. It needs an initial condition to begin iteration where p = IC. To iterate the method, it checks if p{n} is equivalent to p{n-1} - f(p{n-1}) / f'(p{n-1}) and if it isn't then p{n}=p{n-1} - f(p{n-1}) / f'(p{n-1}).

An example instantiation of this class is
```newton = Newton(f, fderiv, IC, tol, iter)```
where:

f is the function being evaluated

fderiv is the derivative of the function

IC is the initial condition

tol is the tolerance of what is considered equivalent

iter is the maximum number of iterations

##Newton-Bisection Method
This method finds a root within a certain interval. It combines the Newton and the Bisection Method for faster convergance. Once the point falls within the tolerance of zero it is considered the root and returned.

An example instantiation of this class is 
```newton_bisection = NewtonBisection(f, fderiv, a, b, tol, iter)``` 
where:

f is the function being evaluated

fderiv is the derivative of the function

a is the start point of the interval

b is the end point of the interval

tol is the tolerance of what is considered zero

iter is the maximum number of iterations
