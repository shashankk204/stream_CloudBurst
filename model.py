import xgboost as xgb
# import pickle as pk
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
import streamlit as st
# model=pk.load(open("SIH_MODEL.pkl","rb"))
loaded_model = xgb.Booster()
loaded_model.load_model("xgboost_model.txt")
# X=pd.read_csv('imputed_test.csv')
# y=X.pop('Rainfall')
# x_val=pd.read_csv('imputed_train.csv')
# y_val=x_val.pop("Rainfall")
# X_train=np.concatenate((X,x_val),axis=0)
# y_train=np.concatenate((y,y_val),axis=0)
# pred = loaded_model.predict(xgb.DMatrix(X_train))

st.title("Machine Learning Model Deployment")
st.write("Enter your input data below:")
input=[0]*18
input[0] = st.number_input("Enter the first number:")
input[1] = st.number_input("Enter the second number:")
input[2] = st.number_input("Enter the third number:")
input[3] = st.number_input("Enter the thi4d number:")
input[4] = st.number_input("Enter the first5 number:")
input[5] = st.number_input("Enter the second6 number:")
input[6] = st.number_input("Enter the third n7umber:")
input[7] = st.number_input("Enter the third nu8mber:")
input[8] = st.number_input("Enter the first num9ber:")
input[9] = st.number_input("Enter the second nu10mber:")
input[10] = st.number_input("Enter the third numbe12r:")
input[11] = st.number_input("Enter the third numb4er:")
input[12] = st.number_input("Enter the first numbe65r:")
input[13] = st.number_input("Enter the second num7ber:")
input[14] = st.number_input("Enter the third numbe87r:")
input[15] = st.number_input("Enter the third numbe134r:")
input[16] = st.number_input("Enter the t5hird numbe134r:")
input[17] = st.number_input("Enter the third number:143")


# Use the input values
input_array=np.array(input).reshape(1,-1)
pred = loaded_model.predict(xgb.DMatrix(input_array))
st.write("predicted=",pred[0],"%")

# Check if the user has provided input data
# if input_data1 and input_data2:
#     # Convert the input data to a format that your model expects
#     # For example, if your model expects numerical input, you might need to convert it

#     # Make a prediction
#     result = input_data1, input_data2  # Assuming your model expects a list of inputs

#     # Display the result
#     st.write("Prediction:", result)