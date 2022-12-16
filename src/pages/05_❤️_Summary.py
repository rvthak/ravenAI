import streamlit as st
import random
from params import BANNERS, TITLE, LOGO, LOGO_BANNER, API_KEY, GENRE_OPTIONS, STYLE_OPTIONS
from fpdf import FPDF

from storage import storage_init
storage_init()

import openai
openai.api_key = API_KEY

# =============================================================================================================
#       Configuration
# =============================================================================================================

st.set_page_config(
    page_title="Game Summary",
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

# =============================================================================================================
#       Main Content
# =============================================================================================================

st.image(BANNERS[random.randint(0, len(BANNERS)-1)])
st.subheader("Putting it all together...")

if st.session_state.title != "":
    st.write("## " + st.session_state.title)

if st.session_state.ai_story!="":
    st.write("## Game Story")
    st.write(st.session_state.ai_story)

if st.session_state.ai_mechanics!="":
    st.write("## Game Mechanics")
    st.write(st.session_state.ai_mechanics)

if st.session_state.ai_world_0 != "":
    st.write("## Concept art of the Game World")
    col1, col2 = st.columns(2)
    with col1:
        st.image(st.session_state.ai_world_0)
    with col2:
        st.image(st.session_state.ai_world_1)

if st.session_state.ai_char_0 != "":
    st.write("## Concept art of your character")
    col1, col2 = st.columns(2)
    with col1:
        st.image(st.session_state.ai_char_0)
    with col2:
        st.image(st.session_state.ai_char_1)


# Create a PDF report cotaining everything
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 18)
pdf.cell(200, 10, txt = TITLE,
         ln = 1, align = 'C')

if st.session_state.title != "":
    pdf.cell(200, 10, txt = st.session_state.title,
         ln = 1, align = 'C')
else:
    pdf.cell(200, 25, txt = "Your Game Title",
         ln = 1, align = 'C')

if st.session_state.ai_story!="":
    pdf.set_font("Arial", size = 18)
    pdf.cell(200, 10, txt = 'Game Story',
            ln = 1, align = 'L')
    pdf.set_font("Arial", size = 12)
    pdf.multi_cell(0, 5, st.session_state.ai_story)

if st.session_state.ai_mechanics!="":
    pdf.add_page()
    pdf.set_font("Arial", size = 18)
    pdf.cell(200, 10, txt = 'Game Mechanics',
            ln = 1, align = 'L')
    pdf.set_font("Arial", size = 12)
    text = st.session_state.ai_mechanics.encode('latin-1','ignore').decode('latin-1')
    pdf.multi_cell(0, 5, text)

# Calculate the center position of the page
center_x = pdf.w / 2

if st.session_state.ai_world_0 != "":
    pdf.add_page()
    pdf.set_font("Arial", size = 18)
    pdf.cell(200, 10, txt = 'Concept art of the Game World',
            ln = 1, align = 'C')
    pdf.image("./img/ai_world_0.png", x=center_x/2, y=40, w=100, h=100)
    pdf.image("./img/ai_world_1.png", x=center_x/2, y=160, w=100, h=100)

if st.session_state.ai_char_0 != "":
    pdf.add_page()
    pdf.set_font("Arial", size = 18)
    pdf.cell(200, 10, txt = 'Concept art of your character',
            ln = 1, align = 'C')
    pdf.image("./img/ai_char_0.png", x=center_x/2, y=40, w=100, h=100)
    pdf.image("./img/ai_char_1.png", x=center_x/2, y=160, w=100, h=100)

pdf.output("result.pdf")  

col1, col2, col3 = st.columns(3)
with col2:
    with open("result.pdf", "rb") as file:
        btn = st.download_button(
                label="Download Summary PDF",
                data=file,
                file_name="results.pdf",
                mime="application/pdf"
            )