# Open the file
file = open("sales_data.txt", "r")

# Read all lines
lines = file.readlines()
file.close()

# Convert to integers
sales = []

for line in lines:
    sales.append(int(line.strip()))

# Calculate summary
total = sum(sales)
highest = max(sales)
lowest = min(sales)
average = total / len(sales)

# Display summary
print("===== Sales Summary =====")
print("Total Sales   :", total)
print("Highest Sale  :", highest)
print("Lowest Sale   :", lowest)
print("Average Sale  :", average)