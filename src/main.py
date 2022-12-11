import streamlit as st
import os
import openai
import random
from params import BANNERS, TITLE, LOGO, LOGO_BANNER, API_KEY

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
	st.write("All the fields below are optional, so feel free to fill out whatever information you want. They are just here to help you get ideas, and in turn help our AI models create a better story for you. ")

	title = st.text_input('Title', placeholder='An idea for a potential title for your game')

	col1, col2 = st.columns(2)

	with col1:
		genre_options = st.multiselect(
		'Game Genre',
		['Action', 'Adventure', 'Fighting', 'Platform', 'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy'],
		[])
		style_option = st.selectbox(
		'Art Style',
		('Random', 'Realism', 'Fantasy', 'Low Poly', 'Hand-Painted', 'Cartoon', '2D Pixel Art', 'Vector' , 'Cutout' , 'Cel Shading', 'Monochromatic' ,'Flat'))

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
		startText = "Generate a long and detailed story for a video game. "
		if title != None and title != "":
			startText += "The game's title is " + title + ". "

		if len(genre_options) != 0 and genre_options != None:
			print(len(genre_options))
			startText += " It's genre is "
			startText += genre_options[0]
			if len(genre_options) > 1:
				genre_options.pop(0)
				concatGenre = ""
				for genre in genre_options:
					concatGenre += " and " + genre
				startText += concatGenre
			
			if other_genre != None and other_genre != "":
				startText += " and " + other_genre	
			startText += ". "
		
		if style_option != None and style_option != "":
			if style_option == "Random":
				styleList = ['Realism', 'Fantasy', 'Low Poly', 'Hand-Painted', 'Cartoon', '2D Pixel Art', 'Vector' , 'Cutout' , 'Cel Shading', 'Monochromatic' ,'Flat']
				style_option = styleList[random.randint(0, len(styleList)-1)]
			startText += " The art style is " + style_option
			if other_style != None and other_style != "":
				startText += " and " + other_style
			startText += ". "
		
		if mechanics != None and mechanics != "":
			startText += "An example of game mechanics is " + mechanics + ". "
		
		if world_setting != None and world_setting != "":
			startText += "A description of the world the game takes place in is " + world_setting + ". "

		if other_prompts != None and other_prompts != "":
			startText += other_prompts + ". "
		
		if people != None and people != "":
			startText += "The people that live in game's world are described as " + people + ". "
		
		startText += "\n\n"
		print(startText)



		response = openai.Completion.create(
		engine="text-davinci-003",
		prompt=startText,
		temperature=0.4,
		max_tokens=1000,
		top_p=1.0,
		frequency_penalty=0.0,
		presence_penalty=0.0
		)

		firstResponse = response['choices'][0]['text']

		print(firstResponse)
		st.write(firstResponse)
