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


do_easter_egg()
data = load_data()

st.header("Biotech Data Analysis")

cols = st.columns(3)

cols[0].metric("Total observations", len(data["Observation"]))
cols[1].metric("School-wide mean", f"{data['Observation'].mean():.2f}")
cols[2].metric(
    "Shops' mean", f"{utils.exclude_no_shop(data)['Observation'].mean():.2f}"
)


st.subheader("Shops")
shops_mean_observation, shops_observations_amounts, shops_scatter = st.tabs(
    ["Mean observation", "Amount of observations", "Scatter Plot"]
)

with shops_mean_observation:
    academies = list(utils.shops.keys())

    academies_select = st.multiselect(
        "Search by academy",
        key="academies_select_acadmies_mean_observation",
        options=academies,
        default=academies,  # Will default to showing all
        placeholder="Choose academies to get their shop's data",
        accept_new_options=False,
    )

    graphing.shops_mean_graph(data, academies_select)
with shops_observations_amounts:
    academies_select = st.multiselect(
        "Search by academy",
        key="academies_select_academies_observation_amount",
        options=academies,
        default=academies,  # Will default to showing all
        placeholder="Choose academies to get their shop's data",
        accept_new_options=False,
    )

    graphing.shops_observations_amounts_graph(data, academies_select)
with shops_scatter:
    graphing.mean_observations_vs_obvervations_amounts_scatter_plot(data)

st.subheader("Academies")
academies_mean_observation, academies_observations_amount = st.tabs(
    ["Mean observation", "Amount of observations"]
)

with academies_mean_observation:
    graphing.academies_mean_graph(data)
with academies_observations_amount:
    graphing.academies_observations_amounts_graph(data)

st.subheader("Other Locations")
(
    other_locations_mean,
    other_locations_observations_amount,
    other_locations_scatter_plot,
) = st.tabs(["Mean observation", "Amount of observations", "Scatter plot"])

with other_locations_mean:
    graphing.other_locations_mean_graph(data)
with other_locations_observations_amount:
    graphing.other_locations_observations_amounts_graph(data)
with other_locations_scatter_plot:
    graphing.other_locations_scatter_plot(data)
