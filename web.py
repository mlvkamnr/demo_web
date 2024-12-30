import streamlit as st
import pandas as pd

#dataset = pd.read_csv("water_potability.csv")
#st.dataframe(dataset)

#st.title("Welcome to my cookery labs")
#st.markdown("SERVED WITH LOVE")
#st.header("My orders")
#st.subheader("Contact")
#st.code(""" for i in range(1,5,1):
             #print("Hello world")
                  #""")
                
                
                
name = st.text_input("Enter Your Name :")
fname = st.text_input("Enter Your Father's Name :")
adr = st.text_area("Enter Your Text:")
classdata = st.selectbox("Enter your class :",(1,2,3,4,5,6))


button=st.button("Done")
if button:
    st.markdown(f""""
    Name :{name}
    Father Name :{fname}
    address:{adr}
    class:{classdata}""")

