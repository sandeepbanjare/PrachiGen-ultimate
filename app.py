import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
API_KEY = "AIzaSyBlKXwwGmVQ1BwNg34wH59yxc2dfFpkfS4"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- UI SETUP ---
st.set_page_config(page_title="PrachiGen AI", page_icon="🚀", layout="wide")

# Sidebar Navigation
with st.sidebar:
    st.title("🛡️ PrachiGen Pro")
    st.subheader("Creator Tool Suite")
    page = st.radio("Features", ["Video Script AI", "Viral Hook Generator", "Competitor Spy (Beta)", "Premium Upgrade"])
    st.write("---")
    st.write("Logged in as: Sandeep")

# --- FEATURE 1: SCRIPT GENERATOR ---
if page == "Video Script AI":
    st.header("🎬 Viral Video Script Generator")
    topic = st.text_input("Video ka topic ya niche dalo:", placeholder="e.g. How to grow on YouTube 2026")
    
    if st.button("Generate Script"):
        if topic:
            with st.spinner("AI dimaag laga raha hai..."):
                prompt = f"Write a high-retention YouTube script for: {topic}. Include intro, body, and call to action."
                response = model.generate_content(prompt)
                st.markdown("### Aapka Viral Script:")
                st.write(response.text)
        else:
            st.warning("Pehle topic toh dalo bhai!")

# --- FEATURE 2: HOOK GENERATOR ---
elif page == "Viral Hook Generator":
    st.header("🪝 Short-form Viral Hooks")
    concept = st.text_input("Apni video ka main point batao:")
    if st.button("Get Hooks"):
        response = model.generate_content(f"Give 5 viral hooks for a Reel/Short about: {concept}")
        st.write(response.text)

# --- FEATURE 3: COMPETITOR SPY ---
elif page == "Competitor Spy (Beta)":
    st.header("🔍 Competitor Analysis")
    st.info("Coming Soon: Isme hum YouTube API se data fetch karenge.")

# --- FEATURE 4: PAYMENT ---
elif page == "Premium Upgrade":
    st.header("💎 Go Premium")
    st.write("Unlimited access aur advanced features ke liye upgrade karein.")
    st.success("Price: ₹199 / Month")
    # Yahan apna Cosmofeed ya UPI link dalo
    st.link_button("Abhi Pay Karein (UPI)", "https://cosmofeed.com/vp/sandeep")
  
