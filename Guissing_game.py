import streamlit as st
import random

# Set up initial session state if not already present
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randrange(100)
    st.session_state.chances = 7
    st.session_state.guess_counter = 0
    st.session_state.game_over = False
    st.session_state.message = "Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game"

# Display welcome message
st.write(st.session_state.message)

# Check if the game is over
if st.session_state.game_over:
    st.write(f"The number was {st.session_state.number_to_guess}. Better luck next time!")
else:
    # Input field for user guess
    my_guess = st.number_input('Please enter your guess:', min_value=0, max_value=99, step=1)

    # Button to make a guess
    if st.button('Submit Guess'):
        st.session_state.guess_counter += 1

        # Check if the guess is correct or not
        if my_guess == st.session_state.number_to_guess:
            st.session_state.message = f"Congrats! The number was {st.session_state.number_to_guess}. You guessed it in {st.session_state.guess_counter} attempts."
            st.session_state.game_over = True
        elif st.session_state.guess_counter >= st.session_state.chances:
            st.session_state.message = f"Oops sorry, The number was {st.session_state.number_to_guess}. Better luck next time!"
            st.session_state.game_over = True
        elif my_guess > st.session_state.number_to_guess:
            st.session_state.message = "Your guess is too high. Try again!"
        elif my_guess < st.session_state.number_to_guess:
            st.session_state.message = "Your guess is too low. Try again!"

# Option to restart the game
    