import pickle 
import streamlit as st 

# load model and tfidf 
model = pickle.load(open("model.pkl",'rb'))
tfidf = pickle.load(open("tfidf.pkl",'rb'))

import re

def clean_text(text):
    # Convert to string first
    text = str(text).lower()  
    
    # Remove unwanted characters
    text = re.sub(r"[^a-z0-9\s]", '', text)   
    
    # Remove multiple spaces
    text = " ".join(text.split())
    
    return text


# Streamlit UI
st.title("Fake News (Scam) Detection APP")
st.write("Paste your text here and find out it, is it real or fake")

text = st.text_input("Enter Text here...")

if st.button("Detect"):
    text = clean_text(text)
    text_converted = tfidf.transform([text])

    prediction = model.predict(text_converted)[0]

    if prediction == 1:   
        st.success("Real Text, No Scam is here...")
    else:            
        st.warning("Fake News, Scam Alert...")