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
    b = st.session_state.board
    for combo in winning_combos:
        a, b1, c = combo
        if b[a] == b[b1] == b[c] != "":
            st.session_state.winner = b[a]
            st.session_state.winning_combo = combo
            return

# Title
st.markdown("<h1 style='text-align:center; color:#6C63FF;'>🎮 Tic-Tac-Toe</h1>", unsafe_allow_html=True)

# Status
if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif "" not in st.session_state.board:
    st.warning("It's a Draw!")
else:
    st.info(f"🟢 Player {st.session_state.current_player}'s turn")

# CSS for board
st.markdown("""
    <style>
        .tictactoe-btn button {
            height: 100px;
            width: 100%;
            font-size: 40px;
            border-radius: 8px;
            border: 2px solid #ccc;
            background-color: #f8f9fa;
        }
        .tictactoe-btn button:disabled {
            background-color: #e9ecef;
            color: #000;
        }
        .tictactoe-btn .winning {
            background-color: #c8f7c5 !important;
            color: #2b9348 !important;
            border: 2px solid #2b9348 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Game Board
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        value = st.session_state.board[idx]
        is_winning = idx in st.session_state.winning_combo
        btn_label = value or " "
        btn_key = f"btn-{idx}"

        btn_container = cols[col].container()
        btn_class = "winning" if is_winning else ""
        with btn_container:
            st.markdown(f'<div class="tictactoe-btn {btn_class}">', unsafe_allow_html=True)
            if value or st.session_state.winner:
                st.button(btn_label, key=btn_key, disabled=True)
            else:
                if st.button(btn_label, key=btn_key):
                    st.session_state.board[idx] = st.session_state.current_player
                    check_winner()
                    if not st.session_state.winner:
                        st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
                    st.experimental_rerun()
            st.markdown("</div>", unsafe_allow_html=True)

# Reset Button
st.divider()
st.button("🔁 Reset Game", on_click=reset_game, use_container_width=True)
