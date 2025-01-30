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
  # species= st.selectbox("Species",('Adelie' ,'Gentoo', 'Chinstrap'))
  island= st.selectbox("Island",('Torgersen' ,'Biscoe', 'Dream'))
  sex= st.selectbox("Sex",("male","female"))
  bill_length_mm= st.slider("Bill Length(mm)",int(df["bill_length_mm"].min()),int(df["bill_length_mm"].max()),int(df["bill_length_mm"].mean()))
  bill_depth_mm= st.slider("Bill depth(mm)", int(df["bill_depth_mm"].min()), int(df["bill_depth_mm"].max()),int( df["bill_depth_mm"].min()))
  flipper_length_mm= st.slider("Flipper length(mm)",df["flipper_length_mm"].min(), df["flipper_length_mm"].max(), int(df["flipper_length_mm"].mean()))
  body_mass_g= st.slider("Body Mass(grams)", int(df["body_mass_g"].min()), int(df["body_mass_g"].max()), int(df["body_mass_g"].mean()))

# df["flipper_length_mm"]
# cols
# for col in cols:
  # st.write(f"Column name:{col}\n\n {df[col].unique()}")

#creating a dataframe for input features 
  data={"island": island,"sex": sex,"bill_length_mm":bill_length_mm,"bill_depth_mm":bill_depth_mm,"flipper_length_mm":flipper_length_mm,
      "body_mass_g": body_mass_g}
  input_df= pd.DataFrame(data, index=[0])
  combined_df= pd.concat([input_df,X], axis=0)
#input_df

with st.expander("**New input feature**"):
  st.write("input feature")
  input_df
  st.write("combined test dataframe")
  combined_df

encode_cols=["sex","island"]
combined_df= pd.get_dummies(combined_df, prefix=encode)
combined_df[:3]
