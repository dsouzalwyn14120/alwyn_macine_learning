import streamlit as st
import pandas as pd 

#reading the penguins_cleaned.csv file using the raw link
df= pd.read_csv("https://raw.githubusercontent.com/dsouzalwyn14120/data/refs/heads/master/penguins_cleaned.csv")

st.title('Machine learning app 🤖')

st.info('in this app we build a Machine Learning model!') #this is used to print text, same as print()

df
