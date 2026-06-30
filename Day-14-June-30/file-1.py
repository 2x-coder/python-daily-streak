import matplotlib.pyplot as plt
import numpy as np

# Sample data 
x = np.arange(1,11)
y = x**2

'''--------------------
1.Line Plot 
-----------------------'''
plt.plot(x, y, marker='^')
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

'''--------------------
1.Scatter Plot
-----------------------'''
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

'''--------------------
3. Bar Chart
-----------------------'''
values = 
