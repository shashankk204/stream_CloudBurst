import streamlit as st
import xgboost as xgb
# import pickle as pk
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
import streamlit as st
# model=pk.load(open("SIH_MODEL.pkl","rb"))
loaded_model = xgb.Booster()
loaded_model.load_model("xgboost_model.txt")
st.title("CloudBurst")

# Create a form
input=[0]*18
st.write("Enter your input data below:")
with st.form("Submit Form"):
    # Add form elements    
    input[0] = st.number_input("MinTemp:")
    input[1] = st.number_input("MaxTemp:")
    input[2] = st.number_input("Evaporation:")
    input[3] = st.number_input("Sunshine:")
    input[4] = st.number_input("WindGustDir:")
    input[5] = st.number_input("WindGustSpeed:")
    input[6] = st.number_input("WindDir9am:")
    input[7] = st.number_input("WindDir3pm:")
    input[8] = st.number_input("WindSpeed9am:")
    input[9] = st.number_input("WindSpeed3pm:")
    input[10] = st.number_input("Humidity9am:")
    input[11] = st.number_input("Humidity3pm:")
    input[12] = st.number_input("Pressure9am:")
    input[13] = st.number_input("Pressure3pm:")
    input[14] = st.number_input("Cloud9am:")
    input[15] = st.number_input("Cloud3pm:")
    input[16] = st.number_input("Temp9am:")
    input[17] = st.number_input("Temp3pm")

    # Add a submit button
    submitted = st.form_submit_button("Submit")

# Handle form submission
if submitted:

    input_array=np.array(input).reshape(1,-1)
    pred = loaded_model.predict(xgb.DMatrix(input_array))
    pred[pred<0]=0
    st.write("predicted=",pred[0],"%")
