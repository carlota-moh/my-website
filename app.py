import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image   
from utils import load_url, setup_logger, load_css
import base64
from io import BytesIO


# Set up logger
log_file = './logs/website.log'
logger = setup_logger(name="website", log_file=log_file)

# Basic configurations
st.set_page_config(page_title="Carlota's Website", page_icon="👾", layout="wide")

# load Lottie gifs
lottie_coding_gif = "https://assets6.lottiefiles.com/packages/lf20_w51pcehl.json"
coding_gif = load_url(lottie_coding_gif, logger=logger)

# load local CSS styling
load_css('./style/styles.css')

# HEADER SECTION
with st.container():
    info_column, image_column = st.columns((2, 1))
    with info_column:
        st.title("Hi! I'm Carlota 😊")
        st.header("Big Data, Technology & Advanced Analytics MSc Student")
        st.write("I'm an independent, self-driven MSc student with an insatiable appetite for technology and learning new things!")

    with image_column:
        with open("./images/me.jpg", "rb") as f:
            image = f.read()

        st.markdown(f'<img class="my-image" src="data:image/png;base64,{base64.b64encode(image).decode()}" alt="Me" height=50%>', unsafe_allow_html=True)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me 🙋")
        st.write(
            """
            Hi! Thanks for dropping by! My name is Carlota and I am a currently studying a Master's degree in Big Data & Advanced
            Analytics in Madrid (Spain). I originally graduated from a BSc in Biotechnology, but during my final thesis I discovered
            the world of ML & AI and fell in love with it!

            I have experience working in several internships as a Data Scientist and right now I am expanding my limits beyond this field
            to learn more about Computer Science and Software Development! I mainly work with Python, but I amd learning some more languages 
            (including HTML, CSS, JavaScript and Scala).
            """
        )
    
    with right_column:
        st_lottie(coding_gif, height=400, key="coding_gif")

with st.container():
    st.title("Links 🌟")
    st.write("[GitHub](https://github.com/carlota-moh)")
    st.write("[LinkedIn](linkedin.com/in/carlota-monedero-50a5941b0)")

with st.container():
    st.write("---")
    contact_form = """
        <form action="https://formsubmit.co/carlota.monederoh@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Place your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Contact me 📧")
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()