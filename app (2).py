import google.generativeai as genai
import textwrap
import streamlit as st

# ✅ ✅ HARD CODED KEY — WORKS IMMEDIATELY
genai.configure(api_key="AIzaSyAtH_xzMbDUMMYKEY")

KELLY_SYSTEM_PROMPT = """
You are Kelly, an AI Scientist and Poet.
You respond ONLY in poetic form.
Your tone is analytical, skeptical, and professional.
...
"""

def get_model():
    if "model" not in st.session_state:
        with st.spinner("Loading Kelly the AI Scientist..."):
            st.session_state.model = genai.GenerativeModel("gemini-pro")
    return st.session_state.model

def get_kelly_response(question):
    model = get_model()
    prompt = f"{KELLY_SYSTEM_PROMPT}\n\nUser's question: {question}\n\nKelly's poetic response:"
    response = model.generate_content(prompt)
    return textwrap.fill(response.text, width=85)

st.set_page_config(page_title="Kelly – AI Scientist Poet", page_icon="💡", layout="centered")

st.title("💡 Kelly – AI Scientist Poet")
st.write("Ask any question about AI, and Kelly will respond poetically.")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Your Question:")

if st.button("Ask Kelly") and user_input:
    with st.spinner("Kelly is thinking..."):
        response = get_kelly_response(user_input)
        st.session_state.history.append({"user": user_input, "kelly": response})

for chat in reversed(st.session_state.history):
    st.markdown(f"🧍 You: {chat['user']}")
    st.markdown(f"🤖 Kelly:\n\n{chat['kelly']}")
    st.markdown("---")

st.markdown("✨ Developed with Gemini and Streamlit")

