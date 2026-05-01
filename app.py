import streamlit as st
from google import genai
from prompt_engine import build_prompt

# ========================
# CONFIG
# ========================
import os

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "models/gemini-2.5-flash"

client = genai.Client(api_key=API_KEY)

st.set_page_config(
    page_title="AI Personal Chef",
    page_icon="👨‍🍳",
    layout="centered"
)

# ========================
# DARK MODE CSS
# ========================
st.markdown("""
<style>
body {
    background-color: #0f1117;
}

.stApp {
    background: linear-gradient(135deg, #0f1117, #1c1f26);
    color: white;
}

h1 {
    text-align: center;
    font-weight: 700;
    letter-spacing: 1px;
}

.recipe-card {
    background: rgba(255, 255, 255, 0.05);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(0, 255, 150, 0.15);
    margin-top: 25px;
}

textarea, .stTextArea textarea {
    background-color: #1e222b !important;
    color: white !important;
    border-radius: 10px !important;
}

.stButton>button {
    background: linear-gradient(90deg, #00ff99, #00ccff);
    color: black;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 25px;
}

.stSelectbox div {
    background-color: #1e222b !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ========================
# UI HEADER
# ========================
st.markdown("<h1>👨‍🍳 AI Personal Chef</h1>", unsafe_allow_html=True)
st.markdown("<center>Creative • Frugal • Zero Waste</center>", unsafe_allow_html=True)

st.markdown("---")

# ========================
# INPUT SECTION
# ========================
ingredients = st.text_area("🥕 Enter available ingredients (comma separated)")
diet = st.selectbox(
    "🥗 Select dietary restriction",
    ["None", "Vegan", "Keto", "Vegetarian", "High Protein"]
)

# ========================
# GENERATE
# ========================
if st.button("🔥 Generate Gourmet Recipe"):

    if not ingredients.strip():
        st.warning("Please enter ingredients.")
    else:
        with st.spinner("Chef Remy is crafting magic... ✨"):

            prompt = build_prompt(ingredients, diet)

            try:
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt
                )

                st.markdown(
                    f"""
                    <div class="recipe-card">
                    {response.text}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error("Something went wrong:")
                st.write(e)
