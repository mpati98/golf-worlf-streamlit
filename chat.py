import streamlit as st
import streamlit.components.v1 as components

# Assume your React chatbot is hosted at this URL
react_chatbot_url = "https://golf-world-bot.vercel.app/"

# Embed the React chatbot using an iframe
components.html(
    f'<iframe src="{react_chatbot_url}" width=100% height=500></iframe>',
    scrolling=True,
    width=750,
    height=2000,  # Adjust the height as needed
)