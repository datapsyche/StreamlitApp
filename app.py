import streamlit as st
import pickle

st.title("Spam Classifier Application using Streamlit")

user_input = st.text_area("Please paste your message here... ", "your message")

classifier = pickle.load(open('spamclassifier', 'rb'))
result = classifier.classify(user_input)

if user_input != "your message":
  st.text(f"Your Message is {result}")