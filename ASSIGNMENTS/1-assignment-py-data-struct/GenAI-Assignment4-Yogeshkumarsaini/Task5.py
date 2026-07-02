# Open file in write mode
file = open("products.txt", "w")

# Take input for 3 products
for i in range(3):
    print("Enter details for Product", i + 1)

    name = input("Product Name: ")
    price = input("Price: ")

    file.write(name + " | " + price + "\n")

file.close()

# Read and display file
file = open("products.txt", "r")

print("\n===== Product List =====")
print(file.read())

file.close()