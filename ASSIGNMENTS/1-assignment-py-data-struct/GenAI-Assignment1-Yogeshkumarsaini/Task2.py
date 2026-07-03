# Task 2: Categories (Sets)


# Create a parallel categories list
categories = [
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "Accessories",
    "Electronics",
    "Electronics",
    "Accessories"
]

# 1. Create a set of categories
categories_set = set(categories)

print("\nCategories Set:")
print(categories_set)

# 2. Add a new category
categories_set.add("Gaming")

print("\nAfter Adding 'Gaming':")
print(categories_set)

# Add duplicate category
categories_set.add("Electronics")

print("\nAfter Adding Duplicate 'Electronics':")
print(categories_set)

# 3. Check whether a category exists
print("\nDoes 'Accessories' exist?")
print("Accessories" in categories_set)

print("\nDoes 'Furniture' exist?")
print("Furniture" in categories_set)

# Extra (Optional)
print("\nTotal Unique Categories:")
print(len(categories_set))