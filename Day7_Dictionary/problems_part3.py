# Day 7: Dictionary Practice - Part 3

# Problem 6: Find the keys with the highest and lowest values in a dictionary.
print("--- Problem 6: Max and Min Value ---")
product_prices = {
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 75,
    "Monitor": 300,
    "USB Cable": 10
}

max_product = max(product_prices, key=product_prices.get)
min_product = min(product_prices, key=product_prices.get)

print("Product Prices:", product_prices)
print(f"Most Expensive: {max_product} (${product_prices[max_product]})")
print(f"Cheapest: {min_product} (${product_prices[min_product]})")
print()


# Problem 7: Filter dictionary key-value pairs based on a threshold (e.g. scores > 80).
print("--- Problem 7: Value Filter ---")
student_scores = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 93,
    "David": 65,
    "Eva": 89
}

threshold = 80
passed_students = {name: score for name, score in student_scores.items() if score > threshold}

print("Student Scores:", student_scores)
print(f"Students who scored > {threshold}:", passed_students)
print()


# Problem 8: Group a list of integers into lists of even and odd numbers within a dictionary.
print("--- Problem 8: Even/Odd Grouping ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

grouped_numbers = {
    "even": [],
    "odd": []
}

for num in numbers:
    if num % 2 == 0:
        grouped_numbers["even"].append(num)
    else:
        grouped_numbers["odd"].append(num)

print("Numbers List:", numbers)
print("Grouped Dictionary:", grouped_numbers)
print()
