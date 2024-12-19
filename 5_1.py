#Read a CSV file as a pandas data frame
import pandas as pd

# Read the CSV file
file_path = input("Enter the path to your CSV file: ")
data_frame = pd.read_csv(file_path)

# Display the DataFrame
print("\nThe contents of the CSV file are:")
print(data_frame)