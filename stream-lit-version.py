import streamlit as st

st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")

if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.winning_combo = []
    st.session_state.move_index = None

winning_combos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.winning_combo = []
    st.session_state.move_index = None

def check_winner():
    b = st.session_state.board
    for combo in winning_combos:
        a, b1, c = combo
        if b[a] == b[b1] == b[c] != "":
            st.session_state.winner = b[a]
            st.session_state.winning_combo = combo
            return

# Process the move after rerun
if st.session_state.move_index is not None:
    idx = st.session_state.move_index
    if st.session_state.board[idx] == "" and not st.session_state.winner:
        st.session_state.board[idx] = st.session_state.current_player
        check_winner()
        if not st.session_state.winner:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
    st.session_state.move_index = None

st.markdown("<h1 style='text-align: center;'>🎮 Tic-Tac-Toe</h1>", unsafe_allow_html=True)

if st.session_state.winner:
    st.success(f"✅ Player {st.session_state.winner} wins!")
else:
    st.info(f"🔄 Player {st.session_state.current_player}'s turn")

for row in range(3):
    cols = st.columns([1, 1, 1], gap="small")
    for col in range(3):
        i = row * 3 + col
        btn_value = st.session_state.board[i]
        is_winner_cell = i in st.session_state.winning_combo

        btn_style = "font-size: 32px; padding: 16px; height: 75px; width: 100%;"
        if is_winner_cell:
            btn_style += " background-color: #27ae60; color: white; font-weight: bold;"
        elif btn_value != "":
            btn_style += " background-color: #2c3e50; color: white;"
        else:
            btn_style += " background-color: #34495e; color: white;"

        with cols[col]:
            if st.button(btn_value or " ", key=f"cell-{i}", help=f"Cell {i+1}"):
                st.session_state.move_index = i
                st.experimental_rerun()

st.markdown("<hr>", unsafe_allow_html=True)
st.button("🔁 Reset Game", on_click=reset_game, use_container_width=True)
