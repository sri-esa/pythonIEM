#Write a Python program to reshape a 2-dimensional NumPy array
import numpy as np

# Input number of rows and columns for the original array
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize an empty list to store the array elements
elements = []

# Input the elements row-wise
print("Enter the elements row by row:")
for i in range(rows):
    row = list(map(int, input(f"Enter elements of row {i + 1} separated by space: ").split()))
    elements.append(row)

# Convert the list to a 2D NumPy array
array = np.array(elements)

# Display the original 2D NumPy array
print("\nThe original 2D NumPy array is:")
print(array)

# Input new dimensions for reshaping
new_rows = int(input("\nEnter the number of rows for reshaped array: "))
new_cols = int(input("Enter the number of columns for reshaped array: "))

# Reshape the array
reshaped_array = array.reshape(new_rows, new_cols)

# Display the reshaped 2D NumPy array
print("\nThe reshaped 2D NumPy array is:")
print(reshaped_array)