# Read entire file
file = open("sales_data.txt", "r")

print("Reading entire file:")
print(file.read())

file.close()


# Read first line
file = open("sales_data.txt", "r")

print("\nFirst line:")
print(file.readline().strip())

file.close()


# Read all lines
file = open("sales_data.txt", "r")

lines = file.readlines()

# Convert lines to integers
sales = []

for line in lines:
    sales.append(int(line.strip()))

print("\nSales List:")
print(sales)

file.close()