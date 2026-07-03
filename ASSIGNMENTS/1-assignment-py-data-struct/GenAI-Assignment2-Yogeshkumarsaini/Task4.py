# Task 5: Loop Control

daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily:

    if sale == -1:
        print("Corrupted data found.")
        break

    if sale == 0:
        print("No sales today.")
        continue

    total_sales += sale

    print("Today's Sale:", sale)
    print("Running Total:", total_sales)

print("\nFinal Total Sales:", total_sales)