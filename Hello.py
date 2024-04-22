import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="STEM Insights",
        page_icon="👋",
    )

    st.write("# STEM Insights Questions Submission - 📖")

    # st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        This application provides a platform for you to pose questions for discussion within the STEM Insights project group. 
    """
        
        """ 
        Ensure your question is clear in it's ask ad a detailed reason as to why this is being asked is given. 
        """

        """
        <u>**Examples**</u> of correctly considered and asked questions are given below the form. 
        """, unsafe_allow_html=True
    )

    user_question_input = st.text_input('Please Enter a Question For Consideration :sun_with_face:')

    col1,col2 = st.columns(2)
    with col1:
        user_team_input = st.selectbox(
            'What Team Do You Sit On',
            ('','Network Improvement','Marketing and Comms', 'Education Team')
        )
    with col2:
        user_project_input = st.selectbox(
            'What Project Does Your Question Relate Too',
            ('','NCCE','Science', 'STEM Ambassadors', 'General CPD')
        )


if __name__ == "__main__":
    run()
