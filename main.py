import pandas as pd

data = pd.read_csv("data.csv")

def Start(data):
    data = exclude_spore_colonies(data)
    data = exclude_no_shop(data)
    return data

def exclude_spore_colonies(data):
    return data.set_index("Observation").drop("Spore Colonies").reset_index()


def exclude_no_shop(data):
    # `NaN` corresponds to `N/A` in the data
    return data.set_index("Academy").drop(float("nan")).reset_index()


def quantify_observations(data):
    values = {"None": -2.0, "Below Average": -1.0, "Average": 0.0, "Above Average": 1.0}

    data["Observation"] = data["Observation"].replace(values)

    return data


def get_full_mean(data):
    return float(data["Observation"].mean())

def get_specific_shop(data, shopName):
    return data.loc[data["General Location"] == shopName]