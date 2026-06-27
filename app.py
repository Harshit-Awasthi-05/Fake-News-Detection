import streamlit as st
import pickle
import re


@st.cache_resource
def load_models():
    
    with open("model.pkl", 'rb') as f:
        model = pickle.load(f)
    with open("tfidf.pkl", 'rb') as f:
        tfidf = pickle.load(f)
    return model, tfidf


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", '', text)
    text = " ".join(text.split())
    return text


model, tfidf = load_models()

st.title("Fake News (Scam) Detection APP")
st.write("Paste your text here to find out if it is real or fake.")

text = st.text_input("Enter Text here...")

if st.button("Detect"):
    if text:
        clean_input = clean_text(text)
        text_converted = tfidf.transform([clean_input])
        prediction = model.predict(text_converted)[0]


        if prediction == 1:
            
            st.success("Real Text, No Scam is here...")
        else:
            st.warning("Fake News, Scam Alert...")
    else:
        st.warning("Please enter some text to detect.")