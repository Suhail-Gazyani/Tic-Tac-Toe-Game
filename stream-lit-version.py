import streamlit as st

st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")

if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.winning_combo = []

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

def check_winner():
    board = st.session_state.board
    for combo in winning_combos:
        a, b, c = combo
        if board[a] == board[b] == board[c] != "":
            st.session_state.winner = board[a]
            st.session_state.winning_combo = combo
            return True
    return False

st.title("🎮 Tic-Tac-Toe")

if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
else:
    st.info(f"Player {st.session_state.current_player}'s turn")

for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        cell_value = st.session_state.board[idx]
        highlight = idx in st.session_state.winning_combo
        btn_label = cell_value or " "
        btn_color = "✅ " + cell_value if highlight else btn_label

        if st.session_state.winner or cell_value:
            cols[col].button(btn_color, key=idx, disabled=True, use_container_width=True)
        else:
            if cols[col].button(btn_color, key=idx, use_container_width=True):
                st.session_state.board[idx] = st.session_state.current_player
                if not check_winner():
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
                st.experimental_rerun()

st.markdown("---")
st.button("🔁 Reset Game", on_click=reset_game, use_container_width=True)
