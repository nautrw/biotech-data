import pandas as pd
import streamlit as st

import biotech_data.graphing as graphing
from biotech_data.utils import pregraph

data = pd.read_csv("data.csv")

st.header("Biotech Data Analysis")

data = pregraph(data)

graphing.shops_mean_graph(data)
