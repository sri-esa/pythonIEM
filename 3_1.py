#Write a Python program to define a class "Box" and write functions to calculate its volume
class Box:
    def __init__(self, length, width, height):
        """
        Constructor to initialize the dimensions of the box.
        :param length: Length of the box
        :param width: Width of the box
        :param height: Height of the box
        """
        self.length = length
        self.width = width
        self.height = height

    def calculate_volume(self):
        """
        Method to calculate the volume of the box.
        :return: Volume of the box (length * width * height)
        """
        return self.length * self.width * self.height

# Example usage:
# Create a box with specific dimensions
box = Box(10, 5, 3)

# Calculate the volume of the box
volume = box.calculate_volume()
print(f"The volume of the box is: {volume}")
