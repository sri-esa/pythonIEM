# Write a Python program to input a number and check whether it is Krishnamurthy or not, using functions and count the number of iterations used without any functions
n= int(input("Enter a number: "))
t= n
sum_of_factorials = 0
iterations = 0

while t> 0:
    iterations += 1
    d= t % 10
    
    fact = 1
    for i in range(1, d+ 1):
        fact *= i
        iterations += 1 
    
    sum_of_factorials += fact
    
    t//= 10

if sum_of_factorials == n:
    print(f"{n} is a Krishnamurthy number.")
else:
    print(f"{n} is not a Krishnamurthy number.")

print(f"Number of iterations: {iterations}")
