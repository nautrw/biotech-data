import pandas as pd
import streamlit as st

import biotech_data.graphing as graphing
from biotech_data.utils import pregraph

data = pd.read_csv("data.csv")

st.header("Biotech Data Analysis")

data = pregraph(data)

# st.pyplot(graphing.shops_mean_graph(data))
# st.pyplot(graphing.academies_mean_graph(data))
# st.pyplot(graphing.shops_ratings_amounts_graph(data))
# st.pyplot(graphing.academies_ratings_amounts_graph(data))
graphing.shops_mean_graph_test(data)
