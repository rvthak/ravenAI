import streamlit as st
import random
from params import BANNERS, TITLE, LOGO, LOGO_BANNER, GENRE_OPTIONS, STYLE_OPTIONS
from utils import multiselect_to_string

from storage import storage_init
storage_init()

import openai
openai.api_key = st.secrets["openai_api_key"]

# =============================================================================================================
#       Configuration
# =============================================================================================================

st.set_page_config(
    page_title="AI Story Generator",
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

	st.subheader("Generate a story for your game!")
	st.write("What would you like the main plot of your game to be like? Save the princess? Explore new planets to help humanity survive? Is there a protagonist?")


	title = st.text_input('Title', value=st.session_state.title, placeholder='An idea for a potential title for your game')

	col1, col2 = st.columns(2)

	with col1:
		genre_options = st.multiselect(
		'Game Genre',
		GENRE_OPTIONS,
		st.session_state.genre_list)
	with col2:
		other_genre = st.text_input('Other Genres', value=st.session_state.genre_other)

	main_idea = st.text_area('What is the main idea of the plot?', value=st.session_state.main_idea, height=None, placeholder="ex. An Italian plumber that is trying to save the princess of the kingdom from an evil turlte king.")

	world_setting = st.text_area('Describe the world of your game', value=st.session_state.world_setting, height=None, placeholder="ex. The Mushroom Kingdom. A Magical place inhabited by tiny mushroom men.")

	other_prompts = st.text_area('Other prompts', value=st.session_state.other_prompts_story, height=None, placeholder="Other ideas you may have, or advanced prompts")

	# Every form must have a submit button.
	submitted = st.form_submit_button("Submit")
	if submitted:

		# Store changes on session storage
		st.session_state.title = title
		st.session_state.genre_list = genre_options
		st.session_state.genre_other = other_genre
		st.session_state.main_idea = main_idea
		st.session_state.world_setting = world_setting
		st.session_state.other_prompts_story = other_prompts

		# Generate GPT-3 prompt based on the user input
		prompt = "Write a story for a game. "

		if title != "":
			prompt += "A potential title is " + title + ". "
		
		if genre_options != "" or other_genre != "":
			prompt += "The game's genre is: " + multiselect_to_string(genre_options, other_genre) + ". "
		
		if main_idea != "":
			prompt += "The story is about: " + main_idea + ". "
		
		if world_setting != "":
			prompt += "A description of the game's world is: " + world_setting + ". "

		if other_prompts != "":
			prompt += other_prompts + ". "
		
		# st.write(prompt)

		# Send the prompt to GPT and display the response

		try:
		
			with st.spinner('Writing your story...'):
				response = openai.Completion.create(
				engine="text-davinci-003",
				prompt=prompt,
				temperature=0.4,
				max_tokens=1000,
				top_p=1.0,
				frequency_penalty=0.0,
				presence_penalty=0.0
				)

				ai_story = response['choices'][0]['text']

				# Store the response for later
				st.session_state.ai_story = ai_story
				
				# If title is not provided ask gpt3 
				if title == "":
					prompt_title = 'Write a title for a video game with this story: ' + ai_story
					
					response_title = openai.Completion.create(
					engine="text-davinci-003",
					prompt=prompt_title,
					temperature=0.4,
					max_tokens=1000,
					top_p=1.0,
					frequency_penalty=0.0,
					presence_penalty=0.0
					)

					ai_title = response_title['choices'][0]['text'].strip()

					st.session_state.title = ai_title.replace('"','')

		except:
			st.error('Failed to generate a story for your provided promp.', icon="🚨")
			pass

if st.session_state.ai_story!="" and st.session_state.title!="":
	st.write("## Game Story")
	st.write('__Title__: ' + st.session_state.title)
	st.write(st.session_state.ai_story)
	