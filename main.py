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

    values = {"None": 0, "Below Average": 1, "Average": 2, "Above Average": 3}

    data_copy = data.copy()
    data_copy["Observation"] = data_copy["Observation"].replace(values)

    return data_copy


def get_full_mean(data):
    return float(data["Observation"].mean())


def get_specific_shops(data, shops_list):
    # The `in` keyword will NOT work
    return data.loc[data["General Location"].isin(shops_list)]


def shops_mean_graph(data):
    shops_list = sum(shops.values(), [])  # Turns the 2D array into 1D

    values = []
    for shop in shops_list:
        shop_data = get_specific_shops(data, [shop])
        values.append(shop_data["Observation"].mean())

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


def academies_mean_graph(data):
    academies_list = shops.keys()

    values = []
    for academy in academies_list:
        academy_data = get_specific_shops(data, shops[academy])
        values.append(academy_data["Observation"].mean())

    df = pd.DataFrame({"academies": academies_list, "mean": values})
    ax = df.plot.barh("academies", "mean")
    ax.set_xticklabels(
        ["None", "", "Below Average", "", "Average", "", "Above Average"]
    )

    plt.title("Mean rating for all academies")
    plt.ylabel("Academies")
    plt.xlabel("Mean rating")
    plt.tight_layout()
    plt.show()


def shops_ratings_amounts_graph(data):
    shops_list = sum(shops.values(), [])

    values = [
        len(get_specific_shops(data, [shop])["Observation"]) for shop in shops_list
    ]

    df = pd.DataFrame({"shops": shops_list, "amount": values})
    ax = df.plot.barh("shops", "amount")

    plt.title("Amount of ratings for all shops")
    plt.ylabel("Shops")
    plt.xlabel("Amounts")
    plt.tight_layout()
    plt.show()


def academies_ratings_amounts_graph(data):
    academies_list = shops.keys()

    values = [
        len(get_specific_shops(data, shops[academy])["Observation"])
        for academy in academies_list
    ]

    df = pd.DataFrame({"academies": academies_list, "amount": values})
    ax = df.plot.barh("academies", "amount")

    plt.title("Amount of ratings for all academies")
    plt.ylabel("Academies")
    plt.xlabel("Amounts")
    plt.tight_layout()
    plt.show()
