import pandas as pd

# 1. Read CSV file
df = pd.read_csv("dataset/students.csv")

print("CSV Data:")
print(df)

# 2. Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# 3. Save DataFrame to a new CSV file
df.to_csv("students_output.csv", index=False)
print("\nCSV file saved successfully.")

# 4. Create an Excel file
df.to_excel("students_output.xlsx", index=False)
print("Excel file saved successfully.")

# 5. Read the Excel file
excel_df = pd.read_excel("students_output.xlsx")

print("\nExcel Data:")
print(excel_df.head())