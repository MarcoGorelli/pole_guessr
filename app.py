import streamlit as st
import random
from PIL import Image
import os

# List of image file paths (update these paths with your actual image paths)
image_list = sorted([os.path.join('images', x) for x in os.listdir('images')])

# Function to display a random image
def display_random_image():
    selected_image = random.choice(image_list)
    print(selected_image)
    image = Image.open(selected_image)
    st.image(image, width=300)

st.title("Random Image Viewer")

if st.button("Show a Random Image"):
    display_random_image()

