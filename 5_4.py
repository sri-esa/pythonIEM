# Find the mean and standard deviation of a specific column containing numeric data
import pandas as pd

# Read the CSV file into a DataFrame
file_path = input("Enter the path to your CSV file: ")
data_frame = pd.read_csv(file_path)

# Display the DataFrame
print("\nThe contents of the CSV file are:")
print(data_frame)

# Input the column name containing numeric data
column_name = input("\nEnter the column name to find mean and standard deviation: ")

# Check if the column exists and is numeric
if column_name in data_frame.columns and pd.api.types.is_numeric_dtype(data_frame[column_name]):
    # Calculate mean and standard deviation
    mean_value = data_frame[column_name].mean()
    std_dev = data_frame[column_name].std()

    # Display the mean and standard deviation
    print(f"\nMean of '{column_name}': {mean_value}")
    print(f"Standard Deviation of '{column_name}': {std_dev}")
else:
    print("\nThe specified column does not exist or is not numeric.")