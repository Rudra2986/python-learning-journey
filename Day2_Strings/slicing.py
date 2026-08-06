# Reverse String
s = "python"
s = s[::-1]
print(s)

# First Half of a String
a = "python"
print(a[:3])

# Second Half
s = "abcdef"
print(s[3:])

# Remove First Character
s = "python"
print(s[1:])

# Remove Last Character
s = "python"
print(s[:-1])

# Every Second Character
s = "abcdefgh"
print(s[::2])

# Every Second Character (Starting from Index 1)
s = "abcdefgh"
print(s[1::2])

# Reverse Every Second Character
s = "abcdefgh"
print(s[::-2])

# Middle Characters
s = "python"
print(s[2:5])

# Copy Entire String
s = "python"
copy = s[:]
print(copy)

# Reverse First Half
s = "abcdef"

first = s[:3][::-1]
second = s[3:]

print(first + second)

# Check Palindrome
s = "madam"
print(s == s[::-1])

# Remove Middle Character
s = "python"
mid = len(s) // 2
print(s[:mid] + s[mid+1:])

# Swap First and Last Character
s = "python"
new = s[-1] + s[1:-1] + s[0]
print(new)

# Reverse Every Word
sentence = "I Love Python"
words = sentence.split()
for word in words:
    print(word[::-1], end=" ")