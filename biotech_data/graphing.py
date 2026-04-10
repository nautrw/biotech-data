import textwrap

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st

from biotech_data.utils import get_specific_locations, no_shops, shops


def shops_mean_graph(data):
    shops_list = sum(shops.values(), [])

    values = []
    for shop in shops_list:
        shop_data = get_specific_locations(data, [shop])
        values.append(shop_data["Observation"].mean())

    df = pd.DataFrame({"Shop": shops_list, "Average": values})

    fig = px.bar(df, x="Average", y="Shop", title="Mean observations for shops")
    fig.update_layout(yaxis={"dtick": 1})
    st.plotly_chart(fig)


def shops_per_academy_mean_graph(data, academies):
    shops_list = sum([shops[academy] for academy in academies], [])

    values = []
    for shop in shops_list:
        shop_data = get_specific_locations(data, [shop])
        values.append(shop_data["Observation"].mean())

    df = pd.DataFrame({"Shop": shops_list, "Average": values})

    title = textwrap.fill(
        f"Mean observations for shops in {', '.join(academies)}",
        90,
        break_long_words=False,
    ).replace("\n", "<br>")

    fig = px.bar(df, x="Average", y="Shop", title=title)
    fig.update_layout(yaxis={"dtick": 1})
    st.plotly_chart(fig)


def other_locations_mean_graph(data):
    values = []
    for location in no_shops:
        shop_data = get_specific_locations(data, [location])
        values.append(shop_data["Observation"].mean())

    df = pd.DataFrame({"Location": no_shops, "Average": values})

    fig = px.bar(
        df, x="Average", y="Location", title="Mean observations for other locations"
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
            "Average Observation": mean_observations,
            "Observations Amount": observations_amounts,
            "Location": no_shops,
        }
    )

    fig = px.scatter(
        df,
        x="Average Observation",
        y="Observations Amount",
        hover_data=["Location"],
        title="Average Observation vs. Amount of Observations (Other Locations)",
    )
    st.plotly_chart(fig)


def academies_mean_graph(data):
    academies_list = shops.keys()

    values = []
    for academy in academies_list:
        academy_data = get_specific_locations(data, shops[academy])
        values.append(academy_data["Observation"].mean())

    df = pd.DataFrame({"Academy": academies_list, "Average": values})

    fig = px.bar(
        df,
        x="Average",
        y="Academy",
        title="Mean observations for academies",
        text_auto=True,
    )
    fig.update_layout(yaxis={"dtick": 1})
    st.plotly_chart(fig)


def shops_observations_amounts_graph(data):
    shops_list = sum(shops.values(), [])

    values = [
        len(get_specific_locations(data, [shop])["Observation"]) for shop in shops_list
    ]

    df = pd.DataFrame({"Shop": shops_list, "Amount": values})

    fig = px.bar(df, x="Amount", y="Shop", title="Amount of observations per shop")
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
    academies_list = shops.keys()

    mean_observations = [
        get_specific_locations(data, [shop])["Observation"].mean()
        for shop in shops_list
    ]
    observations_amounts = [
        len(get_specific_locations(data, [shop])["Observation"]) for shop in shops_list
    ]

    df = pd.DataFrame(
        {
            "Average Observation": mean_observations,
            "Observations Amount": observations_amounts,
            "Shop": shops_list,
        }
    )

    fig = px.scatter(
        df,
        x="Average Observation",
        y="Observations Amount",
        hover_data=["Shop"],
        title="Average Observation vs. Amount of Observations (Shops)",
    )
    st.plotly_chart(fig)
