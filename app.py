import pandas as pd
import streamlit as st

import biotech_data.graphing as graphing
from biotech_data.utils import pregraph

data = pd.read_csv("data.csv")
data = pregraph(data)

st.header("Biotech Data Analysis")

graphing.mean_observations_vs_obvervations_amounts_graph(data)

st.subheader("Average ratings")
shops_mean, academies_mean = st.tabs(["Shops", "Academies"])

with shops_mean:
    graphing.shops_mean_graph(data)
with academies_mean:
    graphing.academies_mean_graph(data)

st.subheader("Amount of ratings")
shops_ratings_amounts, academies_ratings_amount = st.tabs(["Shops", "Academies"])

with shops_ratings_amounts:
    graphing.shops_observations_amounts_graph(data)
with academies_ratings_amount:
    graphing.academies_observations_amounts_graph(data)
