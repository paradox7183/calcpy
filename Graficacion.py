import matplotlib.pyplot as plt
import sympy 
import  colorama
# Define the function
def f(x): 
	return 2*x**3
# Define the variable
x = sympy.Symbol('x')
# Calculate the derivative of the function
derivative = sympy.diff(f(x), x)
# Define the range of x-values to plot
x_range = range(-10, 11)
# Calculate the y-values of the derivative
y_values = [derivative.evalf(subs={x: i}) for i in x_range]
# Plot the derivative
plt.plot(x_range, y_values)
plt.show()
