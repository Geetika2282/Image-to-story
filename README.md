# 📸 AI Audio Story Generator

Upload an image, and this app will:
1. Generate a caption using a vision model.
2. Use that caption to generate a short fictional story.
3. Convert the story into audio using TTS.

Deployed using Streamlit and Hugging Face Spaces with only free resources.

## 🧰 Tech Stack
- BLIP (Image Captioning)
- Hugging Face LLMs (Story Gen)
- Coqui TTS (Text-to-Speech)
- Streamlit UI

## 🚀 Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
