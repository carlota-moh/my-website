import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image   
from utils import load_url, load_css
import base64
from io import BytesIO

# Basic configurations
st.set_page_config(page_title="Carlota's Website", page_icon="👾", layout="wide")

# load Lottie gifs
lottie_coding_gif = "https://assets6.lottiefiles.com/packages/lf20_w51pcehl.json"
lottie_news_gif = "https://assets1.lottiefiles.com/packages/lf20_inviljje.json"
lottie_ml_gif = "https://assets2.lottiefiles.com/private_files/lf30_8npirptd.json"
coding_gif = load_url(lottie_coding_gif)
news_gif = load_url(lottie_news_gif)
ml_gif = load_url(lottie_ml_gif)

# load local CSS styling
load_css('./style/styles.css')

# HEADER SECTION
with st.container():
    info_column, image_column = st.columns((2, 1))
    with info_column:
        st.title("Hi! I'm Carlota 😊")
        st.header("Big Data, Technology & Advanced Analytics MSc Student")
        st.write("""
                 I'm an independent, self-driven MSc student with an insatiable appetite for technology and learning new things!
                 I love coffee, cats, playing bass and learning Japanese.
                 """)
        st.subheader("Links 🌟")
        st.write("[GitHub](https://github.com/carlota-moh) [LinkedIn](https://linkedin.com/in/carlota-monedero-50a5941b0)")

    with image_column:
        with open("./images/me.jpg", "rb") as f:
            image = f.read()

        st.markdown(f'<img class="my-image" src="data:image/png;base64,{base64.b64encode(image).decode()}" alt="Me" height=50%>', unsafe_allow_html=True)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("About me 🙋")
        st.markdown(
            """
            Hi! Thanks for dropping by! My name is Carlota and I am a currently studying a Master's degree in Big Data & Advanced
            Analytics in Madrid (Spain). My background includes a degree in Biotechnology that I achieved with an average grade of 9.58/10, 
            but during my final thesis I discovered the world of ML & AI and fell in love with it! I am currently completing an MSc in Big Data 
            & Advanced Analytics, which I will be completing in June.

            As a Software Engineer, I have several years of previous experience working with Python for various applications including Web Scraping, 
            Machine Learning, Data Science, and Deep Learning, as well as a deep understanding of distributed system architecture and open-source tools 
            such as Kafka, ElasticSearch or HDFS. I am comfortable working with Linux-based systems and scripting in bash, as well as some experience 
            with Docker.

            Though my main field of expertise is Data Science, I am also learning new programming languages that can be applied to a wider range of
            applications, including:

            + Front-end development: HTML, CSS and JavaScript
            + Functional programming: Scala and Elixir
            + Dynamic programming: Python and JavaScript

            """
        )
    
    with right_column:
        st_lottie(coding_gif, height=600, key="coding_gif")

########## PROJECTS ###########

with st.container():
    st.write("---")
    st.title("Projects 🚀")
    st.write("Here is a list of some of my recent projects. Feel free to look around 👀 ")
    st.write("")
    st.write("")

    with st.container():
        left_column, right_column = st.columns((1, 1.5), gap="small")

        with left_column:
            with open("./images/eval_animation.gif", "rb") as frozen_gif:
                contents = frozen_gif.read()
                frozen_url = base64.b64encode(contents).decode("utf-8")
            st.markdown(
                f'<img class=project-image src="data:image/gif;base64,{frozen_url}" alt="frozen lake gif">',
                unsafe_allow_html=True,
            )

        with right_column:
            st.subheader("Frozen lake ❄️")
            st.markdown(
                """
                Frozen lake is a simple game in which you have to get from the start point to the goal without falling
                into any of the holes in the way. Well, it may seem easy for a human... but how would a machine do it?
                In this project I used Reinforcement Learning (specifically, a technique called *Q-learning*) to train 
                an agent to learn to play frozen lake game, using an OpenAI gymnasium environment. In addition, I tweeked
                the reward scheme so that the agent learnt the *best* (i.e.: shortest) possible path.
                Link to the project: https://github.com/carlota-moh/frozen-lake
                """, unsafe_allow_html=True
            )

    st.write("")
    st.write("---")
    st.write("")

    with st.container(): 
        left_column, right_column = st.columns((1, 1.5), gap="small")
        with left_column:
            st_lottie(news_gif, height=400, key="news_gif")

        with right_column:
            st.subheader("Hacker News Crawler 👾📃")
            st.markdown(
                """
                [Hacker news](https://news.ycombinator.com/) is a website portal where tech-related news are updated
                daily. Although the website seems simple at first hand, working with it can become tricky, since the entries 
                change daily and do not always follow a uniform structure, as some of them may be lacking some fields.

                In this project, I scraped, parsed and cleaned content from the website using Python libraries such as `requests` and `BeatifulSoup4`,
                organizing the code using OOP principles and ensuring a clean and organized Git log. 
                 
                The project is still under development, and I plan to introduce automatic testing using `pytest`, 
                as well as building an small backend for storing information using `django`. In addition, I would like to build
                a small front-end application to test my recently acquired knowledge of HTML, CSS and JavaScript so stay tuned
                for that!

                Link to the project: https://github.com/carlota-moh/hacker-news-crawler
                """, unsafe_allow_html=True
            )

    st.write("---")

    with st.container(): 
        left_column, right_column = st.columns((1, 1.5), gap="small")
        with left_column:
            st_lottie(ml_gif, height=400, key="ml_gif")

        with right_column:
            st.subheader("Ensemble Learning 🤖")
            st.markdown(
                """
                In this project, some colleges and I collaborated to implement advanced Machine Learning for solving
                a real world problem: predicting whether a day will be holiday or not based on daily energy demand data.
                In order to do this we conducted a torough comparison of different Ensemble-learning algorithms, including
                Random Forest, Bagging, Gradient Boosting and Stacking.

                I was in charge of implementing Bayesian Optimization for hyperparameter optimization, as well as fine-tuning
                a gradient boosting algorithm using `LGBM` and implementing stacking techniques for combining it with other
                tree based algorithms, which achieved the best performances among the essayed models.

                Link to the project: https://github.com/carlota-moh/ml2-ensemble
                """, unsafe_allow_html=True
            )

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
        st.title("Contact me! 📧")
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
