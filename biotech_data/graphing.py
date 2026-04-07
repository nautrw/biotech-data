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

    fig = px.bar(df, x="Average", y="Shop", title="Mean ratings for shops")
    fig.update_layout(yaxis={"dtick": 1})
    st.plotly_chart(fig)


def academies_mean_graph(data):
    academies_list = shops.keys()

    values = []
    for academy in academies_list:
        academy_data = get_specific_shops(data, shops[academy])
        values.append(academy_data["Observation"].mean())

    df = pd.DataFrame({"academies": academies_list, "mean": values})
    fig, ax = plt.subplots()
    df.plot.barh("academies", "mean", ax=ax)
    ax.set_xticklabels(
        ["None", "", "Below Average", "", "Average", "", "Above Average"]
    )

    plt.title("Mean rating for all academies")
    plt.ylabel("Academies")
    plt.xlabel("Mean rating")

    return fig


def shops_ratings_amounts_graph(data):
    shops_list = sum(shops.values(), [])

    values = [
        len(get_specific_shops(data, [shop])["Observation"]) for shop in shops_list
    ]

    df = pd.DataFrame({"shops": shops_list, "amount": values})
    fig, ax = plt.subplots()
    df.plot.barh("shops", "amount", ax=ax)

    plt.title("Amount of ratings for all shops")
    plt.ylabel("Shops")
    plt.xlabel("Amounts")

    return fig


def academies_ratings_amounts_graph(data):
    academies_list = shops.keys()

    values = [
        len(get_specific_shops(data, shops[academy])["Observation"])
        for academy in academies_list
    ]

    df = pd.DataFrame({"academies": academies_list, "amount": values})
    fig, ax = plt.subplots()
    df.plot.barh("academies", "amount", ax=ax)

    plt.title("Amount of ratings for all academies")
    plt.ylabel("Academies")
    plt.xlabel("Amounts")

    return fig
