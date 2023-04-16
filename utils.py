import requests
import logging
import streamlit as st

def setup_logger(name: str, log_file: str) -> logging.Logger:

    # Initialize logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # Create a file handler to log the messages.
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    # Create a console handler with a higher log level.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    # Modify the handlers log format to your convenience.
    handler_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(handler_format)
    console_handler.setFormatter(handler_format)
    # Finally, add the handlers to the logger.
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def load_url(url: str, logger: logging.Logger) -> dict:

    response = requests.get(url)

    if response.status_code == 200:
        logger.debug(f"Succesfully retrieved {url}")
        return response.json()

    else:
        logger.critical(f"Something went wrong with {url}! Status code {response.status_code}")

def load_css(style_file: str) -> None:
    """Load CSS styling"""
    with open(style_file, 'r') as f:
        st.markdown(f"<style>{f.read()}<style/>", unsafe_allow_html=True)