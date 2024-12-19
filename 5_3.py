# Display the value of specific columns of a pandas data frame
import pandas as pd

# Read the CSV file into a DataFrame
file_path = input("Enter the path to your CSV file: ")
data_frame = pd.read_csv(file_path)

# Display the DataFrame
print("\nThe contents of the CSV file are:")
print(data_frame)

# Input the column names to display
columns = input("\nEnter the column names you want to display (comma-separated): ").split(',')

# Strip any extra spaces from column names
columns = [col.strip() for col in columns]

# Display the selected columns
try:
    selected_columns = data_frame[columns]
    print(f"\nThe values of the columns {columns} are:")
    print(selected_columns)
except KeyError:
    print("\nOne or more of the specified columns do not exist in the DataFrame.")