import streamlit as st

st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")

if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.winning_combo = []

winning_combos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

def check_winner():
    board = st.session_state.board
    for combo in winning_combos:
        a, b, c = combo
        if board[a] == board[b] == board[c] != "":
            st.session_state.winner = board[a]
            st.session_state.winning_combo = combo
            return

def handle_click(index):
    if st.session_state.board[index] == "" and st.session_state.winner is None:
        st.session_state.board[index] = st.session_state.current_player
        check_winner()
        if st.session_state.winner is None:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.winning_combo = []

st.title("🎮 Tic-Tac-Toe")

if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
else:
    st.info(f"Player {st.session_state.current_player}'s turn")

cols = st.columns(3)
for i in range(9):
    btn_style = "background-color:lightgreen;" if i in st.session_state.winning_combo else ""
    with cols[i % 3]:
        if st.button(st.session_state.board[i] or " ", key=i, help=f"Cell {i+1}"):
            handle_click(i)
        st.markdown(f"<style>div[data-testid='column'] button{{ {btn_style} }}</style>", unsafe_allow_html=True)

st.markdown("---")
if st.button("🔁 Reset Game"):
    reset_game()
