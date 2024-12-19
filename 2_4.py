#Implement the following functions/methods which operates on lists in Python with suitable examples: list() i len() ii, count() iv. index() append() V. vi. insert() vii. extend() viii. remove() ix. pop() X. reverse() xi. sort() xii. copy[) xii. clear()
# 1. list(): Create a list
L = list([1, 2, 3, 4, 5])
print("1. list() =>", L)

# 2. len(): Get the length of the list
length = len(L)
print("2. len() =>", length)

# 3. count(): Count occurrences of a value
L.append(3)  # Adding another 3 to count its occurrences
count_3 = L.count(3)
print("3. count(3) =>", count_3)

# 4. index(): Find the first index of a value
index_4 = L.index(4)
print("4. index(4) =>", index_4)

# 5. append(): Add an element to the end of the list
L.append(17)
print("5. append(17) =>", L)

# 6. insert(): Insert an element at a specific index
L.insert(3,6)
print("6. insert(3,6) =>", L)

# 7. extend(): Extend the list by appending elements from another list
L.extend([8, 9])
print("7. extend([8, 9]) =>", L)

# 8. remove(): Remove the first occurrence of a specific value
L.remove(3)
print("8. remove(3) =>", L)

# 9. pop(): Remove and return the element at the specified index (default is the last element)
popped_value = L.pop()  # Popping the last element
print("9. pop() =>", L, ", popped value =", popped_value)

# 10. reverse(): Reverse the list
L.reverse()
print("10. reverse() =>", L)

# 11. sort(): Sort the list (ascending by default)
L.sort()
print("11. sort() =>", L)

# 12. copy(): Create a shallow copy of the list
copied_list = L.copy()
print("12. copy() =>", copied_list)

# 13. clear(): Remove all elements from the list
L.clear()
print("13. clear() =>", L)
