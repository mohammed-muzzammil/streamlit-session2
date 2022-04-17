import streamlit as st
import requests

# Text to Image

# Title
st.title("Text to Image")

# INFO
st.info("This is a simple text to image converter.")

# Text Input

text = st.text_input("Enter your text here:")

if st.button("Convert"):
    # API
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': text,
        },
        headers={'api-key': '6d0a5321-5e74-4a0a-80e1-fc6a530846f5'}
    )
    # Image
    st.image(r.json()['output_url'])