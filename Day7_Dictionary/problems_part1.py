# Day 7: Dictionary Practice - Part 1

# Problem 1: Merge two dictionaries into one.
print("--- Problem 1: Merge Dictionaries ---")
dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 30, 'c': 40}

# In Python 3.9+, we can use the | operator to merge
merged_dict = dict1 | dict2
print("Dict 1:", dict1)
print("Dict 2:", dict2)
print("Merged Dict:", merged_dict)
print()


# Problem 2: Find the sum of all numeric values in a dictionary.
print("--- Problem 2: Sum of Values ---")
scores = {
    'math': 85,
    'science': 90,
    'english': 78,
    'history': 88
}
total_score = sum(scores.values())
print("Scores dictionary:", scores)
print("Total Score (Sum):", total_score)
print()


# Problem 3: Check if a key exists in a dictionary, print its value, and insert a default if missing.
print("--- Problem 3: Check Key and Update ---")
inventory = {
    'apples': 10,
    'bananas': 5,
    'oranges': 8
}

def check_and_update(item, default_qty):
    if item in inventory:
        print(f"'{item}' is in inventory. Quantity: {inventory[item]}")
    else:
        print(f"'{item}' is missing. Adding to inventory with default quantity: {default_qty}")
        inventory[item] = default_qty

print("Initial Inventory:", inventory)
check_and_update('bananas', 0)
check_and_update('grapes', 15)
print("Updated Inventory:", inventory)
print()
