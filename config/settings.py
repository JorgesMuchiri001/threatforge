import streamlit as st

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
MODEL_NAME = st.secrets.get("MODEL_NAME", "gpt-4o-mini")

llm_config = {
    "config_list": [
        {
            "model": MODEL_NAME,
            "api_key": OPENAI_API_KEY
        }
    ],
    "temperature": 0.2,
    "timeout": 120,
}