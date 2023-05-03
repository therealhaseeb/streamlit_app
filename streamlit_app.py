import streamlit

streamlit.title("My parents new dinner healthy")

streamlit.header("Menu")

streamlit.text("Khausey")
streamlit.text("Kabab")
streamlit.text("Biryani")


import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.header("Build your own smoothie")
streamlit.dataframe(my_fruit_list)
