import pandas as pd

# Read dataset
df = pd.read_csv("dataset/students.csv")

print("1. First 5 rows:")
print(df.head())

print("\n2. Dataset shape:")
print(df.shape)

print("\n3. Basic information:")
df.info()

print("\n4. Statistical summary:")
print(df.describe())

print("\n5. Missing values:")
print(df.isnull().sum())

print("\n6. Average exam score:")
print(df["exam_score"].mean())

print("\n7. Highest exam score:")
print(df["exam_score"].max())

print("\n8. Student with highest exam score:")
print(df.loc[df["exam_score"].idxmax(), "name"])

print("\n9. Students with attendance below 75:")
print(df[df["attendance"] < 75])

print("\n10. Average exam score by department:")
print(df.groupby("department")["exam_score"].mean())