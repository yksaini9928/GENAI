import streamlit as st

# Title
st.title("Product Form")

# Sidebar Inputs
st.sidebar.header("Enter Product Details")

product_name = st.sidebar.text_input("product name")

product_price = st.sidebar.number_input("product price", min_value=0.00, value=1000.00, step=500.00)

product_category = st.sidebar.selectbox("product category", ["Electronics", "Clothing", "Home Appliances", "Books", "Other"])

if st.sidebar.button("Add Product"):
    st.sidebar.success("Product details submitted successfully!")
    

    st.subheader("Product Details")

    product_details = {
        "Field": [
            "Product Name",
            "Category",
            "Price"
        ],
        "Value": [
            product_name,
            product_category,
            f"₹{product_price:.2f}"
        ]
    }

    st.table(product_details)
