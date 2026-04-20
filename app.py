import streamlit as st
from rag import build_index, ask
from pypdf import PdfReader

st.set_page_config(page_title="TurboVec PDF RAG", layout="centered")

st.title("📄 PDF RAG with TurboVec + Ollama")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    # simple chunking
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    st.success(f"✅ Loaded {len(chunks)} chunks from PDF")

    # build index
    index = build_index(chunks)

    query = st.chat_input("Ask something from the PDF...")

    if query:
        st.chat_message("user").write(query)

        answer, context = ask(query, index, chunks)

        st.chat_message("assistant").write(answer)

        with st.expander("🔍 Retrieved Context"):
            for c in context:
                st.write("- ", c)
