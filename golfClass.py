import streamlit as st
import myFunc as Func

# https://materializecss.com/
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">', unsafe_allow_html=True)
# https://materializecss.com/icons.html
st.markdown('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">', unsafe_allow_html=True)
# https://fontawesome.com/start
st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" rel="stylesheet">', unsafe_allow_html=True)

introHTML=f"""
<div class="row">
<h1>Beginner Series Level 2</h1>
<p>Tôi sẽ hướng dẫn từng bước để giúp bạn kiểm tra các vị trí quan trọng nhất để tinh chỉnh cú đánh golf của mình.
Cuối cùng, chúng ta sẽ nói về các loại gậy khác nhau, các tư thế nằm khác nhau, v.v.! Vì vậy, hãy cùng chờ đón hành trình của chúng ta nhé!
Lần này, tôi sẽ dạy bài học bằng tiếng Anh có phụ đề tiếng Hàn.</p>
</div>
"""
# html generate
st.html(introHTML)

with st.form("my_form"):
    st.title("Đăng ký miễn phí")
    name = st.text_input(
            "Họ và tên",
            placeholder=""
            )
    email = st.text_input(
            "Email",
            placeholder=""
            )

    phone = st.text_input(
            "Số điện thoại",
            placeholder="",
            )

    message = st.text_area(
            "Lời nhắn",
            placeholder="Bạn có lưu ý hay yêu cầu gì không?",
            )


        # Every form must have a submit button.
    submitted = st.form_submit_button("Gửi")
    if submitted:
            Func.create_customer(name, email, phone,message)
            st.toast("Thông tin của bạn đã được ghi nhận, chúng tôi sẽ liên hệ lại ngay khi có thể !")


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