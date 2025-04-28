
# 📄 Ask Questions About Your PDF

This is a simple **Streamlit** web application that allows you to upload a PDF and ask questions about its content.
It uses **LangChain** and **OpenAI's GPT model** to understand and answer your questions based on the uploaded document.

## UI Preview

<img width="518" alt="image" src="https://github.com/user-attachments/assets/2edf6514-7650-402e-9195-09bdaa9bf0d6" />


## Features

- 📄 Upload any PDF file.
- ❓ Ask any question about the content of the PDF.
- 🤖 Get AI-powered answers using OpenAI GPT.
- ⚡ Quick and interactive UI built with Streamlit.


## How it Works

- Upload a PDF file using the Streamlit file uploader.
- Ask a question in the input box.
- The app processes the PDF using **PyPDFLoader** from **LangChain Community**.
- It uses the **Map Reduce** QA chain approach to efficiently answer based on the document's content.


## Dependencies

- Streamlit
- LangChain
- OpenAI
- LangChain Community Extensions
- Python Dotenv

