import streamlit as st

st.set_page_config(page_title="Planted In Nutrition", page_icon="🌱")

st.title("Planted In Nutrition 🌱")
st.markdown("""
Welcome to the Planted In Nutrition App!
This is a placeholder Streamlit app. 
Customize this with your nutrition content, calculators, blog, or interactive modules.
""")

# Optionally show HTML or text files from your repo
try:
    with open("README.md") as file:
        st.markdown(file.read())
except Exception:
    st.info("Add a README.md for more info on this project.")

# Sample input
user_food = st.text_input("Enter a food to get nutrition facts:")
if user_food:
    st.success(f"Nutritional facts for **{user_food}** coming soon!")
