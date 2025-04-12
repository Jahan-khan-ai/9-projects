import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt       "igot n errer in streamlit"

st.title ("Simple Data Dashboard")
uploaded_file = st.file_uploader("chose a csv file",type = "csv")

if uploaded_file is not None:
     df = pd.read_csv (uploaded_file)

     st.subheader("Data Preview")
     st.write(df.head())

     st.subheader("Data Summary")
     st.write(df.describe())

     st.header("Filter Data")
     columns = df.columns.tolist()
     selected_columns = st.selectbox("select column to filter by",columns)
     unique_values =df[selected_column].unique()
     selected_value = st.selectbox("select value",unique_values)

     filtered_df = [df[selected_column] == selected_value]
     st.write(filtered_df)

     st.subheader('Plot Data')
     x_column = st.selectbox("select x-axis column",columns)
     y_column = st.selectbox("select y-axis column",columns)

     if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
        
else:
    st.write("Waiting on a file upload...")
