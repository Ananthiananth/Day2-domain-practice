import pandas as pd

# Create DataFrame
data = {
    "Name": ["Arun", "Banu", "Charan", "Divya", "Eswar"],
    "Age": [19, 20, 19, 20, 21],
    "Mark": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 1. Select one column
print("\n1. Name column:")
print(df["Name"])


# 2. Select multiple columns
print("\n2. Name and Mark:")
print(df[["Name", "Mark"]])


# 3. Select first row using loc
print("\n3. First row:")
print(df.loc[0])


# 4. Select second row using iloc
print("\n4. Second row:")
print(df.iloc[1])


# 5. Select students with mark greater than 80
print("\n5. Students with mark > 80:")
print(df[df["Mark"] > 80])