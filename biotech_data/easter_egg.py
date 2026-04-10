import random
from datetime import datetime

import streamlit as st


def do_easter_egg():
    if random.random() < 0.01:
        now = datetime.now()
        eggs = [st.balloons, st.snow]

        random.choice(eggs)()
        st.toast("You found an easter egg!", icon="🥚", duration="long")
        print(f"An easter egg was found at {now.strftime('%Y-%m-%d %H:%M:%S')}")
