
# Task 3: Product Pricing (Dictionaries)


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

print("Original Price Dictionary:")
print(price_dict)


# Add a new product

price_dict["Tablet"] = 30000
print("\nAfter Adding Tablet:")
print(price_dict)


# Update an existing product price

price_dict["Laptop"] = 72000
print("\nAfter Updating Laptop Price:")
print(price_dict)


# Remove a product safely

product_to_remove = "Mouse"

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print("\nMouse removed successfully.")
else:
    print("\nProduct not found.")

print(price_dict)


# Average Price

total = 0

for price in price_dict.values():
    total += price

average = total / len(price_dict)

print("\nAverage Price =", average)


# Maximum and Minimum Price Product

max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("\nHighest Price Product:")
print(max_product, "=", price_dict[max_product])

print("\nLowest Price Product:")
print(min_product, "=", price_dict[min_product])


