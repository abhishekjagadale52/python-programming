import streamlit as st

def main():
    st.set_page_config(page_title="Grocery Bill Calculator", page_icon="🛒")
    
    st.title("🛒 Grocery Bill Calculator")
    st.write("Enter your items below to calculate the total.")

    # Initialize a list to store items in the session state
    if 'items' not in st.session_state:
        st.session_state.items = []

    # Input Section
    with st.form("item_form", clear_on_submit=True):
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            item_name = st.text_input("Item Name")
        with col2:
            price = st.number_input("Price", min_value=0.0, step=0.1)
        with col3:
            quantity = st.number_input("Quantity", min_value=1, step=1)
            
        submit = st.form_submit_button("Add Item")

    if submit and item_name:
        st.session_state.items.append({
            "name": item_name,
            "price": price,
            "quantity": quantity,
            "total": price * quantity
        })

    # Display Table and Calculations
    if st.session_state.items:
        st.subheader("Your Basket")
        
        # Display as a table
        grand_total = 0
        for i, item in enumerate(st.session_state.items):
            st.write(f"*{item['name']}: {item['quantity']} x ₹{item['price']:.2f} = *₹{item['total']:.2f}**")
            grand_total += item['total']
