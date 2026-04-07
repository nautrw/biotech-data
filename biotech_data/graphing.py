import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st

from biotech_data.utils import get_specific_shops, shops


def shops_mean_graph(data):
    shops_list = sum(shops.values(), [])

    values = []
    for shop in shops_list:
        shop_data = get_specific_shops(data, [shop])
        values.append(shop_data["Observation"].mean())

    df = pd.DataFrame({"Shop": shops_list, "Average": values})

    fig = px.bar(df, x="Average", y="Shop", title="Mean observations for shops")
    fig.update_layout(yaxis={"dtick": 1})
    st.plotly_chart(fig)


def academies_mean_graph(data):
    academies_list = shops.keys()

    values = []
    for academy in academies_list:
        academy_data = get_specific_shops(data, shops[academy])
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
        len(get_specific_shops(data, [shop])["Observation"]) for shop in shops_list
    ]

    df = pd.DataFrame({"Shop": shops_list, "Average": values})

    fig = px.bar(df, x="Average", y="Shop", title="Amount of ratings per shop")
    fig.update_layout(yaxis={"dtick": 1})
    st.plotly_chart(fig)


def academies_observations_amounts_graph(data):
    academies_list = shops.keys()

    values = [
        len(get_specific_shops(data, shops[academy])["Observation"])
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
