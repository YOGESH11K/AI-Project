import random
import streamlit as st

st.set_page_config(page_title="🎯 Number Guessing Game", page_icon="🎯")

st.title("🎯 Number Guessing Game")
st.write("Maine 1 se 10 ke beech ek number choose kiya hai.")
st.write("Tumhare paas **3 chances** hain!")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 10)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.won = False

def reset_game():
    st.session_state.secret = random.randint(1, 10)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.won = False

guess = st.number_input(
    "Apna guess enter karo (1-10):",
    min_value=1,
    max_value=10,
    step=1,
    key="guess_input",
)

if st.button("Submit Guess"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1
        if guess < st.session_state.secret:
            st.warning("📈 Too low!")
        elif guess > st.session_state.secret:
            st.warning("📉 Too high!")
        else:
            st.success(f"🎉 Correct! Number {st.session_state.secret} tha.")
            st.success(f"✅ Tumne {st.session_state.attempts} attempts mein guess kar liya!")
            st.balloons()
            st.session_state.game_over = True
            st.session_state.won = True

        if st.session_state.attempts >= 3 and not st.session_state.won:
            st.error("❌ 3 attempts khatam!")
            st.error(f"Number {st.session_state.secret} tha.")
            st.session_state.game_over = True

attempts_left = max(3 - st.session_state.attempts, 0)
st.info(f"Chances left: **{attempts_left}**" + (" (Game over)" if st.session_state.game_over else ""))

if st.session_state.game_over:
    if st.button("🔄 Dobara try karna hai?"):
        reset_game()
        st.rerun()