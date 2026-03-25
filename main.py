import pandas as pd
import streamlit as st

import graphing as graphing
from utils import pregraph

data = pd.read_csv("data.csv")

st.header("Biotech Data Analysis")

data = pregraph(data)
shops_means = graphing.shops_mean_graph(data)
st.pyplot(shops_means)
