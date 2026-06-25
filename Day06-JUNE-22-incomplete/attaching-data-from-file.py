# 1 create data/experiment.csv
# 2 read csv using pandas
import pandas as pd
data = pd.read_csv("Day06-JUNE-22/data/experiment.csv")
print(data)

# 3 Average Temperature 
import pandas as pd 
data = pd.read_csv("Day06-JUNE-22/data/experiment.csv")
average_temp = data["temperature"].mean()
print("Average Temperature:", average_temp)

#4 Maximum Temperature
import pandas as pd
data = pd.read_csv("Day06-JUNE-22/data/experiment.csv")
max_temp = data["temperature"].max()
print("Maximum Temperature:", max_temp)

#More examples to practice 
#1 Minimum Temperature

