# Task 2: Process Multiple Orders

orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders = 0

print("Order\tDiscount\tFinal Amount")

for order in orders:

    if order >= 2000:
        discount = 15
    elif order >= 1500:
        discount = 10
    elif order >= 1000:
        discount = 7
    else:
        discount = 0

    if discount > 0:
        discounted_orders += 1

    final_amount = order - (order * discount / 100)
    total_revenue += final_amount

    print(order, "\t", str(discount) + "%", "\t\t", final_amount)

print("\nTotal Revenue:", total_revenue)
print("Orders with Discount:", discounted_orders)