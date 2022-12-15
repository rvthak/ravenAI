import streamlit as st
import os
import random
from params import BANNERS, TITLE, LOGO, LOGO_BANNER, API_KEY, GENRE_OPTIONS, STYLE_OPTIONS

from storage import storage_init
storage_init()

import openai
openai.api_key = API_KEY

# =============================================================================================================
#       Configuration
# =============================================================================================================

st.set_page_config(
    page_title=TITLE,
    page_icon=LOGO,
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "Built with ❤️ by the RavenAI team"
    }
)
	
# =============================================================================================================
#       Sidebar
# =============================================================================================================

st.sidebar.image(LOGO_BANNER)
st.sidebar.title(TITLE)
st.sidebar.subheader('A collection of AI tools for game developers that aims to inspire new game ideas and consepts.')

# random_button = st.sidebar.button('Need inspiration? Start with a random story!')



# =============================================================================================================
#       Main Content
# =============================================================================================================

st.image(BANNERS[random.randint(0, len(BANNERS)-1)])

st.subheader("What is the " + TITLE +"?") # AI Assisted game design tool

st.write("Game developers often face the challenge of coming up with unique and engaging game ideas, as well as organizing their thoughts and design elements in a cohesive manner.")
st.write("We developed " + TITLE + " in order to tackle these challeges by harvesting the catabilities of OpenAI's GPT-3 and DALL-E 2.")

st.subheader("What is GPT-3?")
st.write("GPT-3, also known as Generative Pretrained Transformer 3, is a state-of-the-art language processing model that can generate human-like text based on a given prompt. This makes it ideal for generating game ideas and concepts, as well as for organizing and refining those ideas into a coherent game design.")

st.subheader("What is DALL-E 2?")
st.write("DALL-E 2, on the other hand, is a powerful artificial intelligence model that can generate images from text descriptions. This can be extremely useful for game developers, as it allows them to quickly visualize their game concepts and design elements, helping them to better understand and refine their ideas.")

st.subheader("How does it work?") # Instructions
st.write("Brainstorming ideas for game design is now easy! Simply select what you want to get ideas for from the sidebar, and fill in the form with any ideas that you may have. Press the button and.. Done!")
st.write('Behind the scenes, your inputs get processed and then passed to the AI models to get the final results.')
st.write("The tools are designed to complement each other in order to create a cohesive vision in the end, but they can also be used individually")
