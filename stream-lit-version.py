import streamlit as st

# Set page configuration
st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None

# Winning combinations
winning_combos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

# Check winner
def check_winner():
    board = st.session_state.board
    for combo in winning_combos:
        a, b, c = combo
        if board[a] == board[b] == board[c] != "":
            st.session_state.winner = board[a]
            return True
    return False

# Reset game
def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None

# Title
st.markdown("<h1 style='text-align:center;'>🎮 Tic-Tac-Toe</h1>", unsafe_allow_html=True)

# Show game status
if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif "" not in st.session_state.board:
    st.warning("😮 It's a Draw!")
else:
    st.info(f"🟢 Player {st.session_state.current_player}'s turn")

# Game board
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        btn_label = st.session_state.board[idx] or " "
        if st.session_state.board[idx] != "" or st.session_state.winner:
            cols[col].button(btn_label, key=f"btn-{idx}", disabled=True)
        else:
            if cols[col].button(btn_label, key=f"btn-{idx}"):
                # Update board
                st.session_state.board[idx] = st.session_state.current_player
                if not check_winner():
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
                st.experimental_rerun()

# Reset button
st.divider()
st.button("🔄 Reset Game", on_click=reset_game, use_container_width=True)
