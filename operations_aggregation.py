import pandas as pd

data = {
    "Name": ["Arun", "Banu", "Charan", "Divya", "Eswar"],
    "Mark": [85, 90, 78, 92, 88],
    "Attendance": [90, 95, 85, 98, 88]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# 1. First 5 rows
print("\n1. First rows:")
print(df.head())

# 2. Basic information
print("\n2. Information:")
df.info()

# 3. Statistical summary
print("\n3. Statistical summary:")
print(df.describe())

# 4. Average mark
print("\n4. Average Mark:")
print(df["Mark"].mean())

# 5. Highest mark
print("\n5. Highest Mark:")
print(df["Mark"].max())

# 6. Lowest mark
print("\n6. Lowest Mark:")
print(df["Mark"].min())

# 7. Total marks
print("\n7. Total Marks:")
print(df["Mark"].sum())

# 8. Sort by mark
print("\n8. Sorted by Mark:")
print(df.sort_values("Mark", ascending=False))