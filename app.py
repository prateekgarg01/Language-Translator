from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st


groq_api_key="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"
model = ChatGroq(model="Gemma2-9b-it",api_key=groq_api_key)
generic_template="Translate the following into {language}:"
prompt=ChatPromptTemplate.from_messages(
    [("system",generic_template),("user","{text}")]
)


parser = StrOutputParser()

chain=prompt|model|parser
st.title("Language Translator")
input_text=st.text_input("Type The Word or Sentence")
input_language=st.text_input("Type the Language in which you want to Transalate the Text")

if st.button("Translate"):
    st.write("**Translated Output :**",chain.invoke({"language":input_language,"text":input_text}))