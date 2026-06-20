#using numpy
import numpy as np
data = [12,14,16,15,13]
print(np.mean(data))
print(np.std(data))

#1 Creating NumPy Arrays
print("------1 Creating NumPy Arrays------")
import numpy as np 
arr = np.array([10,20,30,40,50])
print(arr)
print(type(arr))

#2 Basic Statistics
print("------2 Basic Statistics------")
import numpy as np
data = np.array([12,14,16,15,13])

print("Mean:", np.mean(data))
print("Median:",np.median(data))
print("Min:", np.min(data))
print("Max:", np.max(data))

#3 Standard Deviation
print("------3 Standard Deviation------")

import numpy as np
scores = np.array([70,75,80,85,90])
print("Mean", np.mean(scores))
print("Std Dev:", np.std(scores))

#4 Sum and Average 
print("------4 Sum and Average------")
import numpy as np
expenses = np.array([100, 250, 150,300])
print("Total Expense:", np.sum(expenses))
print("Average Expense:", np.mean(expenses))

#5 Array Arithmatic
print("------5 Array Arithmatics------")
import numpy as np
a = np.array([1,2,3])
print(a + 5)
print(a * 2)

#6 Comparing Values 
print("------6 Comparing Values------")
import numpy as np
marks = np.array([45, 78, 90, 34, 88])
print(marks > 50)

#7 Filtering Data
print("------7 Filtering Data------")
import numpy as np
marks = np.array([5, 78, 90, 34, 88])
passed = marks[marks >= 50]
print(passed)

#8 2D Arrays(Tables)
print("------8 2D Arrays(Tables)s------")
import numpy as np 
students = np.array([
    [85, 90, 88],
    [70, 75, 80],
    [95, 92, 96]
])
print(students)

#9 Row-wise Statistics
print("------9 Row-wise Statistics------")
'Average marks of each Student'
import numpy as np
students = np.array([
    [85, 90, 88],
    [70, 75, 80],
    [95, 92, 96]
])
print(np.mean(students, axis=1))

#10 Column-wise Statistics
print("------10 Column-wise Statistics------")
'Average marks per subject'
import numpy as np 
students = np.array([
     [85, 90, 88],
    [70, 75, 80],
    [95, 92, 96]
])
print(np.mean(students, axis=0))

#11 Finding Highest and Lowest Values
print("------11 Finding Highest and Lowest Values------")
import numpy as np 
temperatures = np.array([32, 35, 30, 38, 36])
print("Highest:", np.max(temperatures))
print("Lowest:", np.min(temperatures))
print("var", np.var(temperatures))

#12 Variance
print("------12 Variance------")
import numpy as np
data= np.array([10, 12, 14, 16, 18])
print("Variance:", np.var(data))
print("Std Dev:", np.std(data))

#13 Percentiles
print("------13 Percentiles------")
import numpy as np
scores = np.array([55, 60, 70, 75, 80, 90, 95])

print("25th percentile:", np.percentile(scores, 25))
print("50th percentile:", np.percentile(scores,50 ))
print("90th percentile:", np.percentile(scores,90 ))

#14 Random Experimental Data
print("------14 Random Experimental Data------")
import numpy as np 
data = np.random.normal(loc=50, scale=5,size=10)

print(data)
print("Mean:", np.mean(data))
print("Std:", np.std(data))
