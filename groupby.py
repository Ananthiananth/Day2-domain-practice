import pandas as pd

data = {
    "Name": ["Arun", "Banu", "Charan", "Divya", "Eswar", "Fathima"],
    "Department": ["IT", "CSE", "IT", "CSE", "IT", "CSE"],
    "Mark": [85, 90, 78, 92, 88, 95]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# 1. Average mark by department
print("\n1. Average mark by department:")
print(df.groupby("Department")["Mark"].mean())

# 2. Maximum mark by department
print("\n2. Maximum mark by department:")
print(df.groupby("Department")["Mark"].max())

# 3. Minimum mark by department
print("\n3. Minimum mark by department:")
print(df.groupby("Department")["Mark"].min())

# 4. Number of students in each department
print("\n4. Student count by department:")
print(df.groupby("Department")["Name"].count())

# 5. Multiple aggregation
print("\n5. Multiple aggregation:")
print(df.groupby("Department")["Mark"].agg(["mean", "max", "min", "count"]))