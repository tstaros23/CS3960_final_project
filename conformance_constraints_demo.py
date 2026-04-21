import streamlit as st
import pandas as pd

st.title("Constraint Validator")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of data:")
    st.dataframe(df.head())

column = st.selectbox("Select column for range check", df.columns)
min_val = st.number_input("Min value")
max_val = st.number_input("Max value")

if st.button("Check Range"):
    #pandas uses vectors to perform operations, so I did not loop manually and applied conditions to the entire column. 
    #so we are comparing two series and creating a new series of validations
    violations = df[(df[column] < min_val) | (df[column] > max_val)]
    
    if violations.empty:
        st.success("No violations")
    else:
        st.error(f"{len(violations)} violations found")
        st.dataframe(violations)