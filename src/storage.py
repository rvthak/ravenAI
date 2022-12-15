import streamlit as st


# Used to init and manage  session storage

# Initialization
def storage_init():

#===================================================================
# User Input fields
#===================================================================

    if 'title' not in st.session_state:
        st.session_state.title = ""

    if 'genre_list' not in st.session_state:
        st.session_state.genre_list = []

    if 'genre_other' not in st.session_state:
        st.session_state.genre_other = ""

    if 'main_idea' not in st.session_state:
        st.session_state.main_idea = ""
    
    if 'world_setting' not in st.session_state:
        st.session_state.world_setting = ""
    
    if 'other_prompts_story' not in st.session_state:
        st.session_state.other_prompts_story = ""

    if 'platforms' not in st.session_state:
        st.session_state.platforms = []

    if 'game_goal' not in st.session_state:
        st.session_state.game_goal = ""

    if 'game_fun' not in st.session_state:
        st.session_state.game_fun = ""

    if 'game_systems' not in st.session_state:
        st.session_state.game_systems = ""
    
    if 'other_prompts_mech' not in st.session_state:
        st.session_state.other_prompts_mech = ""

    if 'style_option' not in st.session_state:
        st.session_state.style_option = []

    if 'perspective' not in st.session_state:
        st.session_state.perspective = []

    if 'other_style' not in st.session_state:
        st.session_state.other_style = ""

    if 'world_setting' not in st.session_state:
        st.session_state.world_setting = ""

    if 'other_prompts_world' not in st.session_state:
        st.session_state.other_prompts_world = ""

    if 'prim_color' not in st.session_state:
        st.session_state.prim_color = 'None'

    if 'sec_color' not in st.session_state:
        st.session_state.sec_color = 'None'

    if 'character_description' not in st.session_state:
        st.session_state.character_description = ""

    if 'character_apparel' not in st.session_state:
        st.session_state.character_apparel = ""

    if 'character_weapons' not in st.session_state:
        st.session_state.character_weapons = ""
    
    if 'character_skills' not in st.session_state:
        st.session_state.character_skills = ""

    if 'character_story' not in st.session_state:
        st.session_state.character_story = ""

    if 'other_prompts_char' not in st.session_state:
        st.session_state.other_prompts_char = ""

#===================================================================
# Responses
#===================================================================
    if 'ai_story' not in st.session_state:
            st.session_state.ai_story = ""
    
    if 'ai_mechanics' not in st.session_state:
            st.session_state.ai_mechanics = ""
    

    if 'ai_world_0' not in st.session_state:
            st.session_state.ai_world_0 = ""
    
    if 'ai_world_1' not in st.session_state:
            st.session_state.ai_world_1 = ""

    if 'ai_char_0' not in st.session_state:
            st.session_state.ai_char_0 = ""
    
    if 'ai_char_1' not in st.session_state:
            st.session_state.ai_char_1 = ""
