import streamlit as st

pages = {
    "Take your journey": [
        st.Page("home.py", title="Home"),
        st.Page("product.py", title="Product"),
        st.Page("golfClass.py", title="Golf Class"),
        st.Page("about.py", title="About"),
    ],
}
pg = st.navigation(pages)
pg.run()