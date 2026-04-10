import random

import streamlit as st


def do_easter_egg():
    if random.random() < 0.51:
        eggs = [st.balloons, st.snow]

        random.choice(eggs)()
        st.toast("You found an easter egg!", icon="🥚", duration="long")
