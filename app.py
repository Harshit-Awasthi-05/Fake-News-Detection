import streamlit as st
import pickle
import re

print("Checkpoint 1: Starting to load models...")

@st.cache_resource
def load_models():
    print("Checkpoint 2: Inside load_models function")
    
    with open("model.pkl", 'rb') as f:
        print("Checkpoint 3: Opening model.pkl")
        model = pickle.load(f)
        print("Checkpoint 4: Loaded model.pkl")
        
    with open("tfidf.pkl", 'rb') as f:
        print("Checkpoint 5: Opening tfidf.pkl")
        tfidf = pickle.load(f)
        print("Checkpoint 6: Loaded tfidf.pkl")
        
    return model, tfidf

# Start the loading
model, tfidf = load_models()
print("Checkpoint 7: Models loaded and ready!")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", '', text)
    text = " ".join(text.split())
    return text

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