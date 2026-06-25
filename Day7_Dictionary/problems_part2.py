# Day 7: Dictionary Practice - Part 2

# Problem 4: Generate a dictionary of word lengths from a list of words.
print("--- Problem 4: Word Lengths ---")
words = ["apple", "banana", "cherry", "date", "fig"]

word_lengths = {word: len(word) for word in words}
print("Words List:", words)
print("Word Lengths Dict:", word_lengths)
print()


# Problem 5: Swap keys and values of a dictionary (invert dictionary).
print("--- Problem 5: Key-Value Swap (Invert) ---")
original_dict = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 2  # Note: duplicate values will result in one key overwriting another in the inverted dict
}

# Standard dictionary comprehension to swap
inverted_dict = {value: key for key, value in original_dict.items()}
print("Original Dict:", original_dict)
print("Inverted Dict (Values to Keys):", inverted_dict)
print()
