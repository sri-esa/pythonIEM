# Fetch rows from the data frame based on a specific attribute.
import pandas as pd

# Read the CSV file into a DataFrame
file_path = input("Enter the path to your CSV file: ")
data_frame = pd.read_csv(file_path)

# Display the DataFrame
print("\nThe contents of the CSV file are:")
print(data_frame)

# Input the column name (attribute) and the value to filter
column_name = input("\nEnter the column name to filter by: ")
filter_value = input(f"Enter the value to filter rows where '{column_name}' is: ")

# Fetch rows where the column has the specified value
filtered_rows = data_frame[data_frame[column_name] == filter_value]

# Display the filtered rows
print(f"\nRows where '{column_name}' is '{filter_value}':")
print(filtered_rows)