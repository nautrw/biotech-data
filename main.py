import pandas as pd

data = pd.read_csv("data.csv")


def exclude_spore_colonies(data):
    return data.set_index("Observation").drop("Spore Colonies").reset_index()


def quantify_observations(data):
    values = {"None": 0, "Below Average": 1, "Average": 2, "Above Average": 3}

    data["Observation"] = data["Observation"].replace(values)

    return data
