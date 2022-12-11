import streamlit as st

import random
from params import BANNERS, TITLE, LOGO, LOGO_BANNER


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

#  --- IDEA -- Like a navbar
# if st.sidebar.button('Say hello'):
#     st.sidebar.write('Why hello there')
# else:
#     st.sidebar.write('Goodbye')



# =============================================================================================================
#       Main Content
# =============================================================================================================


# st.title(TITLE)
# st.subheader('A collection of tools for game developers that aims to inspire new game ideas and consepts.')
st.image(BANNERS[random.randint(0, len(BANNERS)-1)])




with st.form("input_form"):

	st.subheader("Tell us a bit about your ideas")

	# TO organize the form internals
	col1, col2, col3 = st.columns(3)

	with col1:
		st.header("A cat")
		st.image("https://static.streamlit.io/examples/cat.jpg")

	with col2:
		st.header("A dog")
		st.image("https://static.streamlit.io/examples/dog.jpg")

	with col3:
		st.header("An owl")
		st.image("https://static.streamlit.io/examples/owl.jpg")



	# Select primary and secondary colors???
	color = st.color_picker('Pick A Color', '#00f900')

	color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
	st.write('My favorite color is', color)

	# Text inputs
	st.text_area('large text prompt', value="", height=None, placeholder="sadasd")

	title = st.text_input('Movie title', 'Life of Brian')


	slider_val = st.slider("Form slider")
	checkbox_val = st.checkbox("Form checkbox")

	# Every form must have a submit button.
	submitted = st.form_submit_button("Submit")
	if submitted:
		st.write("slider", slider_val, "checkbox", checkbox_val)

