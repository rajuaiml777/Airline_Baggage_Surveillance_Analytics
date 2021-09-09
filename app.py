import streamlit as st
from PIL import Image
# Custom imports
from configs.multipage import MultiPage
import l2l3, about, new_op, overall_performances

# Create an instance of the app
app = MultiPage()

# Web Page Configuration
st.set_page_config(
    page_title='Bag Operator Performance Predictor',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Innodatatics Logo
st.sidebar.image('static/logo.jpg', width=250)

# WebApp Style
with open('static/style2.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Title for the app
def title():
    image = Image.open('static/bags.png')
    img, mid, head = st.columns([25, 5, 80])
    with img:
        st.image(image, channels="BGR", width=220)
    with head:
        st.title("""
                    # Bag Operator's Performance Predictor App
                    Let's check the performance of the operators!!
                    """)


title()
# Add all your applications (pages) here
app.add_page("About WebApp", about.about_app)
app.add_page("Existing Operator Performance", l2l3.main)
app.add_page("New Operator Performance", new_op.new_operator)
app.add_page("Overall Performance", overall_performances.overall_perf)

# The main app
app.run()
