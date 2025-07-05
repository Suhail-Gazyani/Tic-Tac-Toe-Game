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

def check_winner():
    board = st.session_state.board
    for combo in winning_combos:
        a, b, c = combo
        if board[a] == board[b] == board[c] != "":
            st.session_state.winner = board[a]
            st.session_state.winning_combo = combo
            return

def handle_click(index):
    if st.session_state.board[index] == "" and not st.session_state.winner:
        st.session_state.board[index] = st.session_state.current_player
        check_winner()
        if not st.session_state.winner:
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

for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        index = row * 3 + col
        btn_label = st.session_state.board[index] or " "
        btn_color = "background-color:lightgreen;" if index in st.session_state.winning_combo else ""
        with cols[col]:
            if st.button(btn_label, key=index):
                handle_click(index)
            st.markdown(f"""
                <style>
                div[data-testid="column"] > div > button[title="{btn_label}"] {{
                    {btn_color}
                    font-size: 24px;
                    height: 60px;
                    width: 100%;
                }}
                </style>
            """, unsafe_allow_html=True)

st.markdown("---")
if st.button("🔁 Reset Game"):
    reset_game()
