import streamlit as st
from pypdf import PdfReader

# Page Configuration
st.set_page_config(
    page_title="PDF Insight AI",
    page_icon="⚡",
    layout="wide"
)

# Header Section
st.title("⚡ PDF Insight AI")
st.caption("Upload, extract, and search through your documents instantly.")
st.divider()

# Main Layout
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
            
            # Document Stats
            st.markdown("---")
            st.subheader("📊 Stats")
            words = len(full_text.split())
            lines = len(full_text.split('\n'))
            st.metric(label="Total Words", value=words)
            st.metric(label="Total Lines", value=lines)

        with col2:
            st.subheader("🔍 Search Document")
            query = st.text_input("💬 Type keyword or phrase to search:")

            if query:
                matching_lines = [line.strip() for line in full_text.split('\n') if query.lower() in line.lower() and line.strip()]

                if matching_lines:
                    st.write(f"**Found {len(matching_lines)} matching line(s):**")
                    for idx, line in enumerate(matching_lines[:10], 1):
                        st.info(f"**Result {idx}:** {line}")
                else:
                    st.warning("No matches found. Try typing a different word!")
            else:
                st.markdown("---")
                st.subheader("📜 Document Preview (First 500 characters)")
                st.text_area("", full_text[:500] + "...", height=200, disabled=True)

    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    with col2:
        st.info("👈 Upload a PDF or Text file from the left panel to begin searching.")
