odds = set([1,3,5,7,9])
even = set([2,4,6,8])
prime = set([2,3,5,7])
composites = set([4,6,8,9,10])

print(odds)
print(composites)
print(even.intersection(composites))
print(prime.intersection(odds))

#practice test
# Test on Sets

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. Print the union of set1 and set2
print("1. Union of set1 and set2:")
# Your code here
print(set1.intersection(set2))
# 2. Print the intersection of set1 and set2
print("\n2. Intersection of set1 and set2:")
# Your code here
print(set1.intersection(set2))
# 3. Print the difference between set1 and set2
print("\n3. Difference between set1 and set2:")
# Your code here
print(set1-set2)
# 4. Print the symmetric difference between set1 and set2
print("\n4. Symmetric difference between set1 and set2:")
# Your code here
print(set1.symmetric_difference(set2))
# 5. Check if set1 is a subset of set2
print("\n5. Is set1 a subset of set2?")
# Your code here
print(set1.issubset(set2))
# 6. Check if set2 is a superset of set1
print("\n6. Is set2 a superset of set1?")
# Your code here
print(set2.issuperset(set1))

# 7. Add an element 9 to set1
print("\n7. Add an element 9 to set1:")
# Your code here
set1.add(9)
print(set1)
# 8. Remove an element 4 from set2
print("\n8. Remove an element 4 from set2:")
# Your code here
set2.remove(4)
print(set2)

# 9. Check if 3 is present in set1
print("\n9. Is 3 present in set1?")
# Your code here
print(3 in set1 )

# 10. Find the length of set1
print("\n10. Length of set1:")
# Your code here
print (len(set1))


#2. example
# Test on Sets

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. Print the union of set1 and set2
print("1. Union of set1 and set2:")
# Your code here
print(set1.intersection(set2))
# 2. Print the intersection of set1 and set2
print("\n2. Intersection of set1 and set2:")
# Your code here
print(set1.intersection(set2))

# 3. Print the difference between set1 and set2
print("\n3. Difference between set1 and set2:")
# Your code here
print(set1-set2)

# 4. Print the symmetric difference between set1 and set2
print("\n4. Symmetric difference between set1 and set2:")
# Your code here
print(set1.symmetric_difference(set2))
# 5. Check if set1 is a proper subset of set2
print("\n5. Is set1 a proper subset of set2?")
# Your code here
print(set1.issubset(set2))
# 6. Check if set2 is a proper superset of set1
print("\n6. Is set2 a proper superset of set1?")
# Your code here
print(set2.issuperset(set1))
# 7. Add an element 6 to set1
print("\n7. Add an element 6 to set1:")
# Your code here
set1.add(6)
print(set1)
# 8. Remove an element 7 from set2 if it exists
print("\n8. Remove an element 7 from set2:")
# Your code here
set2.remove(7)
print(set2)


# 9. Check if all elements of set1 are present in set2
print("\n9. Are all elements of set1 present in set2?")
# Your code here
print(set1 in set2)
# 10. Find the maximum element in set2
print("\n10. Maximum element in set2:")
# Your code here
print(max in set2)

#3. Example
# Test on Sets

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. Print the union of set1 and set2
print("1. Union of set1 and set2:")
# Your code here
print(set1.union(set2))

# 2. Print the intersection of set1 and set2
print("\n2. Intersection of set1 and set2:")
# Your code here
print(set1.intersection(set2))
# 3. Print the difference between set1 and set2
print("\n3. Difference between set1 and set2:")
# Your code here
print(set1-set2)
# 4. Print the symmetric difference between set1 and set2
print("\n4. Symmetric difference between set1 and set2:")
# Your code here
print(set1.symmetric_difference(set2))
# 5. Check if set1 is a proper subset of set2
print("\n5. Is set1 a proper subset of set2?")
# Your code here
is_proper_subset =set1<set2
print(is_proper_subset)
# 6. Check if set2 is a proper superset of set1
print("\n6. Is set2 a proper superset of set1?")
# Your code here
is_proper_superset = set2>set1
print(is_proper_superset)

# 7. Add elements 6 and 7 to set1
print("\n7. Add elements 6 and 7 to set1:")
# Your code here
set1 !=(6,7)
print(set1)
# 8. Remove any common elements between set1 and set2
print("\n8. Remove any common elements between set1 and set2:")
# Your code here
set1 -= set2
print(set1)
# 9. Check if all elements of set1 are present in set2
print("\n9. Are all elements of set1 present in set2?")
# Your code here
print(set1 in set2)
# 10. Find the maximum element in set2
print("\n10. Maximum element in set2:")
# Your code here
print(max in set2)