import streamlit as st


# https://materializecss.com/
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">', unsafe_allow_html=True)
# https://materializecss.com/icons.html
st.markdown('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">', unsafe_allow_html=True)
# https://fontawesome.com/start
st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" rel="stylesheet">', unsafe_allow_html=True)

st.header("Home")



footerHTML=f"""
        <footer class="page-footer">
          <div class="container">
            <div class="row">
              <div class="col l6 s12">
                <h5 class="white-text">Golf Love</h5>
                <p class="grey-text text-lighten-4">Uy tín, chất lượng</p>
              </div>
              <div class="col l4 offset-l2 s12">
                <h5 class="white-text">Kênh</h5>
                <ul>
                  <li><a class="grey-text text-lighten-3" href="#">Fanpage</a></li>
                  <li><a class="grey-text text-lighten-3" href="#">Youtube</a></li>
                  <li><a class="grey-text text-lighten-3" href="#">Gmail</a></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="footer-copyright">
            <div class="container">
            © 2025 Copyright
            </div>
          </div>
        </footer>
            """
# html generate
st.html(footerHTML)
st.markdown('<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>', unsafe_allow_html=True)