# Import Necessary libraries
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

#Load Environment
load_dotenv()

# Load GROQ API Key from Environment
with st.sidebar:
    groq_api_key=st.text_input("Groq API Key",type="password")

# Define custom CSS
custom_css = """
<style>

.st-emotion-cache-187vdiz {
    background-color: #3295a8; 
    color: white; /* White text */
    border-radius: 8px; /* Rounded corners */
    padding: 10px 20px; /* Padding */
    font-size: 16px; /* Font size */
}
.st-emotion-cache-187vdiz:hover {
    background-color: #ff4b4b;
}
</style>
"""

# Inject CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Select Model from Groq
model = ChatGroq(groq_api_key=groq_api_key,model="Gemma2-9b-it")

# Define Prompt Template
generic_template="Translate the following into {language}:"
prompt=ChatPromptTemplate.from_messages(
    [("system",generic_template),("user","{text}")]
)

# Initialize String out Parser
parser = StrOutputParser()

# Define the Chain
chain=prompt|model|parser

# Streamlit App

## Title
st.title("Language Translator using Gemma2-9B LLM Model")

## Input Fields
input_text=st.text_input("Type The Word or Sentence","Hello")
input_language=st.text_input("Translation Language","Swedish")

## Define Button along witha call to chain.
if st.button("Translate"):
    st.write("**Translated Output :**",chain.invoke({"language":input_language,"text":input_text}))
