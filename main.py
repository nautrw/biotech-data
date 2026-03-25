import pandas as pd
import streamlit as st

import graphing as graphing
from utils import pregraph

data = pd.read_csv("data.csv")

st.header("Biotech Data Analysis")

data = pregraph(data)

st.pyplot(graphing.shops_mean_graph(data))
st.pyplot(graphing.academies_mean_graph(data))
st.pyplot(graphing.shops_ratings_amounts_graph(data))
st.pyplot(graphing.academies_ratings_amounts_graph(data))
