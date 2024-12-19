#Write a Python Program to call data member and function using classes and objects
# Define a class named 'Student'
class Student:
    # Constructor to initialize data members
    def __init__(self, name, age):
        self.name = name  # Data member for student's name
        self.age = age    # Data member for student's age
    
    # A method to display student details
    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")

# Create an object of the Student class
student1 = Student("Alice", 21)

# Access and print data members
print("Accessing data members:")
print(f"Name: {student1.name}")
print(f"Age: {student1.age}")

# Call a function (method) to display student details
print("\nCalling a method to display details:")
student1.display_details()