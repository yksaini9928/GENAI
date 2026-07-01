
# Task 1: Product Collections


# 1. Create a list with at least 6 product names
products = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor"
]

print("Original Products List:")
print(products)

# 2. Create a tuple (product_name, price, category)
sample_product = ("Laptop", 75000, "Electronics")

print("\nSample Product Tuple:")
print(sample_product)

# 3. Print the 2nd and last product
print("\nSecond Product:", products[1])
print("Last Product:", products[-1])

# 4. Append two new products
products.append("Printer")
products.append("Webcam")

print("\nUpdated Products List:")
print(products)

# Extra (Optional)
# Convert tuple to list, change price, convert back to tuple
sample_product_list = list(sample_product)
sample_product_list[1] = 72000  # New price
sample_product = tuple(sample_product_list)

print("\nUpdated Product Tuple:")
print(sample_product)
