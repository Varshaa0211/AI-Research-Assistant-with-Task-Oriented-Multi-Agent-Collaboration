import streamlit as st
from agents.reader_agent import ReaderAgent
from agents.summarizer_agent import SummarizerAgent
from agents.qa_agent import QAAgent
from coordinator import CoordinatorAgent

st.set_page_config(page_title="🧠 AI Research Assistant", page_icon="🤖")

st.title("🤖 AI Research Assistant with Multi-Agent Collaboration")
st.write("Upload a research paper (PDF) and ask questions!")

uploaded_file = st.file_uploader("📄 Upload PDF", type="pdf")
question = st.text_input("❓ Ask a question about the paper:")

if uploaded_file and question:
    reader = ReaderAgent()
    summarizer = SummarizerAgent()
    qa = QAAgent(api_key="YOUR_OPENAI_KEY")  # Replace with your OpenAI key

    coordinator = CoordinatorAgent(reader, summarizer, qa)
    result = coordinator.handle_task(uploaded_file, question)

    st.subheader("📄 Summary")
    st.write(result['summary'])
    st.subheader("📝 Answer")
    st.write(result['answer'])
