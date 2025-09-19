import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env and get GEMINI_API_KEY
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found in .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI setup
st.set_page_config(page_title="🌙 Dream Interpreter", layout="centered")

# Header UI
st.markdown("""
    <h1 style='text-align:center; color:#6C63FF;'>🌠 Rajini Dream Interpreter</h1>
    <p style='text-align:center; font-size:18px;'>Type your dream and Rajini will interpret it using imagination and deep psychology.</p>
    <hr style="border-top: 1px solid #aaa;">
""", unsafe_allow_html=True)

# Input box
user_dream = st.text_area(
    "💭 Describe your dream:",
    placeholder="e.g., I flew into the clouds riding a turtle made of light...",
    height=200
)

# Submit button
if st.button("Interpret My Dream ✨") and user_dream.strip():
    with st.spinner("Rajini is interpreting your dream..."):

        # Construct the prompt
        prompt = f"""
You are a poetic and psychologically insightful AI dream interpreter.

The user had the following dream:

\"{user_dream.strip()}\"

Give a powerful, imaginative interpretation using:
- Symbolism (Jung, archetypes, emotions)
- Freudian psychology (desires, repression)
- Surreal creativity and storytelling
- Insight into the dreamer's emotional or subconscious state

Respond in 1st person as an all-knowing dream oracle. Be vivid, wise, and profound.
"""

        try:
            # Get Gemini's response
            response = model.generate_content(prompt)

            if response and hasattr(response, "text") and response.text.strip():
                interpretation = response.text.strip()

                st.markdown("### 🧠 rajini’s Interpretation:")
                st.markdown(
                    f"""
                    <div style='
                        background-color: #eef2f7;
                        padding: 20px;
                        border-left: 5px solid #6C63FF;
                        border-radius: 10px;
                        font-size: 16px;
                        color: #333;
                        line-height: 1.6;
                    '>
                    {interpretation.replace("\n", "<br>")}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.warning("⚠️ Gemini did not return an interpretation. Try rephrasing your dream.")

        except Exception as e:
            st.error("❌ Gemini failed to interpret your dream.")
            st.exception(e)
else:
    st.info("Type your dream above and click the button to get a unique interpretation.")
