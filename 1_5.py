# Write a Python program to create a list of 20 values and find out Mean, Median and Mode of a list of numbers. Count the number of separators used.
from statistics import mean, median, mode
L =[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84]
mean_value = mean(L)
median_value = median(L)
try:
    mode_value = mode(L)
except:
    mode_value = "No unique mode"

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
separators_count = 2 #for opening and closing brackets
separators_count += len(L) - 1  #for commas
print(f"Total number of separators used: {separators_count}")
