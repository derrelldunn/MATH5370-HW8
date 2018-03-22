import matplotlib.pyplot as plt
import numpy as np

# Create functions and set domain length
x = np.arange(-1.5, 5.0, 0.01)
y = (x**3) - (6*(x**2)) + (11*x) - 6
dy = (x**3) - x
#dz = (x**3) + (3*x) + 2

# Plot functions and a point where they intersect
plt.plot(x, y)
plt.plot(x, dy)
#plt.plot(x, dz)
plt.plot(1,0, 'or')
plt.plot(2,0, 'or')
plt.plot(3,0,'or')
plt.plot(-1, 0, 'or')
plt.plot(0,0, 'or')

# Config the graph
plt.title('Math 5370 - HW8 #1')
plt.xlabel('X')
plt.ylabel('Y')
plt.ylim([-3, 5])
plt.grid(True)
plt.legend(['$f(x)= x^3-6x^2+11x-6$', '$ g(x)= x^3-x$'], loc='upper left')

## Show the graph
plt.show()