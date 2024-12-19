#Given a list of numbers return the indices in which a specific number occurs.
def find_indices(numbers, target):
    indices = [i for i, num in enumerate(numbers) if num == target]
    return indices

# Example usage:
l = [1, 3, 7, 8, 7, 5, 6, 7]
result = find_indices(l, 7)
print(result) 
