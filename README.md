# 🌾 FarmAdvisor AI

**Your Personal Expert Agronomist for Smallholder Farmers**

![FarmAdvisor](https://via.placeholder.com/800x400?text=FarmAdvisor+AI) <!-- You can replace later -->

### Problem
Smallholder farmers in Kenya often lose crops due to pests, diseases, and lack of timely expert advice. Extension services are limited and hard to reach.

### Solution
**FarmAdvisor AI** is an intelligent chatbot that acts as an on-demand agronomist. Farmers can:
- Upload photos of sick plants or soil
- Get instant diagnosis and **low-cost organic remedies**
- Receive advice tailored to their county, crop, soil type, and season
- Generate a practical **7-day farm plan**

### Key Features
- **Multimodal Image Analysis** – Upload leaf/soil photos
- Practical, organic-first recommendations (Neem, wood ash, companion planting, etc.)
- Personalized Weekly Farm Plan generator
- Warm, easy-to-understand responses with clear Action Steps

### Built With
- **Google Gemini** (Gemini 1.5 Flash) – Multimodal reasoning & image analysis
- Streamlit – Clean and responsive web interface
- Python + PIL for image handling

### How to Run Locally
```bash
pip install streamlit google-generativeai pillow
streamlit run farmadvisor.py
