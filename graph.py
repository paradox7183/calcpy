#Library numpy for algebra 
import numpy as np  
#Def function of x and the respective ecuation
def f(x):
    return np.sqrt((-x + 2) * (x**2))
#Importing matplotlib for graphing f(x)    
import matplotlib.pyplot as plt
#Dividing the positives and negative numbers.
def better_graph():
    fix, ax = plt.subplots()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")
    
    for spine in ["right", "top"]:
        ax.spines[spine].set_color("none")
    
    return ax
#Arraying the better_graph function
x = np.linspace(-2, 6, num=30)
ax = better_graph()
ax.grid()
ax.plot(x, f(x))
#Ploting the function
plt.title(r"Grafico de f(x)")
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()