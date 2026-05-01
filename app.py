import pandas as pd
import streamlit as st

import biotech_data.graphing as graphing
import biotech_data.utils as utils
from biotech_data.easter_egg import do_easter_egg

do_easter_egg()

raw_data = pd.read_csv("data.csv")

data = utils.exclude_spore_colonies(raw_data)
data = utils.quantify_observations(data)

st.header("Biotech Data Analysis", divider=True)

st.subheader("Introduction", divider=True)

st.markdown("""This project was made to showcase and analyze the data collecte
by freshmen in the Biotechnology shop 1-week explore.

Because the data was not quantitative, I decided to represent the observations
as numbers, which is a more temporary solution but allows for performing
operations like finding the mean:

| Observation in Raw Data | Corresponding Value |
| ----------------------- | ------------------- |
| None | 0 |
| Below Average | 1 |
| Average | 2 |
| Above Average | 3 |

Thus, a mean between 2 and 3 for a location would indicate that the amount of
bacteria found in that location is between average and above average.

All graphs are fully interactive, and you are able to zoom in by selecting an
area with the mouse, or hover over any bar or point to see the specific value.
Furthermore, you can filter the shops shown in the [shops](#Shops) graphs by
their academy using the select menus.
""")

st.subheader("Important Metrics", divider=True)

main_metrics = st.columns(4)

main_metrics[0].metric("Total observations", len(raw_data["Observation"]))
main_metrics[1].metric("School-wide mean", f"{data['Observation'].mean():.2f}")
main_metrics[2].metric(
    "Shops' mean", f"{utils.exclude_no_shop(data)['Observation'].mean():.2f}"
)
main_metrics[3].metric(
    "Other locations' mean",
    f"{utils.get_specific_locations(data,
        [location for location in utils.no_shops]
    )["Observation"].mean():.2f}",
)

st.subheader("Bacteria Observations", divider=True)

st.markdown("### Shops")
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

st.markdown("### Academies")

academies_mean_observation, academies_observations_amount = st.tabs(
    ["Mean observation", "Amount of observations"]
)

with academies_mean_observation:
    graphing.academies_mean_graph(data)
with academies_observations_amount:
    graphing.academies_observations_amounts_graph(data)

st.markdown("### Other Locations")

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

st.subheader("Spore Colonies", divider=True)

shops_spore_colonies, academies_spore_colonies = st.tabs(["Shops", "Academies"])

with shops_spore_colonies:
    graphing.spore_colonies_graph(raw_data)
with academies_spore_colonies:
    graphing.academies_spore_colonies_graph(raw_data)
