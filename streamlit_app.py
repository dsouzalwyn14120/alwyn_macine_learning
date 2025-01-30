import streamlit as st
import pandas as pd 

#reading the penguins_cleaned.csv file using the raw link
df= pd.read_csv("https://raw.githubusercontent.com/dsouzalwyn14120/data/refs/heads/master/penguins_cleaned.csv")

st.title('Machine learning app 🤖')

st.info('in this app we build a Machine Learning model!') #this is used to print text, same as print()

with st.expander("data"):
  st.write("**Raw Data**")
  df

  st.write("**X**")
  X= df.drop(["species"],axis=1)
  X

  st.write("**Y**")
  Y= df.species
  Y


  # adding some data visualization to the same application

with  st.expander("**Data Visualization**"):
  st.write("**Bill legth V/S Body mass**")
  st.scatter_chart(data=df, x="bill_length_mm", y="body_mass_g", color ="species" )

with st.sidebar:
  st.header("Input Features")
  species= st.selectbox("Species",('Adelie' 'Gentoo' 'Chinstrap'))
  island= st.selectbox("Island",('Torgersen' 'Biscoe' 'Dream'))
  sex= st.selectbox("Sex",("male","female"))
  bill_length_mm= st.slider("Bill Length(mm)",32.1,59.6, 42.9)


# cols= df.columns
# cols

# for col in cols:
  # st.write(f"Column name:{col}\n\n {df[col].unique()}")


