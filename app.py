from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# Define custom CSS
custom_css = """
<style>

.st-emotion-cache-187vdiz {
    background-color: #ff4b4b; /* Red background */
    color: white; /* White text */
    border-radius: 8px; /* Rounded corners */
    padding: 10px 20px; /* Padding */
    font-size: 16px; /* Font size */
}
.st-emotion-cache-187vdiz:hover {
    background-color: #3295a8; /* Darker red on hover */
}
</style>
"""

# Inject CSS
st.markdown(custom_css, unsafe_allow_html=True)

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
