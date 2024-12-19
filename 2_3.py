#Write a Python program to demonstrate the use of Local and Global variables.
# Global variable
x = 10

def local_scope_example():
    # Local variable
    x = 5
    print(f"Inside the function, local x = {x}")  # This will print the local variable x

def global_scope_example():
    # Using the global keyword to modify the global variable inside the function
    global x
    x = 20
    print(f"Inside the function, global x modified to = {x}")

# Example usage
print(f"Initial global x = {x}")  # Prints the global variable x

local_scope_example()  # Demonstrates the local scope variable
print(f"After calling local_scope_example, global x = {x}")  # Global variable x remains unchanged

global_scope_example()  # Modifies the global variable using the 'global' keyword
print(f"After calling global_scope_example, global x = {x}")  # Global variable x is modified
