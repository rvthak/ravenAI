import streamlit as st
import random
from params import BANNERS, TITLE, LOGO, LOGO_BANNER, API_KEY, GENRE_OPTIONS, STYLE_OPTIONS
from utils import multiselect_to_string

from storage import storage_init
storage_init()

import openai
openai.api_key = API_KEY

# =============================================================================================================
#       Configuration
# =============================================================================================================

st.set_page_config(
    page_title="AI Mechanics Generator",
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

	st.subheader("Let's figure out the mechanics of your game together!")
	st.write("What makes your game a good game? How does your game work?")

	col1, col2 = st.columns(2)

	with col1:
		genre_options = st.multiselect(
		'Game Genre',
		GENRE_OPTIONS,
		st.session_state.genre_list)

		platforms = st.multiselect(
		'Target Platform',
		["", "PC", "Console", "Mobile"],
		st.session_state.platforms
		)
	with col2:
		other_genre = st.text_input('Other Genres', value=st.session_state.genre_other)

	goal = st.text_area('What is the goal of the game?', value=st.session_state.game_goal, height=None, placeholder="ex. The player has to finish a set of handmade levels in order to complete the game.")
	fun = st.text_area('How does the player have fun?', value=st.session_state.game_fun, height=None, placeholder="ex. Solving a hard and clever puzzle is fun! The famous AHA moment")
	systems = st.text_area('What systems does the game have?', value=st.session_state.game_systems, height=None, placeholder="ex. A leveling system, a skill system, a progression system, a merchant-based economy (Ideally provide a short description of each system)")

	other_prompts = st.text_area('Other prompts', value=st.session_state.other_prompts_mech, height=None, placeholder="Other ideas you may have, or advanced prompts")

	# Every form must have a submit button.
	submitted = st.form_submit_button("Submit")
	if submitted:

		# Store changes on session storage
		st.session_state.genre_list = genre_options
		st.session_state.genre_other = other_genre
		st.session_state.platforms = platforms
		st.session_state.game_goal = goal
		st.session_state.game_fun = fun
		st.session_state.game_systems = systems
		st.session_state.other_prompts_mech = other_prompts
	

		# Generate GPT-3 prompt based on the user input
		prompt = "Write ideas for game mechanics. "

		if genre_options != "" or other_genre != "":
			prompt += "The game's genre is: " + multiselect_to_string(genre_options, other_genre) + ". "

		if platforms != "":
			prompt += "The game release platforms are " + multiselect_to_string(platforms, "") + ". "
		
		if goal != "":
			prompt += "The goal of the game is: " + goal + ". "
		
		if fun != "":
			prompt += "Here is what make the game fun: " + fun + ". "
		
		if systems != "":
			prompt += "Some of the game systems should be: " + systems + ". "

		if other_prompts != "":
			prompt += other_prompts + ". "
		
		# st.write(prompt)

		# Send the prompt to GPT and display the response
		try:
		
			with st.spinner('Coming up with game mechanics...'):
				response = openai.Completion.create(
				engine="text-davinci-003",
				prompt=prompt,
				temperature=0.4,
				max_tokens=1000,
				top_p=1.0,
				frequency_penalty=0.0,
				presence_penalty=0.0
				)

				ai_mechanics = response['choices'][0]['text']

				# Store the response for later
				st.session_state.ai_mechanics = ai_mechanics

		except:
			st.error('Failed to generate concept art for your provided promp.', icon="🚨")
			pass

if st.session_state.ai_mechanics!="":
	st.write("## Game Mechanics")
	st.write(st.session_state.ai_mechanics)

