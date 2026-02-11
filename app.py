import streamlit as st
import pandas as pd
#text element
st.header("Streamlit core feature")
st.subheader("Text element")
st.text("This is asimple element")

#data display
st.subheader("Data display")
st.write("Here is a simple element")
df=pd.DataFrame({
    "Date":["2024-08-01","2024-08-02","2024-08-03","2024-08-04"],
    "Amount":[105,204,303,408]
})
st.table(df)

#charts
st.subheader("Charts")
st.line_chart([1,2,3,4])
#user input

st.subheader("User input")
value = st.slider("Select a value", 0, 100)
st.write(f"Selected value: {value}")

================================================


import streamlit as st
#checkbox
st.header("Interactive widget example")
if st.checkbox("Show/hide"):
    st.write("Checkbox is checked !")
#selectbox
option=st.selectbox("Category",["rent","food"], label_visibility="collapsed")
st.write(f"Selected option: {option}")

#multiselect
option=st.multiselect("Select multiple number",[1,2,3,4])
st.write(f"Selected option: {option}")








































