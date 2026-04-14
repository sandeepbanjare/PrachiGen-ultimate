import streamlit as st
import google.generativeai as genai

# Nayi API Key yahan dalo
API_KEY = "AIzaSyBdBdJ4tB_Likanjw_tW4FqFtxKWUVXl8s"

genai.configure(api_key=API_KEY)

st.title("🚀 PrachiGen Ultimate")
topic = st.text_input("Apni video ka topic dalo:")

if st.button("Magic Karo"):
    if topic:
        with st.spinner('AI soch raha hai...'):
            try:
                # Direct call bina kisi version jhamela ke
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(topic)
                st.balloons()
                st.success("Taiyar hai!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Kuch toh likho bhai!")
          
