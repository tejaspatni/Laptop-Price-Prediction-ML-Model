#Importing Libraries
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻",
                   layout="wide")

#import model
st.title("Laptop Price Predictor 💻")
pipe=pickle.load(open("pipe.pkl","rb"))
dataset=pickle.load(open("dataset.pkl","rb"))

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # Processor input
    Processor = st.selectbox("Processor", dataset["Processor"].unique())

with middle_column:
    # OS
    OS = st.selectbox("OS", dataset["OS"].unique())

with right_column:
    # Ram
    RAM = st.selectbox("RAM", dataset["RAM"].unique())

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # SSD
    SSD = st.selectbox("SSD", dataset["SSD"].unique())

with middle_column:
    #HDD
    HDD = st.selectbox("HDD", dataset["HDD"].unique())
    

with right_column:
    #EMMC
    EMMC = st.selectbox("EMMC", dataset["EMMC"].unique())

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # Display_size
    Display_size = st.selectbox("Display_size", dataset["Display_size"].unique())

with middle_column:
    # Touchscreen
    Touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])


if st.button("Predict Price"):
    if Touchscreen=="Yes":
        Touchscreen=1
    else:
        Touchscreen=0


    query=np.array([Processor, OS, RAM, SSD, HDD, EMMC, Display_size, Touchscreen])
    prediction = str(int(np.exp(pipe.predict(query)[0])))
    query=query.reshape(1, 8)
    st.title("The price for the following configuration is ₹ {0}/-".format(prediction))