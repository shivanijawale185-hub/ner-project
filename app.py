import streamlit as st
import spacy

# Load spaCy model
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# App title
st.title("🧠 Named Entity Recognition (NER) using spaCy")
st.write("Enter a sentence to extract named entities.")

# Text input
txt = st.text_area(
    "Enter text",
    "Virat Kohli was born in Delhi and plays cricket for India"
)

# Process text
if txt:
    result = nlp(txt)

    st.subheader("🔍 Extracted Entities")

    if result.ents:
        for ent in result.ents:
            st.write(f"**Entity:** {ent.text}")
            st.write(f"**Label:** {ent.label_}")
            st.markdown("---")
    else:
        st.warning("No entities found.")
