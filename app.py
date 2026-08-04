import streamlit as st
from pypdf import PdfReader

# Page Configuration
st.set_page_config(
    page_title="PDF Insight AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced CSS for Futuristic Dark AI Theme
st.markdown("""
    <style>
    /* Main Background & Font */
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Styling */
    .ai-header {
        text-align: center;
        padding: 20px 0;
        background: linear-gradient(90deg, #3B82F6 0%, #8B5CF6 50%, #EC4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .ai-subtitle {
        text-align: center;
        color: #94A3B8;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }

    /* Glassmorphism Cards */
    div[data-testid="stColumn"] > div {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }

    /* Custom File Uploader */
    section[data-testid="stFileUploadDropzone"] {
        background-color: #0F172A !important;
        border: 2px dashed #6366F1 !important;
        border-radius: 12px !important;
    }

    /* Custom Inputs */
    .stTextInput > div > div > input {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
        border: 1px solid #475569 !important;
        border-radius: 10px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #8B5CF6 !important;
        box-shadow: 0 0 10px rgba(139, 92, 246, 0.5) !important;
    }

    /* Metric Cards */
    div[data-testid="stMetricValue"] {
        color: #38BDF8 !important;
        font-weight: 700;
    }

    /* Custom Result Boxes */
    .result-box {
        background-color: #0F172A;
        border-left: 4px solid #8B5CF6;
        padding: 12px 16px;
        border-radius: 8px;
        margin-bottom: 10px;
        color: #E2E8F0;
    }
    </style>
""", unsafe_allow_html=True)

# Top Banner Title
st.markdown('<div class="ai-header">🤖 PDF INSIGHT AI</div>', unsafe_allow_html=True)
st.markdown('<div class="ai-subtitle">Powered by Next-Gen Document Parsing</div>', unsafe_allow_html=True)

# Main Grid
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown("### 📂 Document Portal")
    uploaded_file = st.file_uploader("Drop your PDF or TXT document here", type=["txt", "pdf"])

full_text = ""

if uploaded_file is not None:
    try:
        # Extract text based on file type
        if uploaded_file.name.endswith('.pdf'):
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    full_text += extracted + "\n"
        else:
            full_text = uploaded_file.read().decode("utf-8", errors="ignore")

        with col1:
            st.success("⚡ Document Analyzed Successfully!")
            st.markdown("---")
            st.markdown("### 📊 Document Insights")
            
            words = len(full_text.split())
            lines = len(full_text.split('\n'))
            
            m1, m2 = st.columns(2)
            m1.metric(label="Total Words", value=f"{words:,}")
            m2.metric(label="Total Lines", value=f"{lines:,}")

        with col2:
            st.markdown("### 🔍 Intelligent Search")
            query = st.text_input("💬 Ask or search anything inside document...", placeholder="Type keywords like 'Skills', 'Experience', etc.")

            if query:
                matching_lines = [line.strip() for line in full_text.split('\n') if query.lower() in line.lower() and line.strip()]

                if matching_lines:
                    st.markdown(f"**Found {len(matching_lines)} relevant insights:**")
                    for idx, line in enumerate(matching_lines[:10], 1):
                        st.markdown(f'<div class="result-box"><b>Match {idx}:</b> {line}</div>', unsafe_allow_html=True)
                else:
                    st.warning("No matching keywords found in the document. Try another query!")
            else:
                st.markdown("---")
                st.markdown("### 📜 Smart Preview")
                st.text_area("", full_text[:600] + "...", height=220, disabled=True)

    except Exception as e:
        st.error(f"Error parsing document: {e}")
else:
    with col2:
        st.info("👈 Upload a PDF or Text file on the left panel to trigger the AI parser.")
