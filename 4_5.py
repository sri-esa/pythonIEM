#Write a Python program to find the inverse of a NumPy matrix
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

# Check if the matrix is invertible by checking its determinant
determinant = np.linalg.det(matrix)
if determinant == 0:
    print("\nThe matrix is not invertible (determinant is 0).")
else:
    # Calculate the inverse of the matrix
    inverse_matrix = np.linalg.inv(matrix)
    
    # Display the inverse of the matrix
    print("\nThe inverse of the matrix is:")
    print(inverse_matrix)