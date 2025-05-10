import sys
sys.modules['torch.classes'] = None
import streamlit as st
from file_parser import extract_text_from_pdf, extract_text_from_txt
from embedding import generate_embeddings
from search import search_query
from qa import extract_answer
from utils import highlight_keywords

st.title("📄 Document Upload and Semantic Search")

# File uploader widget
uploaded_file = st.file_uploader("Upload PDF or TXT file", type=["pdf", "txt"])

# Initialize session state for the first time
if 'previous_queries' not in st.session_state:
    st.session_state.previous_queries = []
    st.session_state.embedded_chunks = []

if uploaded_file:
    st.success("File uploaded successfully!")
    
    # Extract text from uploaded file
    if uploaded_file.name.endswith(".pdf"):
        chunks = extract_text_from_pdf(uploaded_file)
    else:
        chunks = extract_text_from_txt(uploaded_file)
    
    # Show extracted text chunks
    st.write(f"Extracted {len(chunks)} text chunks:")
    for chunk in chunks[:3]:  # Show the first 3 chunks for preview
        st.markdown(f"**Page {chunk['page']}**\n\n{chunk['text'][:200]}...")  # Preview the first 200 characters
    
    # Generate embeddings and store them in session state
    embeddings = generate_embeddings(chunks)
    st.write(f"Generated {len(embeddings)} embeddings.")
    st.session_state.embedded_chunks = embeddings  # Store embeddings for later use

# User input for querying
query = st.text_input("Ask a question related to the document:")

if query:
    # Save the current query to session state
    st.session_state.previous_queries.append({
        'query': query,
        'results': []
    })
    
    # Perform the semantic search for the query
    results = search_query(query, st.session_state.embedded_chunks)
    
    # Display the results with highlighted keywords for the current query
    st.write(f"Top 3 results for your query '{query}':")
    for result in results[:3]:  # Show top 3 results
        highlighted_text = highlight_keywords(result['text'][:200], query)  # Highlight for current query
        st.markdown(f"**Page {result['page']} (Relevance Score: {result['score']:.4f})**", unsafe_allow_html=True)
        st.markdown(highlighted_text, unsafe_allow_html=True)

    answers = extract_answer(query, results)
    st.markdown("### 🧠 Best Answer(s):")
    for ans in answers[:1]:  # Show top 1 answer
        highlighted_context = highlight_keywords(ans['context'][:300], query)  # Highlight for current query
        st.markdown(f"**Page {ans['page']} (Confidence: {ans['score']:.2f})**")
        st.markdown(f"✅ **Answer:** {ans['answer']}")
        st.markdown(f"📝 **Context:**", unsafe_allow_html=True)
        st.markdown(highlighted_context, unsafe_allow_html=True)

    # Update the results for this query in session state
    st.session_state.previous_queries[-1]['results'] = results

# If there are previous queries, show them with context but no highlighting
if len(st.session_state.previous_queries) > 1:
    st.write("You previously asked:")
    for idx, query_data in enumerate(st.session_state.previous_queries[:-1], start=1):
        st.write(f"**Query {idx}:** {query_data['query']}")
        st.write(f"**Results:**")
        for result in query_data['results'][:3]:  # Display previous query results without highlighting
            st.markdown(f"Page {result['page']} (Relevance Score: {result['score']:.4f})")
            st.markdown(result['text'][:200])  # Show text without highlighting
