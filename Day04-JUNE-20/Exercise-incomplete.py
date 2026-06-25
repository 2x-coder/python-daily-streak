import numpy as np


#Exercise 1
data = [5, 10, 15, 20, 25]

print("Mean",np.mean(data))
print("Median",np.median(data))
print("std",np.std(data))

#Exercise 2
sales = [120, 150, 180, 200, 170]

print("Total Sales",np.sum(sales))
print("Average Sales",np.average(sales))
print("Highest sale",np.max(sales))
print("Lowest sale",np.min(sales))

#Exercise 3
'Create a 3×3 NumPy array and find:'

marks = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# print("Row averages",np.average(marks, axis=0))
# print("Column averages",np.average(marks, axis = 1))
# print("Overall average",np.average(marks))

# print("Row averages",np.mean(marks, axis=0))
# print("Column averages",np.mean(marks, axis = 1))
# print("Overall average",np.mean(marks))

#Exercise 4
'Generate 20 random numbers between 1 and 100 and find:'
# Mean
# Median
# Standard deviation
# Maximum
