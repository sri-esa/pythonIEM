#Implement the following functions/methods which operates on tuples in Python with suitable examples:i. len() ii.count() iii. index() iv. sorted() v. min() & max() Vi. cmp() vii. reversed()
'''
A = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)
# 1. len(): Get the length of the tuple
length = len(A)
print("1. len() =>", length)

# 2. count(): Count occurrences of a value
count_1 = A.count(1)
print("2. count(1) =>", count_1)

# 3. index(): Find the first index of a value
index_5 = A.index(5)
print("3. index(5) =>", index_5)

# 4. sorted(): Return a sorted list of the tuple elements
sorted_tuple = sorted(A)
print("4. sorted() =>", sorted_tuple)

# 5. min() and max(): Find the minimum and maximum elements in the tuple
min_value = min(A)
max_value = max(A)
print("5. min() =>", min_value)
print("6. max() =>", max_value)

# 6. cmp(): Compare two tuples (Note: cmp() is not available in Python 3.x)
# You can simulate comparison using standard operators
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
comparison = tuple1 < tuple2  # Simulating comparison (returns True if tuple1 is less than tuple2)
print("7. cmp() simulation (tuple1 < tuple2) =>", comparison)

# 7. reversed(): Return a reversed iterator of the tuple elements
reversed_tuple = tuple(reversed(A))
print("8. reversed() =>", reversed_tuple)
'''
A=(3,1,4,1,5,9,2,6,5,3,1)
print("i. len()=>",len(A))
print("ii. count(1)=>",A.count(1))
print("iii. index(5)=>",A.index(5))
print("iv. sorted()=>",sorted(A))
print("v. min()=>",min(A))
print("v. max()=>",max(A))
print("vii. reversed()=>",tuple(reversed(A)))
tu_ple=(1,2,3)
tup_le=(1,2,4)
print("vi. cmp() simulation (tu_ple<tup_le)=>",tu_ple<tup_le) #cmp() not available in python 3.x