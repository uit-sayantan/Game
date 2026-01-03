import streamlit as st
import random

# --- GAME LOGIC ---
def generate_secret_number():
    random_number = random.randint(10**3, 10**4 - 1)
    return random_number


# --- STREAMLIT UI ---
st.set_page_config(page_title="Bulls and Cows", page_icon="🔢")
st.title("🔢 Bulls and Cows: The Number Game")

rows = 5
column = 4

def clear_text():
    for key in list(st.session_state.keys()):
        if key.startswith("input_"):
            st.session_state[key] = ""

if "current_row" not in st.session_state:
    print("Current Row initialized")
    st.session_state.current_row = 0
    st.session_state.data = [['-' for _ in range(column)] for _ in range(rows)]
    st.session_state.secret_number = generate_secret_number()
    st.session_state.default_dash='-'
    clear_text()

if st.button("New Game"):
    st.session_state.secret_number = generate_secret_number()
    st.session_state.current_row = 0
    st.session_state.data = [[0 for _ in range(column)] for _ in range(rows)]
    st.session_state.default_dash='-'
    clear_text()
    st.rerun()
# Sidebar for controls
with st.sidebar:
    st.header("Game Settings")
    st.write("---")
    st.write("**Rules:**")
    st.write("- **Bull:** Correct digit, correct spot.")
    st.write("- **Cow:** Correct digit, wrong spot.")


st.markdown("""
    <style>
    /* This targets the input box itself */
    div[data-testid="stVerticalBlock"] > div:has(div.blue-colored-field) input {
        color: white;
        background-color: #2e7bcf;
        border-radius: 10px;
        border: 2px solid #ff4b4b;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* This targets the input box itself */
    div[data-testid="stVerticalBlock"] > div:has(div.red-colored-field) input {
        color: white;
        background-color: red;
        border-radius: 10px;
        border: 2px solid #ff4b4b;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* This targets the input box itself */
    div[data-testid="stVerticalBlock"] > div:has(div.green-colored-field) input {
        color: white;
        background-color: green;
        border-radius: 10px;
        border: 2px solid #ff4b4b;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* This targets the input box itself */
    div[data-testid="stVerticalBlock"] > div:has(div.yellow-colored-field) input {
        color: white;
        background-color: yellow;
        border-radius: 10px;
        border: 2px solid #ff4b4b;
    }
    </style>
""", unsafe_allow_html=True)

def render_text_field(i,j,color,disabled):
    st.markdown(f'<div class="{color}-colored-field"></div>', unsafe_allow_html=True)
    st.session_state.data[i][j] = st.text_input("Char"+str(i)+str(j),key=f'input_{i}{j}',
                                            label_visibility="collapsed",
                                            disabled = disabled,
                                            max_chars=1)

for i in range(0,rows):
    col = st.columns(column+1) 
    for j in range(0,column):
        with col[j]:
            if st.session_state.current_row==i:
                render_text_field(i,j,'blue',False)
            else:
                render_text_field(i,j,'red',True)
                
            
    if st.session_state.current_row==i:
        with col[column]:
            if st.button("🚀"):
                st.session_state.current_row=st.session_state.current_row+1
                st.rerun()
