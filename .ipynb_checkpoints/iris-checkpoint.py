import streamlit as st
import pickle
from sklearn.datasets import load_iris

st.title("Iris Data Classifier")

sepal_length = st.number_input(label="Sepal Length", min_value=4.3,max_value=7.9,value=5.8,step=.1)
sepal_width = st.number_input(label="Sepal Width", min_value=2.0,max_value=4.4,value=3.0,step=.1)
petal_length = st.number_input(label="Petal Length", min_value=1.0,max_value=6.9,value=4.3,step=.1)
petal_width = st.number_input(label="Petal Width", min_value=.1,max_value=2.5,value=1.30,step=.1)

submit = st.button('Submit Measurements')

if submit:
  irisclassifier = pickle.load(open('irisclassifier', 'rb'))
  result = irisclassifier.predict([[sepal_length,sepal_width,petal_length,petal_width]])

  if result == 0:
    pred = 'Iris Setosa'
  elif result == 1:
    pred = 'Iris Virginica'
  else:
    pred = 'Iris Versicolor'
  
  st.success(f"Model Prediction is {pred}")