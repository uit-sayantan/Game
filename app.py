import streamlit as st
import random

# --- GAME LOGIC ---
def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    return "".join(map(str, digits[:4]))

def get_hints(secret, guess):
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

# --- STREAMLIT UI ---
st.set_page_config(page_title="Bulls and Cows", page_icon="🔢")
st.title("🔢 Bulls and Cows: The Number Game")

# Initialize session state variables
if "secret_number" not in st.session_state:
    st.session_state.secret_number = generate_secret_number()
    st.session_state.history = []
    st.session_state.game_over = False
if st.button("New Game"):
        st.session_state.secret_number = generate_secret_number()
        st.session_state.history = []
        st.session_state.game_over = False
        st.rerun()
# Sidebar for controls
with st.sidebar:
    st.header("Game Settings")
    st.write("---")
    st.write("**Rules:**")
    st.write("- **Bull:** Correct digit, correct spot.")
    st.write("- **Cow:** Correct digit, wrong spot.")

# Main Game Input
if not st.session_state.game_over:
    guess = st.text_input("Enter a 4-digit number (unique digits):", max_chars=4)
    
    if st.button("Submit Guess"):
        if len(guess) == 4 and guess.isdigit():
            bulls, cows = get_hints(st.session_state.secret_number, guess)
            st.session_state.history.insert(0, {"guess": guess, "bulls": bulls, "cows": cows})
            
            if bulls == 4:
                st.session_state.game_over = True
                st.balloons()
        else:
            st.error("Please enter a valid 4-digit number.")

# Display Results
if st.session_state.game_over:
    st.success(f"🎉 Correct! The number was {st.session_state.secret_number}.")
    if st.button("Play Again"):
        st.session_state.secret_number = generate_secret_number()
        st.session_state.history = []
        st.session_state.game_over = False
        st.rerun()

# Guess History Table
if st.session_state.history:
    st.subheader("Guess History")
    st.table(st.session_state.history)

col1, col2 = st.columns([1, 9]) 

with col1:
    char = st.text_input("Char", max_chars=1)

if char:
    st.write(f"Result: {char}")