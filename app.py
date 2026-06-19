
import streamlit as st
from deep_translator import GoogleTranslator

# Page Configuration
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# Title and Description
st.title("🌍 AI Language Translation Tool")
st.markdown(
    "Translate text between multiple languages instantly using AI."
)

st.divider()

# Languages List
languages = [
    "english",
    "hindi",
    "french",
    "spanish",
    "german",
    "italian",
    "japanese",
    "korean",
    "russian",
    "arabic",
    "chinese",
    "portuguese",
    "dutch",
    "turkish",
    "urdu"
]

# Text Input
text = st.text_area(
    "Enter Text",
    placeholder="Type your text here..."
)

# Character Counter
st.write(f"Characters: {len(text)}")

# Language Selection
source = st.selectbox(
    "Source Language",
    languages
)

target = st.selectbox(
    "Target Language",
    languages
)

# Translate Button
if st.button("Translate"):

    if not text.strip():
        st.warning("⚠️ Please enter some text.")

    else:
        try:
            translated = GoogleTranslator(
                source=source,
                target=target
            ).translate(text)

            st.subheader("🌟 Translation Result")

            st.text_area(
                "Output",
                translated,
                height=150
            )

        except Exception:
            st.error(
                "❌ Translation failed. Please try again."
            )

# Footer
st.divider()
st.caption(
    "Developed by Sandhya | CodeAlpha AI Internship Project"
)