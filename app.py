import pandas as pd
import streamlit as st

import biotech_data.graphing as graphing
from biotech_data.utils import pregraph

data = pd.read_csv("data.csv")
data = pregraph(data)

st.header("Biotech Data Analysis")

graphing.shops_mean_graph(data)
graphing.shops_ratings_amounts_graph(data)
graphing.academies_mean_graph(data)
graphing.academies_ratings_amounts_graph(data)
