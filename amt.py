import streamlit as st
import spacy
from spacy import displacy
import en_core_web_sm
import requests
#from newspaper import article
st.title("Named Entity Recognizer")
st.info("This app will take an input from the user and then print the named entities")

text = st.text_area("Enter a paragraph")
url = st.text_input("Enter a URL")

if st.button("Submit"):
    if url:
        response = requests.get(url)
        text = response.text

        nlp = en_core_web_sm.load()
        doc = nlp(text)
        html = displacy.render(doc, style="ent", jupyter=False)
        st.markdown(html, unsafe_allow_html=True)


