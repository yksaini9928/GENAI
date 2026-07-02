prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = float(input("Enter discount percentage: "))

file = open("discount_report.txt", "w")

file.write("Product | Original Price | Discounted Price\n")
file.write("-------------------------------------------\n")

total_discounted = 0

for product in prices:

    original = prices[product]
    discounted = original - (original * discount / 100)

    total_discounted += discounted

    file.write(
        product + " | " +
        str(original) + " | " +
        str(round(discounted, 2)) + "\n"
    )

average = total_discounted / len(prices)

file.write("\n")
file.write("Total Items: " + str(len(prices)) + "\n")
file.write("Average Discounted Price: " + str(round(average, 2)))

file.close()

# Read and print report
file = open("discount_report.txt", "r")

print(file.read())

file.close()