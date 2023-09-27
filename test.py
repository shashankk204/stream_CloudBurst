import streamlit as st
from Index import render as page1_render
from page1 import render as page2_render

# Create a dictionary to map page names to their respective render functions
pages = {
    "Page 1": page1_render,
    "Page 2": page2_render,
}

# Sidebar navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
pages[selected_page]()
