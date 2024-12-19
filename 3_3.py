#Create a class that will return the Fibonacci numbers sequentially every time it is called using __iter__()
class Fibonacci:
    def __init__(self):
        """
        Constructor to initialize the first two Fibonacci numbers.
        """
        self.a = 0  # First Fibonacci number
        self.b = 1  # Second Fibonacci number

    def __iter__(self):
        """
        The __iter__ method makes the object itself an iterator.
        """
        return self

    def __next__(self):
        """
        The __next__ method returns the next Fibonacci number.
        It calculates the next Fibonacci number by updating a and b.
        """
        fib = self.a
        self.a, self.b = self.b, self.a + self.b  # Update for the next Fibonacci number
        return fib

# Example usage:
fib_gen = Fibonacci()  # Create a Fibonacci sequence generator

# Get the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))
