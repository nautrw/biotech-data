import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")

shops = {
    "Alden Academy": [
        "Advanced Manufacturing",
        "Auto Collision",
        "Auto Technology",
        "Computer Aided Drafting",
        "Robotics & Automation Technology",
        "Welding",
    ],
    "Allied Health and Human Services Academy": [
        "Allied Health",
        "Biotechnology",
        "Environmental Tech",
        "Veterinary Assisting",
        "Cosmetology",
        "Early Childhood",
    ],
    "Coughlin Construction Academy": [
        "Carpentry",
        "Electrical",
        "HVAC/R",
        "Painting & Design",
        "Plumbing",
    ],
    "IT and Business Services Academy": [
        "Culinary Arts",
        "Finance, Marketin, & Business Management",
        "Hospitality Management",
        "Information Support Services & Networking",
        "Programming & Web Development",
        "Graphic Communication",
    ],
}


def Start(data):
    data = exclude_spore_colonies(data)
    data = exclude_no_shop(data)
    data = quantify_observations(data)
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


def get_specific_shop(data, shop_name):
    return data.loc[data["General Location"] == shop_name]


def shops_mean_graph(data):
    shops_list = sum(shops.values(), [])  # Turns the 2D array into 1D

    values = []
    for shop in shops_list:
        shop_data = get_specific_shop(data, shop)
        values.append(float(shop_data["Observation"].mean()))

    df = pd.DataFrame({"shop": shops_list, "mean": values})
    ax = df.plot.barh("shop", "mean")

    plt.title("Mean rating for all shops")
    plt.ylabel("Shops")
    plt.xlabel("Mean rating")
    plt.tight_layout()
    plt.show()
