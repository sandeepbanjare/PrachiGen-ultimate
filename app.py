import streamlit as st
import google.generativeai as genai

# Nayi API Key yahan dalo
API_KEY = "AIzaSyBj41MkCvC-eG7FudDJBzPPQgvRxJKve6A"

# Force version v1
genai.configure(api_key=API_KEY, transport='rest')

st.title("🚀 PrachiGen Ultimate")
topic = st.text_input("Topic:")

if st.button("Magic Karo"):
    if topic:
        try:
            # Hum generic model name use karenge jo auto-update hota hai
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            response = model.generate_content(topic)
            st.success("Success!")
            st.write(response.text)
        except Exception as e:
            # Agar latest nahi chala toh base model try karega
            try:
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(topic)
                st.write(response.text)
            except:
                st.error("Google Server busy hai, 1 min baad try karein.")
                                              
