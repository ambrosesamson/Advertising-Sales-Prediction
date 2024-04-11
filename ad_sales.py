import streamlit as st  

import pickle  

import numpy as np  

 

h=open("advertising_sales.pkl","rb")  

lr=pickle.load(h)  

 

TV=st.number_input("TV:")  

Radio=st.number_input("Radio:")  

Newspaper=st.number_input("Newspaper:")   

data=[np.array([TV,Radio,Newspaper])] 

 
 

#=np.array(data).reshape(1,-1)  
prediction=lr.predict(data) 

 

if st.button("predicting sales"):  

    st.write(str(prediction)) 
