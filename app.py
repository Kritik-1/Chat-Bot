from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro-Model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question) -> None:
    response = model.generate_content(question)
    return response.text

## Initialize our streamlit application
st.set_page_config(page_title="Summer Internship Poornima")
st.header("Titu mama Ai Indore Wala")
input = st.text_input("Input: " , key = "input")
submit = st.button("Aee Beta:")

## When user submit is clicked
if submit :
    response = get_gemini_response(input)
    st.subheader("The response is ")
    st.write(response)
