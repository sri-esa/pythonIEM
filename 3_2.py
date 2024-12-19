#Write a program to define a class "Car" and necessary functions to calculate the velocity given starting velocity (input), acceleration (member variable) and time of acceleration(input)
class Car:
    def __init__(self, acceleration):
        """
        Constructor to initialize the car with a constant acceleration.
        :param acceleration: The acceleration of the car (in meters per second squared, m/s^2)
        """
        self.acceleration = acceleration

    def calculate_velocity(self, initial_velocity, time):
        """
        Method to calculate the final velocity of the car using the formula:
        final_velocity = initial_velocity + (acceleration * time)
        
        :param initial_velocity: The starting velocity of the car (in meters per second, m/s)
        :param time: The time during which the car accelerates (in seconds, s)
        :return: The final velocity (in meters per second, m/s)
        """
        final_velocity = initial_velocity + (self.acceleration * time)
        return final_velocity

# Example usage:
# Initialize a car object with an acceleration of 3 m/s^2
car = Car(acceleration=3)

# Input initial velocity and time
initial_velocity = 10  # Initial velocity in m/s
time = 5  # Time of acceleration in seconds

# Calculate the final velocity
final_velocity = car.calculate_velocity(initial_velocity, time)
print(f"The final velocity of the car is: {final_velocity} m/s")
