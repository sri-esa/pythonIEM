#Write a Python program to find the determinant of NumPy matrix.
import numpy as np

# Input the size of the square matrix (n x n)
n = int(input("Enter the size of the square matrix (n x n): "))

# Initialize an empty list to store the matrix elements
elements = []

# Input the elements row-wise
print("Enter the elements row by row:")
for i in range(n):
    row = list(map(float, input(f"Enter elements of row {i + 1} separated by space: ").split()))
    elements.append(row)

# Convert the list to a NumPy matrix
matrix = np.array(elements)

# Display the original matrix
print("\nThe matrix is:")
print(matrix)

# Calculate the determinant of the matrix
determinant = np.linalg.det(matrix)

# Display the determinant
print(f"\nThe determinant of the matrix is: {determinant}")