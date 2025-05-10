from transformers import pipeline

# Load QA pipeline from Hugging Face
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def extract_answer(question, context_chunks):
    """
    Run QA on top-k chunks to extract an answer span.
    Returns a list of answers with confidence scores.
    """
    answers = []
    for chunk in context_chunks:
        result = qa_pipeline({
            'question': question,
            'context': chunk['text']
        })
        answers.append({
            'answer': result['answer'],
            'score': result['score'],
            'page': chunk['page'],
            'context': chunk['text']
        })
    # Sort by confidence score
    return sorted(answers, key=lambda x: x['score'], reverse=True)
