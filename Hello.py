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

    user_question_input = st.text_input('Please Enter a Question For Consideration :sun_with_face:')

    user_team_input = st.selectbox(
        'What Team do you sit on',
        ('Network Improvement','Marketing and Comms', 'Education Team')


if __name__ == "__main__":
    run()
