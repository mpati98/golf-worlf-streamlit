import streamlit as st

pages = {
    "": [
        # st.Page("home.py", title="Home"),
        st.Page("product.py", title="Sản phẩm"),
        st.Page("golfClass.py", title="Lớp học Golf"),
        # st.Page("about.py", title="About"),
    ],
}
pg = st.navigation(pages)
pg.run()