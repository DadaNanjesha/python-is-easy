import streamlit as st
from lessons import variables, loops, functions  # Import lesson modules


def render_header(text: str) -> None:
    header_html = f"""
    <div class="custom-header">
        <h1>{"Python Is Easy"}</h1>
        <h4>{"Welcome to your interactive Python learning app!"}</h4>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)
render_header("Python Is Easy")

# Initialize session state for page selection
if 'page' not in st.session_state:
    st.session_state['page'] = 'Variables'

# Sidebar Header
st.sidebar.markdown("<h2>Topics</h2>", unsafe_allow_html=True)

# Vertical list of buttons in the sidebar
if st.sidebar.button("Variables"):
    st.session_state.page = "Variables"
if st.sidebar.button("Loops"):
    st.session_state.page = "Loops"
if st.sidebar.button("Functions"):
    st.session_state.page = "Functions"

# Optional: Display current selection
st.sidebar.markdown(f"### Current Topic: {st.session_state.page}", unsafe_allow_html=True)

# Render the corresponding lesson based on the selected page
if st.session_state.page == "Variables":
    variables.display()
elif st.session_state.page == "Loops":
    loops.display()
elif st.session_state.page == "Functions":
    functions.display()
def local_css(file_name):
    with open(file_name) as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Call the function at the top of your app
local_css("assets/styles.css")
