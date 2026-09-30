import pandas as pd

# 1. Create Series
marks = pd.Series([85, 90, 78, 92, 88])
print("Series:")
print(marks)


# 2. Create DataFrame
data = {
    "Name": ["Arun", "Banu", "Charan", "Divya"],
    "Mark": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


# 3. Select a column
print("\nNames:")
print(df["Name"])


# 4. Add a new column
df["Result"] = ["Pass", "Pass", "Pass", "Pass"]

print("\nUpdated DataFrame:")
print(df)


# 5. Find average mark
print("\nAverage Mark:")
print(df["Mark"].mean())