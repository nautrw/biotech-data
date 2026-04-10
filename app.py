import pandas as pd
import streamlit as st

import biotech_data.graphing as graphing
import biotech_data.utils as utils
from biotech_data.easter_egg import do_easter_egg


@st.cache_data
def load_data():
    data = pd.read_csv("data.csv")

    data = utils.exclude_spore_colonies(data)
    data = utils.quantify_observations(data)

    return data


data = load_data()
do_easter_egg()

st.header("Biotech Data Analysis")

graphing.mean_observations_vs_obvervations_amounts_scatter_plot(data)

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

st.subheader("Other locations")
(
    other_locations_mean,
    other_locations_observations_amount,
    other_locations_scatter_plot,
) = st.tabs(["Averages", "Observation Amounts", "Scatter plot"])

with other_locations_mean:
    graphing.other_locations_mean_graph(data)
with other_locations_observations_amount:
    graphing.other_locations_observations_amounts_graph(data)
with other_locations_scatter_plot:
    graphing.other_locations_scatter_plot(data)
