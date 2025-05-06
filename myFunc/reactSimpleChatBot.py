import streamlit as st
import streamlit.components.v1 as components
    
def render_chat_bot():
        chat_bot = components.declare_component(
            "chat_bot",
            url="http://localhost:5173", # Replace with your React dev server URL or build URL
        )
        return chat_bot()
    
if __name__ == "__main__":
        st.title("Streamlit Chatbot")
        render_chat_bot()