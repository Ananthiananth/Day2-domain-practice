import pandas as pd

# DataFrame 1
students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Arun", "Banu", "Charan"]
})

# DataFrame 2
marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Mark": [85, 90, 78]
})

print("Students:")
print(students)

print("\nMarks:")
print(marks)

# 1. Merge
print("\n1. Merge:")
merged = pd.merge(students, marks, on="ID")
print(merged)


# 2. Concatenate
df1 = pd.DataFrame({
    "Name": ["Divya", "Eswar"],
    "Mark": [92, 88]
})

df2 = pd.DataFrame({
    "Name": ["Fathima", "Gokul"],
    "Mark": [95, 82]
})

print("\n2. Concatenate:")
combined = pd.concat([df1, df2], ignore_index=True)
print(combined)


# 3. Join
students2 = pd.DataFrame({
    "Name": ["Arun", "Banu", "Charan"]
}, index=[1, 2, 3])

marks2 = pd.DataFrame({
    "Mark": [85, 90, 78]
}, index=[1, 2, 3])

print("\n3. Join:")
joined = students2.join(marks2)
print(joined)