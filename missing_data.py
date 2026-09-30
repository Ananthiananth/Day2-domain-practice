import pandas as pd

data = {
    "Name": ["Arun", "Banu", "Charan", "Divya", "Eswar"],
    "Mark": [85, 90, None, 92, None],
    "Attendance": [90, None, 85, 95, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 1. Check missing values
print("\n1. Missing values:")
print(df.isnull())

# 2. Count missing values
print("\n2. Missing value count:")
print(df.isnull().sum())

# 3. Remove rows with missing values
print("\n3. After removing missing values:")
print(df.dropna())

# 4. Fill missing values with 0
print("\n4. Fill missing values with 0:")
print(df.fillna(0))

# 5. Fill missing Mark with average
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())

print("\n5. Mark after filling with average:")
print(df)