# Task 3: Lambda Function (GST)

gst = lambda price: price + (0.18 * price)

print(gst(100))

# Optional

gst_discount = lambda price: (price * 1.18) * 0.90

print(gst_discount(1000))