import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
<script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
<df-messenger
  intent="WELCOME"
  chat-title="GolfLoveBot"
  agent-id="a67f10e4-262a-4c8a-b846-d5c25cb4753c"
  language-code="vi"
></df-messenger>
    """,
    height=700, # try various values to see what works best (maybe use st.slider)
)