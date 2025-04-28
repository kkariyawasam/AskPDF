import streamlit as st
#from langchain.document_loaders import PyPDFLoader
#from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')



st.set_page_config(page_title="Ask PDF")
st.title("📄 Ask Questions About Your PDF")

# Upload PDF
pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])
question = st.text_input("Ask a question:")

if pdf_file and question:
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.read())

    # Load and process PDF
    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()

    # Load LLM and QA chain
    llm = OpenAI()
    qa_chain = load_qa_chain(llm, chain_type="map_reduce")

    # Get answer
    with st.spinner("Thinking..."):
        answer = qa_chain.run(input_documents=documents, question=question)
        st.success("Answer:")
        st.write(answer)
