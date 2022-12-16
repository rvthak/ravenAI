import streamlit as st
import random
from params import BANNERS, TITLE, LOGO, LOGO_BANNER, GENRE_OPTIONS, STYLE_OPTIONS
from utils import multiselect_to_string, save_image

from storage import storage_init
storage_init()

import openai
openai.api_key = st.secrets["openai_api_key"]

# =============================================================================================================
#       Configuration
# =============================================================================================================

st.set_page_config(
    page_title="AI World Generator",
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


with st.form("input_form"):

	st.subheader("How do you imagine the world of your game?")
	st.write("Visualize the world where your game takes place.")

	col1, col2 = st.columns(2)

	with col1:
		style_option = st.multiselect(
		'Art Style',
		STYLE_OPTIONS,
		st.session_state.style_option
		)

		perspective = st.multiselect(
		'Perspective',
		["", "2D", "3D", "Isometric"],
		st.session_state.perspective
		)

	with col2:
		other_style = st.text_input('Complementary Art Style', value=st.session_state.other_style)

	world_setting = st.text_area('Describe the world of your game', value=st.session_state.world_setting, height=None, placeholder="ex. The Mushroom Kindom. A Magical place inhabited by tiny mushroom men.")

	other_prompts = st.text_area('Other prompts', value=st.session_state.other_prompts_world, height=None, placeholder="Other ideas you may have, or advanced prompts")

	with st.expander("More Options"):

		st.write("Choosing a primary and secondary color for the concept art can result in better concept art. (Usually works better for 2D games)")
		prim_color = st.select_slider(
		'Pick A Primary Color for your concept art', 
		options=['None', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'],
		value=st.session_state.prim_color)

		sec_color = st.select_slider(
		'Pick A Secondary Color for your concept art',
		options=['None', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'],
		value=st.session_state.sec_color)


	# Every form must have a submit button.
	submitted = st.form_submit_button("Submit")
	if submitted:

		# Store changes on session storage
		st.session_state.style_option = style_option
		st.session_state.other_style = other_style
		st.session_state.perspective = perspective
		st.session_state.world_setting = world_setting
		st.session_state.other_prompts_world = other_prompts
		st.session_state.prim_color = prim_color
		st.session_state.sec_color = sec_color


		# Generate Dall-e 2 prompt based on the user input
		prompt = "Imagine the world of a video game. "

		if style_option != "" or other_style != "":
			prompt += "The game's art style is: " + multiselect_to_string(style_option, other_style) + ". "

		if perspective != "":
			prompt += "The game;s perspective is " + multiselect_to_string(perspective, "") + ". "

		if world_setting != "":
			prompt += "A description of the game's world is: " + world_setting + ". "

		if other_prompts != "":
			prompt += other_prompts + ". "

		if prim_color != "None":
			prompt += "The primary color should be " + prim_color + ". "
		
		if sec_color != "None":
			prompt += "The secondary color should be " + sec_color + ". "
		
		# st.write(prompt)

		# Send the prompt to GPT and display the response
		try:
		
			with st.spinner('Drawing your world...'):
				response = openai.Image.create(
					prompt = prompt[:1000],
					n=2,
					size = "1024x1024"
				)

				ai_world_0 = response['data'][0]['url']
				ai_world_1 = response['data'][1]['url']

				# Store the response for later
				st.session_state.ai_world_0 = ai_world_0
				st.session_state.ai_world_1 = ai_world_1

				# Store the images
				save_image(ai_world_0, "ai_world_0")
				save_image(ai_world_1, "ai_world_1")

		except:
			st.error('Failed to generate concept art for your provided promp.', icon="🚨")
			pass


if st.session_state.ai_world_0 != "":
	st.write("## Concept art of the Game World")
	col1, col2 = st.columns(2)
	with col1:
		st.image(st.session_state.ai_world_0)
	with col2:
		st.image(st.session_state.ai_world_1)

