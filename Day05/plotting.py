#matplotlib

#1 Temperature vs Time
print("1 Temperature vs Time")

import matplotlib.pyplot as plt

time =[1, 2, 3, 4, 5]
temperature =[30, 32, 35, 33, 31]

plt.plot(time, temperature)

plt.title("Temperature vs Time")
plt.xlabel("Time (Hours)")
plt.ylabel("Temperature(°C)")

plt.show()

#2Save the graph as an image 
