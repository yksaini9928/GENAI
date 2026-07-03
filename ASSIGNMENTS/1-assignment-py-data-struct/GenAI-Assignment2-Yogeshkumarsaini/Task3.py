# Task 3: User Menu

orders = []

while True:

    print("\n------ MENU ------")
    print("1. Add Order")
    print("2. Show Orders")
    print("q. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter order amount: "))
        orders.append(amount)
        print("Order Added.")

    elif choice == "2":

        if len(orders) == 0:
            print("No orders available.")
            continue

        total = 0

        print("\nOrders")

        for order in orders:

            if order >= 2000:
                discount = 15
            elif order >= 1500:
                discount = 10
            elif order >= 1000:
                discount = 7
            else:
                discount = 0

            final = order - order * discount / 100
            total += final

            print("Order:", order,
                  "Discount:", str(discount) + "%",
                  "Final:", final)

        print("Total:", total)

    elif choice.lower() == "q":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
        continue