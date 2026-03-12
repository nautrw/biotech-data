import pandas as pd

data = pd.read_csv("data.csv")


def exclude_spore_colonies(data):
    return data.set_index("Observation").drop("Spore Colonies").reset_index()
