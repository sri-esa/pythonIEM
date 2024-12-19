#Write a Python Program to demonstrate the use of constructors.
# Define a class named 'Person'
class Person:
    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name  # Data member for person's name
        self.age = age    # Data member for person's age

    # Method to display the person's details
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Create objects of the Person class
person1 = Person("sri", 17)
person2 = Person("kush", 18)

# Call the display_info method for each object
print("Details of person1:")
person1.display_info()

print("\nDetails of person2:")
person2.display_info()
