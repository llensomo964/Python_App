import streamlit as st

st.title("Triangle Validator App")
st.write("Enter the three side measurements of a triangle to check if it's valid.")

# Get user inputs using Streamlit sliders or number inputs
a = st.number_input("Enter the measurement for side a:", min_value=1)
b = st.number_input("Enter the measurement for side b:", min_value=1)
c = st.number_input("Enter the measurement for side c:", min_value=1)

# Button to check validity
if st.button("Check Triangle"):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        st.success("The triangle is VALID")
    else:
        st.error("The triangle is INVALID")

