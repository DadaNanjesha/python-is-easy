# lessons/loops.py
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
            exec(code, {})  # Using an empty globals dict for a basic level of isolation.
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
    Renders the Loops lesson, including explanations, code examples, and an interactive editor.
    """
    render_header("Lesson: Loops")
    
    # Explanation similar to W3Schools style
    st.write(
        """
        Loops are used in Python to execute a block of code repeatedly. Python supports two main types of loops:
        `for` loops and `while` loops. In this lesson, we will focus on `for` loops.
        """
    )
    
    st.subheader("Example 1: Iterating Over a List")
    st.write("A `for` loop can be used to iterate over a list. For example:")
    st.code(
        """
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
        """,
        language='python'
    )
    st.write(
        """
        In this example, the `for` loop iterates over each element in the list `fruits` and prints it.
        """
    )
    
    st.subheader("Interactive Example")
    st.write("Modify the code below and run it to see how the `for` loop works with different lists or operations.")
    
    # Default code for the interactive example:
    code: str = st.text_area(
        "Try it yourself:",
        "fruits = ['apple', 'banana', 'cherry']\nfor fruit in fruits:\n    print(fruit)"
    )
    
    if st.button("Run Code"):
        result: Optional[str] = execute_and_capture(code)
        if result is not None:
            st.text_area("Output", result, height=150)
    
    st.subheader("Additional Information")
    st.write(
        """
        - **Indentation:** Python uses indentation to define blocks of code. Ensure your loop's body is indented correctly.
        - **Range Function:** You can also iterate over a sequence of numbers using the `range()` function. For example:
            ```python
            for i in range(5):
                print(i)
            ```
        - **Nested Loops:** Python supports nested loops (loops inside loops), which are useful for iterating over multi-dimensional structures.
        """
    )
