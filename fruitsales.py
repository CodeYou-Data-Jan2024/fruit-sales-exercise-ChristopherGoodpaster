# add your code here
import pandas as pd

# Create a DataFrame to match the table
data = {"Apples": [35, 41],
        "Bananas": [21, 34]}
#create the index 
index = ["2017 Sales", "2018 Sales"]

df = pd.DataFrame(data, index=index)

# Write the DataFrame to a CSV file
df.to_csv("fruit.csv")

print("Data written to fruit.csv")
