import textwrap

import pandas as pd
import plotly.express as px
import streamlit as st

from biotech_data.utils import get_specific_locations, no_shops, shops


def shops_mean_graph(data, academies):
    shops_list = sum([shops[academy] for academy in academies], [])

    values = []
    for shop in shops_list:
        shop_data = get_specific_locations(data, [shop])
        values.append(shop_data["Observation"].mean())

    df = pd.DataFrame({"Shop": shops_list, "Mean": values})

    title = textwrap.fill(
        f"Mean observations for shops in {', '.join(academies)}",
        90,
        break_long_words=False,
    ).replace("\n", "<br>")

    fig = px.bar(df, x="Mean", y="Shop", title=title)
    fig.update_layout(yaxis={"dtick": 1})
    st.plotly_chart(fig)


def other_locations_mean_graph(data):
    values = []
    for location in no_shops:
        shop_data = get_specific_locations(data, [location])
        values.append(shop_data["Observation"].mean())

    df = pd.DataFrame({"Location": no_shops, "Mean": values})

    fig = px.bar(
        df, x="Mean", y="Location", title="Mean observations for other locations"
    )
    fig.update_layout(yaxis={"dtick": 1})
    st.plotly_chart(fig)


def other_locations_observations_amounts_graph(data):
    values = [
        len(get_specific_locations(data, [location])["Observation"])
        for location in no_shops
    ]

    df = pd.DataFrame({"Location": no_shops, "Amount": values})

    fig = px.bar(
        df, x="Amount", y="Location", title="Amount of observations in other locations"
    )
    fig.update_layout(yaxis={"dtick": 1})
    st.plotly_chart(fig)


def other_locations_scatter_plot(data):
    mean_observations = [
        get_specific_locations(data, [location])["Observation"].mean()
        for location in no_shops
    ]
    observations_amounts = [
        len(get_specific_locations(data, [location])) for location in no_shops
    ]

    df = pd.DataFrame(
        {
            "Mean Observation": mean_observations,
            "Amount of Observations": observations_amounts,
            "Location": no_shops,
        }
    )

    fig = px.scatter(
        df,
        x="Mean Observation",
        y="Amount of Observations",
        hover_data=["Location"],
        title="Mean Observation vs. Amount of Observations (Other Locations)",
    )
    st.plotly_chart(fig)


def academies_mean_graph(data):
    academies_list = shops.keys()

    values = []
    for academy in academies_list:
        academy_data = get_specific_locations(data, shops[academy])
        values.append(academy_data["Observation"].mean())

    df = pd.DataFrame({"Academy": academies_list, "Mean": values})

    fig = px.bar(
        df,
        x="Mean",
        y="Academy",
        title="Mean observations for academies",
        text_auto=True,
    )
    fig.update_layout(yaxis={"dtick": 1})
    st.plotly_chart(fig)


def shops_observations_amounts_graph(data, academies):
    shops_list = sum([shops[academy] for academy in academies], [])
    values = [
        len(get_specific_locations(data, [shop])["Observation"]) for shop in shops_list
    ]

    df = pd.DataFrame({"Shop": shops_list, "Amount": values})

    title = textwrap.fill(
        f"Amount of observations for shops in {', '.join(academies)}",
        90,
        break_long_words=False,
    ).replace("\n", "<br>")

    fig = px.bar(df, x="Amount", y="Shop", title=title)
    fig.update_layout(yaxis={"dtick": 1})
    st.plotly_chart(fig)


def academies_observations_amounts_graph(data):
    academies_list = shops.keys()

    values = [
        len(get_specific_locations(data, shops[academy])["Observation"])
        for academy in academies_list
    ]

    df = pd.DataFrame({"Academy": academies_list, "Amount": values})

    fig = px.bar(
        df,
        x="Amount",
        y="Academy",
        title="Amount of observations per academy",
        text_auto=True,
    )
    fig.update_layout(yaxis={"dtick": 1})
    st.plotly_chart(fig)


def mean_observations_vs_obvervations_amounts_scatter_plot(data):
    shops_list = sum(shops.values(), [])

    mean_observations = [
        get_specific_locations(data, [shop])["Observation"].mean()
        for shop in shops_list
    ]
    observations_amounts = [
        len(get_specific_locations(data, [shop])["Observation"]) for shop in shops_list
    ]

    df = pd.DataFrame(
        {
            "Mean Observation": mean_observations,
            "Amount of Observations": observations_amounts,
            "Shop": shops_list,
        }
    )

    fig = px.scatter(
        df,
        x="Mean Observation",
        y="Amount of Observations",
        hover_data=["Shop"],
        title="Mean Observation vs. Amount of Observations (Shops)",
    )
    st.plotly_chart(fig)
