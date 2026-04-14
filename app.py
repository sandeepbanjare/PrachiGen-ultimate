import streamlit as st
import google.generativeai as genai

# API Key dhyan se quotes mein daalna
API_KEY = "AIzaSyBlKXwwGmVQ1BwNg34wH59yxc2dfFpkfS4"

genai.configure(api_key=API_KEY)

# SABSE IMPORTANT CHANGE: Model ka naam fixed version mein
# 'gemini-pro' ya 'gemini-1.5-flash' ki jagah ye use karo
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

st.title("🚀 PrachiGen Ultimate")

topic = st.text_input("Topic dalo:")

if st.button("Generate Script"):
    if topic:
        try:
            # Response lene ka naya tarika
            response = model.generate_content(topic)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
          
