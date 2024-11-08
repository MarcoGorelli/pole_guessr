import streamlit as st
import random
from PIL import Image
import os

st.page_link("https://github.com/MarcoGorelli/pole_guessr", label="Source code")

# List of image file paths (update these paths with your actual image paths)
image_list = sorted([os.path.join('images', x) for x in os.listdir('images')])

# Initialize session state variables
if "current_image" not in st.session_state:
    st.session_state.current_image = None
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# Define a function to display a random image
def display_random_image():
    st.session_state.current_image = random.choice(image_list)
    st.session_state.show_answer = False

# Display a button to show a random image
if st.button("Display Random Image"):
    display_random_image()
# Button to show the answer (file name of the image)
if st.button("Show Answer"):
    st.session_state.show_answer = True

# Display the selected image if available
if st.session_state.current_image:
    image = Image.open(st.session_state.current_image)
    st.image(image, width=300)


# Display the filename if 'Show Answer' was pressed
if st.session_state.show_answer and st.session_state.current_image:
    st.write("Country:", st.session_state.current_image.split('/')[1].split('_')[0])

# Footer link
st.markdown("---")  # A separator line
st.markdown(
    "<div style='text-align: center;'>"
    "<a href='https://github.com/MarcoGorelli/pole_guessr' target='_blank'>"
    "View Source Code on GitHub</a>"
    "</div>",
    unsafe_allow_html=True
)
