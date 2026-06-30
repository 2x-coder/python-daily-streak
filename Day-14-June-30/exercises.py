import matplotlib.pyplot as plt
import numpy as np

x= np.arange(1,11)
y= x **3

# '''exercise 1-y=x3'''
# plt.plot(x, y, marker='o')
# plt.show()


# '''Exercise 2-experiment with colors and markers'''
# '''--------------------
# 1.Scatter Plot
# -----------------------'''
# plt.scatter(x, y, )#color='red', marker='*')
# plt.title("Scatter Plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.plot(x, y, marker='o', color='red')
# '''this is also not wrong'''
# plt.show()

# '''Exercise 3:colors to bars'''
# categories = ["A", "B", "C", "D", "E"]
# values = [12, 25, 18, 30, 22]
# # color=["red","green","blue","lavender","gray"]
# plt.bar(categories, values,color=["red","green","blue","lavender","gray"])
# plt.show()

'''Exercise 4:histogram'''

# data = np.random.randn(1000)
# plt.hist(data, bins=10)
# plt.show()
# data = np.random.randn(1000)
# plt.hist(data, bins=20)
# plt.show()
# data = np.random.randn(1000)
# plt.hist(data, bins=30)
# plt.show()
# data = np.random.randn(1000)
# plt.hist(data, bins=40)
# plt.show()
# data = np.random.randn(1000)
# plt.hist(data, bins=90)
# plt.show()

#OR

# data = np.random.randn(1000)

# bin_sizes = [10, 20, 30, 40, 90]
# colors = ['blue', 'green', 'red', 'purple', 'orange']

# plt.figure(figsize=(10,6))

# for bins, color in zip(bin_sizes, colors):
#     plt.hist(data, bins=bins, alpha=0.5, label=f'{bins} bins', color=color)

# plt.title("Histograms with Different Bin Sizes")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.legend()
# plt.show()

#OR SUBPLOTS
# import numpy as np
# import matplotlib.pyplot as plt

# data = np.random.randn(1000)
# bin_sizes = [10, 20, 30, 40, 90]

# fig, axes = plt.subplots(1, len(bin_sizes), figsize=(20,4))

# for ax, bins in zip(axes, bin_sizes):
#     ax.hist(data, bins=bins, color='skyblue', edgecolor='black')
#     ax.set_title(f'{bins} bins')

# plt.tight_layout()
# plt.show()


'''Exercise 5: Pie chart'''



