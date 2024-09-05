from dotenv import load_dotenv
load_dotenv() # activate the Local Env Variables.

import streamlit as st
import os
import google.generativeai as genai

 #Setup the local environment for the Google API key
genai.configure(api_key = "AIzaSyBm4WwkBWw85kt0rsDzXH4rnJKVtQlkOmk")
 
 #Gen AI Model
model = genai.GenerativeModel('gemini-pro')
 
 # Function to generate the content
def generate(question):
     response = model.generate_content(question)
     return(response.text)
 
 ### Streamlit Webpage ####
st.set_page_config(page_title='LLM QnA Application')
st.header('Generating Answers using Gemini Pro')
# Streamlit run app.py to run the application
input = st.text_input(label='Ask the Question',key='input')

submit = st.button('Generate Response')

if submit:
    response = generate(input)
    st.subheader('The Response is : ')
    st.write(response)
    
    
