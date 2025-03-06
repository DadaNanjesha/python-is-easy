# lessons/variables.py
import streamlit as st
from io import StringIO
import contextlib
from typing import Optional

def execute_and_capture(code: str) -> Optional[str]:
    """
    Executes the given Python code and captures its output.

    Parameters:
        code (str): The Python code to execute.

    Returns:
        Optional[str]: The captured output if execution succeeds, or None on error.
    """
    output_buffer: StringIO = StringIO()
    try:
        with contextlib.redirect_stdout(output_buffer):
            exec(code, {})  # Using an empty globals dict for a bit of isolation
    except Exception as e:
        st.error(f"Error: {e}")
        return None
    return output_buffer.getvalue()

def render_header(text: str) -> None:
    """
    Renders a custom HTML header to highlight the lesson title.

    Parameters:
        text (str): The header text to display.
    """
    header_html: str = f"""
    <div class="custom-header">
        <h2>{text}</h2>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)
    
def display() -> None:
    """
    Renders the Variables lesson with explanations and interactive examples,
    inspired by the style of W3Schools Python Variables tutorial.
    """
    render_header("Lesson: Variables")
    
    # Explanation similar to W3Schools
    st.write(
        """
        Python variables are containers for storing data values. Unlike some other programming languages,
        Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.
        """
    )
    
    st.subheader("Example 1: Creating Variables")
    st.write("In Python, you can assign a value to a variable without declaring its type explicitly. For example:")
    st.code("x = 5\ny = 'Hello, World!'", language='python')
    st.write(
        """
        Here, the variable `x` is assigned the integer value `5`, and `y` is assigned the string value `'Hello, World!'`.
        """
    )

    st.subheader("Interactive Example")
    st.write("Try modifying the code below and see the output. You can experiment with assigning different values to variables.")
    
    # Default code for the interactive example:
    code: str = st.text_area("Try it yourself:", "x = 10\nprint('Value of x:', x)")
    
    if st.button("Run Code"):
        result: Optional[str] = execute_and_capture(code)
        if result is not None:
            st.text_area("Output", result, height=150)
    
    st.subheader("Additional Information")
    st.write(
        """
        - **Variable Names:** Variable names in Python are case-sensitive.
        - **Naming Rules:** They must start with a letter or an underscore (_), and can only contain alphanumeric characters and underscores.
        - **Dynamic Typing:** Python is dynamically-typed, which means you can reassign variables to different data types.
        """
    )
