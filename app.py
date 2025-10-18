import streamlit as st
from transformers import pipeline

# -------------------------
# Load summarization model
# -------------------------
# This loads the "facebook/bart-large-cnn" model for summarization
@st.cache_resource  # Caches the model to avoid reloading every time
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# -------------------------
# Streamlit UI
# -------------------------
st.title("📝 Hugging Face Text Summarizer")
st.write("Paste your text below and get a concise summary!")

# Input text from user
user_text = st.text_area("Enter text to summarize:", height=200)

# Button to summarize
if st.button("Summarize"):
    if user_text.strip() == "":
        st.warning("Please enter some text!")
    else:
        try:
            # Summarize the text
            summary = summarizer(user_text, max_length=120, min_length=30, do_sample=False)
            st.success("Summary:")
            st.write(summary[0]['summary_text'])

        except Exception as e:
            st.error(f"Error: {e}")
