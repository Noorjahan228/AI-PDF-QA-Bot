import streamlit as st
from pypdf import PdfReader

# Page Configuration
st.set_page_config(
    page_title="PDF Insight AI",
    page_icon="⚡",
    layout="wide"
)

# Custom CSS for Sleek UI
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #4F46E5;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #6B7280;
        text-align: center;
        margin-bottom: 30px;
    }
    .stTextInput > div > div > input {
        border-radius: 8px;
  import streamlit as st
from pypdf import PdfReader

# Page Configuration
st.set_page_config(
    page_title="PDF Insight AI",
    page_icon="⚡",
    layout="wide"
)

# Custom CSS for Sleek UI
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #4F46E5;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #6B7280;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown('<div class="main-header">⚡ PDF Insight AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Upload, Extract, and Search through your documents instantly</div>', unsafe_allow_html=True)

# Main Container
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📁 Upload Document")
    uploaded_file = st.file_uploader("Choose a TXT or PDF file", type=["txt", "pdf"])

full_text = ""

if uploaded_file is not None:
    try:
        # Check file type and extract text
        if uploaded_file.name.endswith('.pdf'):
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    full_text += extracted + "\n"
        else:
            full_text = uploaded_file.read().decode("utf-8", errors="ignore")

        with col1:
            st.success("✅ File Processed Successfully!")
            
            # File Stats
            st.markdown("### 📊 Document Stats")
            words = len(full_text.split())
            lines = len(full_text.split('\n'))
            st.metric(label="Total Words", value=words)
            st.metric(label="Total Lines", value=lines)

        with col2:
            st.subheader("🔍 Search & Analyze")
            query = st.text_input("💬 Ask a question or search key phrases:")

            if query:
                st.write(f"**Results for:** *'{query}'*")
                matching_lines = [line.strip() for line in full_text.split('\n') if query.lower() in line.lower() and line.strip()]

                if matching_lines:
                    for idx, line in enumerate(matching_lines[:8], 1):
                        st.info(f"**Match {idx}:** {line}")
                else:
                    st.warning("No direct matches found. Try another keyword!")
            else:
                st.markdown("---")
                st.markdown("#### 📜 Document Preview (First 500 characters):")
                st.text_area("", full_text[:500] + "...", height=200, disabled=True)

    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    with col2:
        st.info("👈 Please upload a PDF or Text file from the sidebar/left panel to start searching.")