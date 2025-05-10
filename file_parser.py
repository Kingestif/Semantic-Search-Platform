import fitz  

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    text_chunks = []
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text()
            if text.strip():
                text_chunks.append({
                    "page": page_num,
                    "text": text.strip()
                })
    return text_chunks

# Extract text from TXT file
def extract_text_from_txt(txt_file):
    content = txt_file.read().decode("utf-8")
    # Split text into 500-character chunks
    chunks = [content[i:i+500] for i in range(0, len(content), 500)]
    return [{"page": i + 1, "text": chunk.strip()} for i, chunk in enumerate(chunks)]
