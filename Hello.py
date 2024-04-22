import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="STEM Insights",
        page_icon="👋",
    )

    st.write("# STEM Insights Questions Submission - 📖")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        This application provides a platform for you to pose questions for discussion within the STEM Insights project group.
    """
    )

    user_input = st.text_input('Please Enter a Question :question: :question: :question: :question:')

     # user_input = st.text_input('Please Enter a Question')

if __name__ == "__main__":
    run()
