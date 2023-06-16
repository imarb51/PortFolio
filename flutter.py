import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="pages",
    layout="centered")

col1, col2 = st.columns(2)
with col1:
    st.image("images/flutter.py.png")
with col2:
    st.title("Flutter")
    content = """
    This is the Page where I have developed 10+ Flutter Projects in all fields.
    """
    st.info(content)

content2 = """
Below you can find the projects which I have developed or the projects where I have added some features.
"""
st.write(content2)
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("flutter.csv", sep=";")

with col3:
    for index, row in df[:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[4:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")