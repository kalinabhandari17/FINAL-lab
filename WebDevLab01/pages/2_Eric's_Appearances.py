import streamlit as st
import pandas as pd
import json


st.title("Eric Cartman Data of Appearances")
st.write("This app explores episode-level data about Eric Cartman from *South Park*. Filter and analyze chaos levels, ratings, and appearances.")



with open("data.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)


if "views" not in st.session_state:
    st.session_state.views = 0
st.session_state.views += 1
st.sidebar.write(f"🔄 Views this session: {st.session_state.views}")


st.sidebar.header("Filter Episodes")
selected_season = st.sidebar.selectbox("Select Season", sorted(df["season"].unique()))  # Input 1
rating_threshold = st.sidebar.slider("Minimum Episode Rating", 1.0, 10.0, 7.0, 0.1)      # Input 2


filtered_df = df[(df["season"] == selected_season) & (df["rating"] >= rating_threshold)]


st.subheader("Eric Cartman appearances by Season")
st.bar_chart(df.groupby("season")["appearance_count"].sum())  # static chart


st.subheader(f"Ratings by episode name (Season {selected_season})")
st.line_chart(filtered_df.set_index("episode")["rating"])  # NEW


st.subheader("Cartman's chaos per episode (Filtered by Season)")
st.bar_chart(filtered_df.set_index("episode")["chaos_level"])  # NEW


st.success("Dashboard updated with your selections!")  # NEW


st.markdown("---")
st.markdown("CS 1301 | Lab 02 - Phase II | Streamlit-only version")
