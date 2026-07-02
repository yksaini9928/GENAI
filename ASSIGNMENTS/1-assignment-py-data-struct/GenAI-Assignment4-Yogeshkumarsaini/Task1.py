# List of sales amounts
sales = [1200, 450, 980, 1500, 3000]

# Open file in write mode
file = open("sales_data.txt", "w")

# Write each sale on a new line
for sale in sales:
    file.write(str(sale) + "\n")

# Close the file
file.close()

# Reopen the file and print its contents
file = open("sales_data.txt", "r")

print("Contents of sales_data.txt:")
print(file.read())

file.close()