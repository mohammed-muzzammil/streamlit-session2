import streamlit as st
import requests

# Title
st.title("Image Colorizer")

# upload image
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png"])
image = st.image(uploaded_file)


if st.button("Colorize"):
    # API
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={
            'image': uploaded_file
        },
        headers={'api-key': '6d0a5321-5e74-4a0a-80e1-fc6a530846f5'}
    )
    st.image(r.json()['output_url'])

