# New sales values
new_sales = [5000, 2500, 1700]

# Open file in append mode
file = open("sales_data.txt", "a")

# Append each sale
for sale in new_sales:
    file.write(str(sale) + "\n")

file.close()


# Reopen and display updated contents
file = open("sales_data.txt", "r")

print("Updated File Contents:")
print(file.read())

file.close()


# Count total number of lines
file = open("sales_data.txt", "r")

lines = file.readlines()

print("Total number of sales records:", len(lines))

file.close()