import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input(
        "Enter a URL:", 
        value="https://careers.nike.com/lead-technology-asset-management/job/R-89188"
    )
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            raw_content = loader.load().pop().page_content
            data = clean_text(raw_content)
            
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    # Page config must be set before any other Streamlit UI components run
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)