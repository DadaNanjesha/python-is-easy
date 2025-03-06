# lessons/functions.py
import streamlit as st
from io import StringIO
import contextlib
from typing import Optional

def execute_and_capture(code: str) -> Optional[str]:
    """
    Executes the provided Python code and captures its output.

    Parameters:
        code (str): The Python code to execute.

    Returns:
        Optional[str]: The captured output as a string if successful, otherwise None.
    """
    output_buffer: StringIO = StringIO()
    try:
        with contextlib.redirect_stdout(output_buffer):
            exec(code, {})  # Using an empty globals dict for basic isolation.
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
    Renders the Functions lesson, including explanations, examples, and an interactive code editor.
    """
    render_header("Lesson: Functions")
    
    st.write(
        """
        Functions are blocks of code that perform a specific task and can be reused throughout your program.
        They help break down complex problems into smaller, manageable pieces. In Python, functions are defined
        using the `def` keyword.
        """
    )
    
    st.subheader("Example 1: Defining and Calling a Function")
    st.write("Below is an example of a simple function that prints a greeting:")
    st.code(
        """
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
        """,
        language='python'
    )
    st.write(
        """
        In this example, the function `greet()` takes a parameter `name` and prints a greeting message.
        """
    )
    
    st.subheader("Interactive Example")
    st.write("Try modifying the code below to create and call your own function.")
    
    # Default code for the interactive example
    code: str = st.text_area(
        "Try it yourself:",
        "def greet(name):\n    print('Hello, ' + name + '!')\n\ngreet('Bob')"
    )
    
    if st.button("Run Code"):
        result: Optional[str] = execute_and_capture(code)
        if result is not None:
            st.text_area("Output", result, height=150)
    
    st.subheader("Additional Information")
    st.write(
        """
        - **Parameters and Arguments:** Functions can accept parameters (inputs) and can also return a value.
        - **Return Statement:** Use the `return` keyword to output a value from a function.
        - **Built-in Functions:** Python offers many built-in functions such as `print()`, `len()`, and others.
        - **Docstrings:** It's good practice to document your functions with docstrings to explain their purpose.
        """
    )
