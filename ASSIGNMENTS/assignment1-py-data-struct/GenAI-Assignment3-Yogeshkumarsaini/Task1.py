# Task 1: Price After Discount

def apply_discount(price, discount_percent=5):
    if discount_percent > 60:
        discount_percent = 60

    final_price = price - (price * discount_percent / 100)
    return final_price


print("Discounted Price:", apply_discount(1000, 10))
print("Default Discount:", apply_discount(500))