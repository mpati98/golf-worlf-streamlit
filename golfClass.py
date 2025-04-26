import streamlit as st
import myFunc as Func

with st.form("my_form"):
    st.title("Registration for free")
    name = st.text_input(
            "Name",
            placeholder="Your name"
            )
    email = st.text_input(
            "Email",
            placeholder="Your email"
            )

    phone = st.text_input(
            "Phone",
            placeholder="Your phone",
            )

    message = st.text_area(
            "Message",
            placeholder="Your message",
            )


        # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
            Func.create_customer(name, email, phone,message)
            st.toast("Your submit was recorded!")
st.write("Outside the form")