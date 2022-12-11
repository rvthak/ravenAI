import streamlit as st
import openai
import os
from dotenv import load_dotenv
import requests

# API key is stored in a .env file as OPENAI_API_KEY="sk-..."
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

image_description = 'Cat playing with a ball of yarn in a playground'

# create a new image with gicen description
response = openai.Image.create(
    prompt = image_description,
    n=1,
    size = "256x256"
)
image_url = response['data'][0]['url']

print(image_url)
st.write("# Created image")
st.image(image_url)

# Download the image from the URL
img_data = requests.get(image_url)

# Save the image to a file
with open("../img/temp.png", "wb") as f:
    f.write(img_data.content)

# # create variation of that image 
# response_variation = openai.Image.create_variation(
#   image=open("temp.png", "rb"),
#   n=1,
#   size="256x256"
# )
# image_url_variation = response_variation['data'][0]['url']
# st.write("# Variation of that image")
# st.image(image_url_variation)

# # Download the image from the URL
# img_data = requests.get(image_url_variation)

# # Save the image to a file
# with open("temp_variation.png", "wb") as f:
#     f.write(img_data.content)