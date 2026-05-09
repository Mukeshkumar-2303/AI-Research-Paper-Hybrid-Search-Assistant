import streamlit as st
import requests

API_URL = "https://ai-research-paper-hybrid-search-assistant.onrender.com"


# PAGE CONFIG

st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)


# CUSTOM CSS

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
    font-weight: 600;
}

.stTextInput input {
    border-radius: 10px;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.info-box {
    background-color: #111827;
    padding: 1rem;
    border-radius: 12px;
    border: 1px solid #374151;
    margin-bottom: 1rem;
}

.answer-box {
    background-color: #0f172a;
    padding: 1.5rem;
    border-radius: 14px;
    border: 1px solid #334155;
}

.tip-box {
    background-color: #1e293b;
    padding: 1rem;
    border-radius: 12px;
    border-left: 5px solid #38bdf8;
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)


# TITLE

st.title(" AI Research Paper Hybrid Search Assistant")

st.markdown("""
Upload research papers in PDF format and ask academic questions using:

✅ Hybrid Retrieval (FAISS + TF-IDF)  
✅ Semantic Search  
✅ AI Summarization using Groq LLM  
✅ LangGraph Agent Workflow  
""")


# HOW TO USE

with st.expander("📖 How To Use This App", expanded=True):

    st.markdown("""
### Step-by-Step Guide

1️⃣ Upload a research paper PDF  

2️⃣ Wait until processing is completed  

3️⃣ Click **Generate Answer**

4️⃣ Read the AI-generated academic summary

5️⃣  IMPORTANT:
After every generated answer, click the **Clear Answer** button before asking a new question.
""")


# SESSION STATE

if "answer_data" not in st.session_state:
    st.session_state.answer_data = None

if "question" not in st.session_state:
    st.session_state.question = ""


# SIDEBAR

with st.sidebar:

    st.header("⚙️ System Information")

    st.info("""
Hybrid Search Architecture:

• SentenceTransformers Embeddings  
• FAISS Vector Search  
• TF-IDF Retrieval  
• LangGraph Workflow  
• Groq LLM Summarization  
""")

    st.markdown("---")

    st.subheader(" Suggested Questions")

    st.markdown("""
- What is the research objective?
- Explain the methodology
- Summarize the paper
- What are the key findings?
- What are the limitations?
""")


# PDF UPLOAD

st.subheader(" Upload Research Paper")

uploaded_file = st.file_uploader(
    "Upload PDF File",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner(" Uploading and processing PDF..."):

        files = {"file": uploaded_file}

        response = requests.post(
            f"{API_URL}/upload",
            files=files
        )

    if response.status_code == 200:

        result = response.json()

        st.success(" PDF Processed Successfully")

        st.markdown(f"""
<div class="info-box">

<b>File Name:</b> {uploaded_file.name} <br>

 <b>Total Chunks Created:</b> {result.get("chunks", 0)}

</div>
""", unsafe_allow_html=True)

    else:
        st.error("❌ Upload failed")
        st.write(response.text)

# --------------------------------------------------
# QUESTION INPUT
# --------------------------------------------------
st.subheader("Ask Academic Question")

st.session_state.question = st.text_input(
    "Enter your question",
    value=st.session_state.question,
    placeholder="Example: What is the main contribution of this paper?"
)

# --------------------------------------------------
# BUTTONS
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    ask_btn = st.button(" Generate Answer")

with col2:
    clear_btn = st.button("🗑️ Clear Answer")

# --------------------------------------------------
# CLEAR BUTTON
# --------------------------------------------------
if clear_btn:
    st.session_state.answer_data = None
    st.session_state.question = ""
    st.rerun()


# GENERATE ANSWER

if ask_btn:

    if not st.session_state.question.strip():
        st.warning(" Please enter a question")
        st.stop()

    with st.spinner(" AI is analyzing the research paper..."):

        response = requests.post(
            f"{API_URL}/ask",
            json={
                "question": st.session_state.question
            }
        )

        try:
            data = response.json()

        except Exception:

            st.error("❌ Backend returned invalid response")
            st.write(response.text)
            st.stop()

        st.session_state.answer_data = data


# DISPLAY ANSWER

if st.session_state.answer_data:

    data = st.session_state.answer_data

    if "summary" not in data:
        st.error(data.get("detail", "Unknown backend error"))
        st.stop()

    st.subheader(" AI Generated Summary")

    st.markdown(
        f"""
<div class="answer-box">

{data["summary"]}

</div>
""",
        unsafe_allow_html=True
    )

    # IMPORTANT NOTE
    st.markdown("""
<div class="tip-box">

 <b>Important:</b> After every generated answer, please click the 
<b>Clear Answer</b> button before asking a new question.

</div>
""", unsafe_allow_html=True)

