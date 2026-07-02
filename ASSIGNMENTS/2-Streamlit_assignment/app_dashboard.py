import streamlit as st

# Title and Description
st.title("Simple Sales Dashboard")
st.write("This dashboard displays monthly sales data.")

# List of months
months = ["January", "February", "March", "April"]

# Dictionary of monthly sales
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

# Selectbox
selected_month = st.selectbox("Select a Month", months)

# Display selected month's sales
st.subheader("Monthly Sales")

st.metric(
    label=f"{selected_month} Sales",
    value=f"₹{sales[selected_month]}"
)

# Display bar chart
st.subheader("Sales Comparison")

st.bar_chart(list(sales.values()))

# Optional: Show sales details in a table
st.subheader("Sales Details")

table = {
    "Month": list(sales.keys()),
    "Sales": list(sales.values())
}

st.table(table)