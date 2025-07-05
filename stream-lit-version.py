import streamlit as st

st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.winning_combo = []

# Game logic
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
            return True
    return False

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.winning_combo = []

# UI Title
st.markdown("<h1 style='text-align:center; color:#a78bfa;'>🎮 Tic-Tac-Toe</h1>", unsafe_allow_html=True)

# Game Status
if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif "" not in st.session_state.board:
    st.warning("It's a Draw!")
else:
    st.info(f"🟢 Player {st.session_state.current_player}'s turn")

# Custom CSS
st.markdown("""
<style>
.square-btn button {
    width: 100%;
    padding-top: 100%; /* Aspect ratio 1:1 */
    position: relative;
    background-color: #1f2937;
    border: 2px solid #4b5563;
    border-radius: 8px;
    font-size: 40px;
    color: #ffffff;
}
.square-btn button div {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
.winner-cell {
    background-color: #22c55e !important;
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

# Game Board
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        cell_value = st.session_state.board[idx]
        is_winner = idx in st.session_state.winning_combo
        btn_key = f"cell_{idx}"
        
        btn_class = "winner-cell" if is_winner else ""
        with cols[col]:
            st.markdown(f'<div class="square-btn {btn_class}">', unsafe_allow_html=True)
            if st.button(" ", key=btn_key, disabled=bool(cell_value or st.session_state.winner)):
                st.session_state.board[idx] = st.session_state.current_player
                if not check_winner():
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
            st.markdown(f'<div>{cell_value}</div>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

st.divider()
st.button("🔁 Reset Game", on_click=reset_game, use_container_width=True)
