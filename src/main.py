import requests
import streamlit as st
import os
import openai
import random
from params import BANNERS, TITLE, LOGO, LOGO_BANNER, API_KEY, GENRE_OPTIONS, STYLE_OPTIONS

openai.api_key = API_KEY
prompt = ""
submitted = False
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


# if random_button:
# 	prompt = "Generate a long and detailed story for a video game. "
# 	prompt += " It's genre is " + GENRE_OPTIONS[random.randint(0, len(GENRE_OPTIONS)-1)] + ". "
# 	prompt += " The art style is " + STYLE_OPTIONS[random.randint(0, len(STYLE_OPTIONS)-1)] + ". "
# 	submitted = True

with st.form("input_form"):

	st.subheader("Tell us a bit about your game ideas")
	st.write("All the fields below are optional, so feel free to fill out whatever information you want. They are just here to help you get ideas, and in turn help our AI models create a better story for you. ")


	title = st.text_input('Title', placeholder='An idea for a potential title for your game')

	col1, col2 = st.columns(2)

	with col1:
		genre_options = st.multiselect(
		'Game Genre',
		GENRE_OPTIONS,
		[])
		style_option = st.selectbox(
		'Art Style',
		STYLE_OPTIONS)

	with col2:
		other_genre = st.text_input('Other Genres')
		other_style = st.text_input('Complementary Art Style')

	mechanics = st.text_area('Game Mechanics', value="", height=None, placeholder="ex. Shooting, Time traveling, Resource gathering, Turn-based")

	world_setting = st.text_area('Describe the world setting of your game', value="", height=None, placeholder="ex. A Magical Kingdom high in the clouds that uses steampunk machines to travel the skies")

	other_prompts = st.text_area('Other prompts', value="", height=None, placeholder="Other ideas you may have, or advanced prompts")


	with st.expander("More Options"):
		prim_color = st.select_slider(
		'Pick A Primary Color for your concept art', 
		options=['None', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'])

		sec_color = st.select_slider(
		'Pick A Secondary Color for your concept art',
		options=['None', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'])

		people = st.text_area('Describe the people and/or the heroes that live on your world', value="", height=None, placeholder="ex. High elves that are proficient with jewelry and trade")

	# Every form must have a submit button.
	submitted = st.form_submit_button("Submit")
	if submitted:
		# st.write("title", title)
		prompt = "Generate a long and detailed story for a video game. "
		if title != None and title != "":
			prompt += "The game's title is " + title + ". "

		if len(genre_options) != 0 and genre_options != None:
			print(len(genre_options))
			prompt += " It's genre is "
			prompt += genre_options[0]
			if len(genre_options) > 1:
				genre_options.pop(0)
				concatGenre = ""
				for genre in genre_options:
					concatGenre += " and " + genre
				prompt += concatGenre
			
			if other_genre != None and other_genre != "":
				prompt += " and " + other_genre	
			prompt += ". "
		
		if style_option != None and style_option != "":
			if style_option != "-":
				if style_option == "Random":
					styleList = STYLE_OPTIONS
					style_option = styleList[random.randint(0, len(styleList)-1)]
				prompt += " The art style is " + style_option
				if other_style != None and other_style != "":
					prompt += " and " + other_style
				prompt += ". "
		
		if mechanics != None and mechanics != "":
			prompt += "An example of game mechanics is " + mechanics + ". "
		
		if world_setting != None and world_setting != "":
			prompt += "A description of the world the game takes place in is " + world_setting + ". "

		if other_prompts != None and other_prompts != "":
			prompt += other_prompts + ". "
		
		if people != None and people != "":
			prompt += "The people that live in game's world are described as " + people + ". "
		
		prompt += "\n\n"



if submitted:
	# st.write(prompt)
	submitted = False

	try:
	
		with st.spinner('Creating your game...'):
			response = openai.Completion.create(
			engine="text-davinci-003",
			prompt=prompt,
			temperature=0.4,
			max_tokens=1000,
			top_p=1.0,
			frequency_penalty=0.0,
			presence_penalty=0.0
			)

			firstResponse = response['choices'][0]['text']

			# firstResponse = "The game takes place in a vast and dangerous low-poly world. The player is a brave leader of a small group of survivors, who are determined to make a stand against the forces of evil. The player begins by scavenging for resources, such as rocks, iron, gold, and wood, which can then be used to build a base castle. The player can upgrade their castle, by adding walls, towers, and other defensive structures, as well as training and equipping soldiers to fight the enemy. As the game progresses, the player must manage their resources carefully, as they will be needed to survive the onslaught of the enemy. The player must also explore the world, searching for new resources, and discovering secrets and hidden areas. As the days pass, the enemy forces grow stronger and more numerous. Eventually, the player will have to face a massive enemy attack, which they must survive if they are to win the game. The player will have to use all of their wits and resources to survive the enemy onslaught and win the game. If they are successful, they will be rewarded with fame and glory, and will be remembered as a hero who saved the world from evil."	
			# print(firstResponse)

			st.write("## Game Description")
			st.write(firstResponse)

			# create a new image with given description
			response = openai.Image.create(
				prompt = firstResponse[:1000],
				n=2,
				size = "1024x1024"
			)
			
			st.write("## Concept art")
			col1, col2 = st.columns(2)
			with col1:
				st.image(response['data'][0]['url'])
			with col2:
				st.image(response['data'][1]['url'])

	except:
		st.error('Failed to generate concept art for your provided promp.', icon="🚨")
		pass

	# st.success('Done!')


	# # Download the image from the URL
	# img_data = requests.get(image_url)

	# # Save the image to a file
	# with open("../img/image.png", "wb") as f:
	# 	f.write(img_data.content)
