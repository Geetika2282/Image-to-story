import streamlit as st
from PIL import Image
import base64
from io import BytesIO
from image_captioning import generate_caption
from story_generator import generate_story
from TTS import generate_audio

st.set_page_config(page_title="Image to Audio Story", layout="centered")

st.title("🖼️ ➡️ 📖 ➡️ 🔊 Image to Audio Story Generator")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Story and Audio"):
        with st.spinner("Analyzing image and generating story..."):
            caption = generate_caption(image)
            story = generate_story(caption)
            st.markdown("### 📖 Generated Story")
            st.write(story)

            audio_path = generate_audio(story)

            if audio_path:
                st.markdown("### 🔊 Listen to the Story")
                audio_file = open(audio_path, "rb")
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/wav")
            else:
                st.error("Audio generation failed.")
