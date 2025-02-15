import streamlit as st
import openai

# OpenAI API Key (Replace with your own key)
OPENAI_API_KEY = "AIzaSyDCi65n5TeUCk592gPnnXzHZUjgQoDIiAo"

# Configure Streamlit page settings
st.set_page_config(
    page_title="Smart AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# Custom Styling
st.markdown(
    """
    <style>
        body {
            font-family: 'Verdana', sans-serif;
            background-color: #eef2ff;
            color: #333;
        }
        .main-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: #4a4e69;
        }
        .input-container {
            padding: 15px;
            background: #fff;
            border-radius: 10px;
            box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .response-box {
            padding: 15px;
            background: #f4f4f8;
            border-radius: 10px;
            box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }
        .generate-button {
            background-color: #6c5ce7;
            color: white;
            font-weight: bold;
            padding: 12px 20px;
            border-radius: 8px;
            border: none;
            width: 100%;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .generate-button:hover {
            background-color: #4b4adb;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Header
st.markdown("<div class='main-title'>AI Code Analyzer</div>", unsafe_allow_html=True)

# User Input
st.markdown("### Paste your code or describe your issue below:")
user_query = st.text_area("", placeholder="Enter code or problem description...", height=150)

# Generate Response Button
if st.button("Generate Response", key="generate_response", help="Click to analyze your code"):
    if user_query.strip():
        try:
            openai.api_key = OPENAI_API_KEY
            
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant that analyzes code and provides feedback."},
                    {"role": "user", "content": user_query}
                ]
            )
            
            ai_response = response["choices"][0]["message"]["content"].strip()
            
            # Display AI Response
            st.markdown("<div class='response-box'>", unsafe_allow_html=True)
            st.markdown("#### AI Response:")
            st.code(ai_response, language="python")
            st.markdown("</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid prompt!")
