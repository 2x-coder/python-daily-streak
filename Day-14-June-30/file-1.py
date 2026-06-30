import matplotlib.pyplot as plt
import numpy as np

# # Sample data 
x = np.arange(1,11)
y = x**2

# '''--------------------
# 1.Line Plot 
# -----------------------'''
# plt.plot(x, y, marker='^')
# plt.title("Line Plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid(True)
# plt.show()

# '''--------------------
# 1.Scatter Plot
# -----------------------'''
# plt.scatter(x, y)
# plt.title("Scatter Plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# '''--------------------
# 3. Bar Chart
# -----------------------'''
# categories = ["A", "B", "C", "D", "E"]
# values = [12, 25, 18, 30, 22]
# plt.bar(categories, values)
# plt.title("Bar Chart")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid("True")
# plt.show()


# '''--------------------
# 4. Histogram
# -----------------------'''

# data = np.random.randn(1000)
# plt.hist(data, bins=20)
# plt.title("Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

# '''--------------------
# 5. Pie Chart
# -----------------------'''
# labels = ["Python", "Java", "C++", "Javascript"]
# sizes = [40,25,20,15]
# plt.pie(sizes, labels=labels, autopct="%1.1f%%")
# plt.title("Pie Chart")
# plt.show()

'''--------------------
6. Box Plot
-----------------------'''
data = [np.random.normal(0,1,100), 
        np.random.normal(2, 0.5, 100)]
plt.boxplot(data)
plt.title("Box Plot")
plt.xticks([1,2], ["Group1", "Group2"])
plt.show()

