# Semantic Search Platform

## Project Overview

The **Semantic Search Platform** is a web-based application designed to provide users with the ability to upload PDF or TXT documents and perform semantic search. The platform uses advanced Natural Language Processing (NLP) models to allow users to query documents and receive contextually relevant results. It also integrates a **Question Answering (QA)** module to provide the best answers to user queries, improving the overall search experience.

## Technologies Used

- **Python**: Backend development.
- **Streamlit**: For the interactive web interface.
- **Transformers (Hugging Face)**: For NLP and question-answering capabilities.
- **TensorFlow/PyTorch**: For machine learning-based embeddings.
- **FAISS**: For efficient similarity search.
- **spaCy**: For text processing and NLP tasks.
- **Pandas**: For data manipulation and storage.
- **NumPy**: For numerical operations.
- **Docker**: For containerizing the application.
- **GitHub Actions**: For continuous integration and deployment.

## Features

- **File Upload**: Upload PDF or TXT files to extract content.
- **Text Extraction**: Automatically extract text from the uploaded files.
- **Semantic Search**: Perform queries on the uploaded document and get contextually relevant results.
- **Question Answering (QA)**: Ask specific questions and get precise answers from the document.
- **Highlighting Keywords**: Highlight queried keywords in the results to improve the search experience.
- **Previous Query History**: View previous queries with results and context.

## Project Structure

Semantic-Search-Platform/
├── app.py # Main Streamlit app file
├── file_parser.py # Functions for extracting text from PDF and TXT files
├── embedding.py # Functions to generate embeddings for documents
├── search.py # Functions for performing semantic search
├── qa.py # Functions for question answering
├── utils.py # Utility functions (e.g., for highlighting keywords)
├── requirements.txt # List of dependencies
├── Dockerfile # Docker configuration file
└── .gitignore # Git ignore file for unwanted files/folders


## 🔧 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/Semantic-Search-Platform.git
   cd Semantic-Search-Platform

Create a virtual environment:

```python -m venv .venv
```
Activate the virtual environment:

```.\.venv\Scripts\activate
```
Install the dependencies:

```pip install -r requirements.txt
```
Running the Application

```streamlit run app.py
```

License
This project is licensed under the MIT License - see the LICENSE file for details.