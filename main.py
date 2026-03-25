import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")

shops = {
    "Alden Academy": [
        "Advanced Manufacturing",
        "Auto Collision",
        "Auto Technology",
        # "Computer Aided Drafting", # No data on CAD
        "Robotics & Automation Technology",
        "Welding",
    ],
    "Allied Health and Human Services Academy": [
        "Allied Health",
        # "Biotechnology", # No data on Biotech
        "Environmental Tech",
        "Veterinary Assisting",
        "Cosmetology",
        "Early Childhood",
    ],
    "Coughlin Construction Academy": [
        "Carpentry",
        "Electrical",
        "Hvac/R",
        "Painting & Design",
        "Plumbing",
    ],
    "IT and Business Services Academy": [
        "Culinary Arts",
        # "Finance, Marketing, & Business Management", # No data on finance
        "Hospitality Management",
        "Information Support Services & Networking",
        "Programming & Web Development",
        "Graphic Communication",
    ],
}


def pregraph(data):
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
    # values = {"None": -2.0, "Below Average": -1.0, "Average": 0.0, "Above Average": 1.0}

    values = {"None": 0, "Below Average": 1, "Average": 2, "Above Average": 3.0}

    data_copy = data.copy()
    data_copy["Observation"] = data_copy["Observation"].replace(values)

    return data_copy


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

    df = pd.DataFrame({"shops": shops_list, "mean": values})
    ax = df.plot.barh("shops", "mean")
    ax.set_xticklabels(
        ["None", "", "Below Average", "", "Average", "", "Above Average"]
    )

    plt.title("Mean rating for all shops")
    plt.ylabel("Shops")
    plt.xlabel("Mean rating")
    plt.tight_layout()
    plt.show()
