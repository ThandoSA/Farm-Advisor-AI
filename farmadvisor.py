import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

st.set_page_config(page_title="FarmAdvisor AI", page_icon="🌱", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #FDFCF7; }
    .stButton>button { background-color: #059669; color: white; border-radius: 12px; font-weight: bold; }
    .stButton>button:hover { background-color: #047857; }
    </style>
""", unsafe_allow_html=True)

# System Instruction
SYSTEM_INSTRUCTION = """You are FarmAdvisor, an expert, warm, and practical agronomist helping smallholder farmers in Kenya.
Give sustainable, low-cost, organic-first advice. Always end with "Recommended Action Steps" and the disclaimer."""

# Header
st.title("🌾 FarmAdvisor AI")
st.subheader("Your Personal Expert Agronomist 🌱")

# Sidebar
st.sidebar.markdown("## Settings")
api_key = st.sidebar.text_input("Gemini API Key", type="password", 
                                value="AQ.Ab8RN6KOKTOGmNzrJ1thRXg3F64fNOUfZSL3WOPbee-T4FPrxg")

st.sidebar.markdown("### Your Farm Profile")
county = st.sidebar.selectbox("County", ["Nakuru", "Uasin Gishu", "Kiambu", "Kakamega", "Meru"])
crop = st.sidebar.selectbox("Main Crop", ["Maize", "Beans", "Kales", "Potatoes", "Sorghum"])
soil = st.sidebar.selectbox("Soil Type", ["Loamy", "Clay", "Sandy", "Volcanic", "Black Cotton"])
season = st.sidebar.selectbox("Season", ["Long Rains", "Short Rains", "Dry Season"])

if st.sidebar.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# Initialize Model - Using a stable model name
if api_key:
    genai.configure(api_key=api_key)
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",   # Most reliable right now
            system_instruction=SYSTEM_INSTRUCTION
        )
        st.sidebar.success("✅ Gemini Connected")
    except Exception as e:
        st.error(f"Model Error: {e}")
        model = None
else:
    st.warning("Enter API Key")
    model = None

# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "model", "content": "Jambo! Upload a photo or tell me about your crop challenges."}]

# Display Chat
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "image" in msg:
            st.image(msg["image"], width=300)

# Input Area
uploaded_file = st.file_uploader("📸 Upload plant/soil photo", type=["jpg", "png", "jpeg"])
user_input = st.chat_input("Ask anything about your farm...")

if user_input or (uploaded_file and st.button("Send")):
    prompt = user_input if user_input else "Analyze this image and give advice."
    
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)
        if uploaded_file:
            image = Image.open(io.BytesIO(uploaded_file.read()))
            st.image(image, width=300)
            st.session_state.chat_history.append({"role": "user", "content": prompt, "image": image})

    # Generate Response
    if model:
        with st.spinner("FarmAdvisor is thinking..."):
            try:
                contents = [f"Farmer in {county} growing {crop} on {soil} soil during {season}. Question: {prompt}"]
                if uploaded_file:
                    contents.append(image)
                
                response = model.generate_content(contents)
                
                with st.chat_message("model"):
                    st.markdown(response.text)
                
                st.session_state.chat_history.append({"role": "model", "content": response.text})
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Model not ready.")

# Extra Feature
if st.button("📅 Generate Weekly Farm Plan"):
    if model:
        with st.spinner("Creating personalized plan..."):
            plan_prompt = f"Create a practical 7-day farm plan for a farmer in {county} growing {crop} on {soil} soil in {season}."
            response = model.generate_content(plan_prompt)
            st.success("**Your Weekly Farm Plan**")
            st.markdown(response.text)

# Resources
st.sidebar.markdown("### Quick Organic Remedies")
st.sidebar.info("Neem leaves, Wood ash, Chilli-garlic spray, Companion planting (beans + maize)")