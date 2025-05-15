import streamlit as st
logo = "./static/imgs/图片 1.png"
st.logo(logo,size="large")

with st.sidebar:
    st.title("Navigation")
    st.write("This is a simple navigation example using Streamlit.")
    st.write("You can navigate between different pages using the sidebar.")
pages = {
        "Home": [
            st.Page('./tools/home.py',title='home',icon="🏠"),
        ],
        "About": [
            st.Page('./tools/test.py',title='about',icon="ℹ️"),    
        ],
        # "Contact": [],
    }
pg = st.navigation(pages)
pg.run()

