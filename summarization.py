from transformers import pipeline

summarizer = pipeline("summarization", device=-1)

def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

import streamlit as st

st.title("AI Text Summarizer")

user_input = st.text_area("Enter text to summarize:")

if st.button("Summarize"):
    summary = summarize_text(user_input)
    st.write("### Summary:")
    st.write(summary)