#Write a Python program to transpose a 2-dimensional NumPy array.
import numpy as np
# Input number of rows and columns
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

# Transpose the array
transposed_array = array.T

# Display the transposed 2D NumPy array
print("\nThe transposed 2D NumPy array is:")
print(transposed_array)