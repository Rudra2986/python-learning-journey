# Create a set
numbers = {10, 20, 30, 40}
print(numbers)

# Empty set
empty_set = set()
print(empty_set)

# Duplicates are removed automatically
duplicate_numbers = {1, 2, 2, 3, 3, 4}
print(duplicate_numbers)

# Add an element
numbers.add(50)
print(numbers)

# Remove an element
numbers.remove(20)
print(numbers)

# Check if an element exists
if 30 in numbers:
    print("30 Found")

# Loop through a set
for item in numbers:
    print(item)

# Remove duplicates from a list
nums = [1, 2, 2, 3, 4, 4, 5]
unique = set(nums)
print(unique)

# Convert set back to list
unique_list = list(unique)
print(unique_list)

# Union
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)

# Intersection
print(A & B)

# Difference
print(A - B)

# Reverse Difference
print(B - A)

# Things sets can't do

# numbers[0]          # ❌ No indexing

# numbers[1:3]        # ❌ No slicing

# numbers.append(10)  # ❌ append() doesn't exist

# numbers.sort()      # ❌ sort() doesn't exist

# Sets are unordered.
# Duplicate values are automatically removed.