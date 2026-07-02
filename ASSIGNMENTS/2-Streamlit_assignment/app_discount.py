import streamlit as st

# Title
st.title("Price Calculator")

# Product price input
price = st.number_input(
    "Enter Product Price:",
    min_value=0.00,
    value=1000.00,
    step=500.00
)

# Discount slider
discount = st.slider(
    "Select Discount Percentage:",
    min_value=0,
    max_value=50,
    value=10
)

# Calculate button
if st.button("Calculate"):
    discount_amount = price * discount / 100
    final_price = price - discount_amount

    # Display result
    st.success(f"Final Price: ₹{final_price:.2f}")

    st.write(f"**Original Price:** ₹{price:.2f}")
    st.write(f"**Discount:** {discount}%")
    st.write(f"**Discount Amount:** ₹{discount_amount:.2f}")

    # Comparison table (Optional)
    st.subheader("Price Comparison")

    table = [
        ["Before Discount", f"₹{price:.2f}"],
        ["After Discount", f"₹{final_price:.2f}"]
    ]

    st.table(table)