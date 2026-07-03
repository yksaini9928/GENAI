
# Task 4: Combined Operations

# Product list
products = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor"
]

# Categories list
categories = [
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "Accessories",
    "Electronics"
]

# Price dictionary
price_dict = {
    "Laptop": 75000,
    "Smartphone": 45000,
    "Headphones": 2500,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}
# Create catalog
catalog = []

for product, category in zip(products, categories):
    if product in price_dict:
        catalog.append((product, price_dict[product], category))

print("\nCatalog:")
for item in catalog:
    print(item)


# Create category_to_products dictionary

category_to_products = {}

for product, price, category in catalog:

    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print("\nCategory to Products:")
print(category_to_products)

# Category with maximum products

max_category = max(category_to_products, key=lambda x: len(category_to_products[x]))

print("\nCategory with Maximum Products:")
print(max_category)

print("Products:")

for product in category_to_products[max_category]:
    print(product)