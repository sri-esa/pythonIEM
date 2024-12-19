# Write a Python program to create a Fibonacci sequence till a specific no. of terms and count the number of variables used without any functions

a= int(input("enter no. of terms::"))
n1 = 0
n2 = 1
print(f"The Fibonacci series are:{n1},{n2},",end=" ")
count=2 #a,i
for i in range (2,a):
    n3 = n1 + n2
    n1=n2
    n2=n3
    print (f"{n3},",end=" ")
    count+=3
print (f"\nno. of variable used={count}")


'''
# Input the number of terms for the Fibonacci sequence
n = int(input("Enter the number of terms: "))

# Initialize the first two terms
a = 0
b = 1

# Counter for the number of variables used
variable_count = 4  # variables used: n, a, b, i (will use it in loop)

# Print the Fibonacci sequence
if n >= 1:
    print(a, end=" ")  # Print the first term
if n >= 2:
    print(b, end=" ")  # Print the second term

# Generate the remaining Fibonacci terms
for i in range(2, n):  # Loop starting from the 3rd term
    c = a + b  # Calculate the next term
    print(c, end=" ")  # Print the next term
    a = b  # Move 'a' to 'b'
    b = c  # Move 'b' to the new term 'c'
    
    variable_count += 1  # We use 'c' as an additional variable

# Output the number of variables used
print(f"\nTotal variables used: {variable_count}")
'''