import streamlit as st
from streamlit_lottie import st_lottie
from utils import load_url, load_css
import base64

# Basic configurations
st.set_page_config(page_title="Carlota's Website", page_icon="👾", layout="wide")

# load local CSS styling
load_css('./style/styles.css')

########## HEADER SECTION ###########
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

            I am most interested in becoming a Software Developer. I already have several years of previous experience working with Python for various applications including Web Scraping, 
            Machine Learning, Data Science, and Deep Learning, as well as a deep understanding of distributed system architecture and open-source tools 
            such as Kafka, ElasticSearch or HDFS. I am comfortable working with Linux-based systems and scripting in bash, as well as some experience 
            with Docker, which I have successfully incorporated into several academic & personal projects (including this website!).

            My next learning goals include:
            
            + Building small full-stack applications using Python as backend and React as frontend.
            + Dockerizing my applications and deploying them to the cloud.
            + Learning AWS and getting certified as a Cloud Practitioner.
            + Getting hands-on experience working with Jenkins to provide automatic testing and CI/CD.
            + Learning functional programming languages such as Elixir or Haskell.
            + Studying microservices architecture, which I am really curious about.
            """
        )
    
    with right_column:
        lottie_coding_gif = "https://assets6.lottiefiles.com/packages/lf20_w51pcehl.json"
        coding_gif = load_url(lottie_coding_gif)
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
            lottie_news_gif = "https://assets1.lottiefiles.com/packages/lf20_inviljje.json"
            news_gif = load_url(lottie_news_gif)
            st_lottie(news_gif, height=400, key="news_gif")

        with right_column:
            st.subheader("Hacker News Crawler 👾📃")
            st.markdown(
                """
                [Hacker news](https://news.ycombinator.com/) is a website portal where tech-related news are updated
                daily. Although the website seems simple at first hand, working with it can become tricky, since the entries 
                change daily and do not always follow a uniform structure, as some of them may be lacking some fields.

                In this project, I scraped, parsed and cleaned content from the website using Python libraries such as `requests` and `BeatifulSoup4`,
                organizing the code using OOP principles and ensuring a clean and organized Git log. Moreover, I included further back-end functionalities,
                including a database to store the data and a REST API to serve it!

                Specifically, the project includes the following functionalities:

                + Scraping the website and parsing the HTML content.
                + A dockerized PostgreSQL database for storing the data.
                + A dockerized FastAPI service for interacting with the back-end.
                + Unit-tests for ensuring the correct functioning of the code.                

                Link to the project: https://github.com/carlota-moh/hacker-news-crawler
                """, unsafe_allow_html=True
            )

    st.write("---")

    with st.container(): 
        left_column, right_column = st.columns((1, 1.5), gap="small")
        with left_column:
            lottie_dog_gif = "https://assets6.lottiefiles.com/packages/lf20_HwRTPu.json"
            dog_gif = load_url(lottie_dog_gif)
            st_lottie(dog_gif, height=400, key="dog_gif")

        with right_column:
            st.subheader("Humor Hound 🐶🔎")
            st.markdown(
                """
                What if there was a LLM that was capable of recognizing whether the tone in which a sentence is written
                is sarcastic or not? For this project, I collaborated with some colleagues to train a wide variety of 
                Deep-Learning models (CNN, RNN, LSTM and even a transformer-based model) to recognize sarcasm, using a 
                [kaggle](https://www.kaggle.com/datasets/rmisra/news-headlines-dataset-for-sarcasm-detection) dataset 
                that included news headlines written in both a sarcastic and a non-sarcastic tone. 

                For this project, I was specifically in charge of the application:

                + Creating a front-end interface using Streamlit.
                + Developed a back-end using Fast-API for serving the best model.
                + Virtualized the service using Docker.

                You can interact with the application by simply running the `run.sh` file in the repo in your computer!
                
                Link to the project: https://github.com/carlota-moh/humor-hound
                """, unsafe_allow_html=True
            )

    st.write("---")

    with st.container():
        left_column, right_column = st.columns((1, 1.5), gap="small")

        with left_column:
            lottie_snow_gif = "https://assets9.lottiefiles.com/private_files/lf30_n7en8fxl.json"
            snow_gif = load_url(lottie_snow_gif)
            st_lottie(snow_gif, height=400, key="snow_gif")

        with right_column:
            st.subheader("Frozen lake ❄️")
            st.markdown(
                """
                Frozen lake is a simple game in which you have to get from the start point to the goal without falling
                into any of the holes in the way. Well, it may seem easy for a human... but how would a machine do it?
                
                In this project I used Reinforcement Learning (specifically, a technique called *Q-learning*) to train 
                an agent to learn to play frozen lake game, using an OpenAI gymnasium environment. In addition, I tweeked
                the reward scheme so that the agent learnt the *best* (i.e.: shortest) possible path! After training the 
                agent, I evaluated its performance on a hundred game runs and proved that the agent had indeed learnt to
                play the game perfectly! 

                You can also check out a visual representation of the training and evaluation of the agent through the gifs 
                I generated for the project. 
                
                Link to the project: https://github.com/carlota-moh/frozen-lake
                """, unsafe_allow_html=True
            )

    st.write("")
    st.write("---")
    st.write("")

    with st.container(): 
        left_column, right_column = st.columns((1, 1.5), gap="small")
        with left_column:
            lottie_ml_gif = "https://assets2.lottiefiles.com/private_files/lf30_8npirptd.json"
            ml_gif = load_url(lottie_ml_gif)
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
