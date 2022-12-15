import streamlit as st
import random
from params import BANNERS, TITLE, LOGO, LOGO_BANNER, API_KEY, GENRE_OPTIONS, STYLE_OPTIONS
from utils import multiselect_to_string, save_image

from storage import storage_init
storage_init()

import openai
openai.api_key = API_KEY

# =============================================================================================================
#       Configuration
# =============================================================================================================

st.set_page_config(
    page_title="AI Character Generator",
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

	st.subheader("Meet the people that inhabit your game world!")
	st.write("Visualize how the characters of your game look like. On this page you can create your protagonist, civilians, heroes, villains, gods, and everyone else that lives in your world.")

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

	character_description = st.text_area("Describe your character's appearance. What are his unique characteristics?", value=st.session_state.character_description, height=None, placeholder="ex. An enthusiastic 10 year old with black messy hair.")

	character_apparel = st.text_area('What is your character wearing?', value=st.session_state.character_apparel, height=None, placeholder="ex. He is wearing a red hat turned around, a blue jacket, jeans and a pair of green gloves.")

	character_weapons = st.text_area('Does the character have weapos? What weapons does he have?', value=st.session_state.character_weapons, height=None, placeholder="ex. He doesn't have any weapons. His only defence is his trusted sidekick Pikachu, that is always by his side.")

	character_skills = st.text_area('What skills does this character have?', value=st.session_state.character_skills, height=None, placeholder="ex. He is persistent, has strong will and doesn't age apparently.")

	character_story = st.text_area('What is the backstory of your character?', value=st.session_state.character_story, height=None, placeholder="ex. He left his home at 10 years old in order to chase his dream of becoming the region's champion. In order to achieve this, he has been enslaving helpless animals and forcing them to fight each other and become stronger.")

	other_prompts = st.text_area('Other prompts', value=st.session_state.other_prompts_char, height=None, placeholder="Other ideas you may have, or advanced prompts")

	# Every form must have a submit button.
	submitted = st.form_submit_button("Submit")
	if submitted:

		# Store changes on session storage
		st.session_state.style_option = style_option
		st.session_state.other_style = other_style
		st.session_state.perspective = perspective
		st.session_state.character_description = character_description
		st.session_state.character_apparel = character_apparel
		st.session_state.character_weapons = character_weapons
		st.session_state.character_skills = character_skills
		st.session_state.character_story = character_story
		st.session_state.other_prompts_char = other_prompts

		# Generate Dall-e 2 prompt based on the user input
		prompt = "Imagine the a video game character. "

		if style_option != "" or other_style != "":
			prompt += "The game's art style is: " + multiselect_to_string(style_option, other_style) + ". "

		if perspective != "":
			prompt += "The game;s perspective is " + multiselect_to_string(perspective, "") + ". "

		if character_description != "":
			prompt += character_description + ". "

		if character_apparel != "":
			prompt += "His clothes are: " + character_apparel + ". "
		
		if character_weapons != "":
			prompt += "His weapons are: " + character_weapons + ". "
		
		if character_skills != "":
			prompt += "His skills are: " + character_skills + ". "
		
		if character_story != "":
			prompt += "His backstory is: " + character_story + ". "

		if other_prompts != "":
			prompt += other_prompts + ". "
		
		# st.write(prompt)

		# Send the prompt to GPT and display the response
		try:
		
			with st.spinner('Thinking about your character...'):
				response = openai.Image.create(
					prompt = prompt[:1000],
					n=2,
					size = "1024x1024"
				)

				ai_char_0 = response['data'][0]['url']
				ai_char_1 = response['data'][1]['url']

				# Store the response for later
				st.session_state.ai_char_0 = ai_char_0
				st.session_state.ai_char_1 = ai_char_1

				# Store the images
				save_image(ai_char_0, "ai_char_0")
				save_image(ai_char_1, "ai_char_1")

		except:
			st.error('Failed to generate concept art for your provided promp.', icon="🚨")
			pass

if st.session_state.ai_char_0 != "":
	st.write("## Concept art of your character")
	col1, col2 = st.columns(2)
	with col1:
		st.image(st.session_state.ai_char_0)
	with col2:
		st.image(st.session_state.ai_char_1)