iimport streamlit as st
from pypdf import PdfReader

# Page Configuration
st.set_page_config(
    page_title="BookVerse AI - Interactive Library",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced Custom CSS for Library / E-commerce Look
st.markdown("""
    <style>
    .stApp {
        background-color: #0B0F19;
        color: #E2E8F0;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Title Banner */
    .hero-banner {
        background: linear-gradient(135deg, #1E1B4B 0%, #311B92 50%, #4A148C 100%);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid #4C1D95;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(124, 58, 237, 0.2);
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #FFFFFF;
        margin: 0;
    }
    .hero-tag {
        color: #A78BFA;
        font-size: 1.1rem;
        margin-top: 8px;
    }

    /* Cards Styling */
    .card-box {
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }

    /* Feature Badge */
    .badge {
        background: #8B5CF6;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }

    /* Custom Result Box */
    .search-card {
        background: #1E293B;
        border-left: 4px solid #A855F7;
        padding: 12px 16px;
        border-radius: 8px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Top Hero Section
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">📚 BookVerse AI</h1>
        <div class="hero-tag">Your Interactive Digital Library & Smart Document Intelligence Engine</div>
    </div>
""", unsafe_allow_html=True)

# Feature Showcase Banner (If no file uploaded)
if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False

# Layout Grid
left_col, right_col = st.columns([1, 2], gap="large")

with left_col:
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.subheader("📥 Add To Your Library")
    uploaded_file = st.file_uploader("Upload any Book, PDF, or Text File", type=["pdf", "txt"])
    st.markdown('</div>', unsafe_allow_html=True)

pages_content = []
full_text = ""

if uploaded_file is not None:
    st.session_state.file_uploaded = True
    try:
        if uploaded_file.name.endswith('.pdf'):
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text = page.extract_text() or ""
                pages_content.append(text)
                full_text += text + "\n"
        else:
            raw_text = uploaded_file.read().decode("utf-8", errors="ignore")
            # Split text into virtual pages for reader feel
            chunks = [raw_text[i:i+1000] for i in range(0, len(raw_text), 1000)]
            pages_content = chunks if chunks else [raw_text]
            full_text = raw_text

        with left_col:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="card-box">', unsafe_allow_html=True)
            st.markdown("### 📖 Book Metadata")
            st.write(f"**Title:** {uploaded_file.name}")
            st.write(f"**Total Pages:** {len(pages_content)}")
            
            words = len(full_text.split())
            st.metric(label="Total Words Count", value=f"{words:,}")
            st.markdown('</div>', unsafe_allow_html=True)

        with right_col:
            # Tabs View: Reader vs Search Engine
            tab1, tab2 = st.tabs(["📖 Interactive Reader", "🔍 AI Search Engine"])

            with tab1:
                st.markdown("### 📑 Live Book Flip View")
                if pages_content:
                    page_no = st.slider("Select Page", 1, len(pages_content), 1)
                    
                    # Page Visual Container
                    st.markdown(f"**Page {page_no} of {len(pages_content)}**")
                    st.info(pages_content[page_no - 1] if pages_content[page_no - 1].strip() else "*(Empty or Image-based Page)*")

            with tab2:
                st.markdown("### 🔎 Smart Content Finder")
                query = st.text_input("💬 Search key concepts, phrases, or chapters...")

                if query:
                    matches = [line.strip() for line in full_text.split('\n') if query.lower() in line.lower() and line.strip()]
                    if matches:
                        st.markdown(f"Found **{len(matches)}** direct matches in book:")
                        for idx, match in enumerate(matches[:8], 1):
                            st.markdown(f'<div class="search-card"><b>Result {idx}:</b> {match}</div>', unsafe_allow_html=True)
                    else:
                        st.warning("No matches found for this search term.")
                else:
                    st.caption("Type words like 'Chapter', 'Summary', 'Index' etc.")

    except Exception as e:
        st.error(f"Error loading book: {e}")

else:
    with right_col:
        st.markdown("### 🌟 Popular Digital Formats Supported")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
            <div class="card-box" style="text-align: center;">
                <h2>📘</h2>
                <b>PDF Books</b>
                <p style="font-size: 0.8rem; color: #9CA3AF;">Textbooks, Manuals, Novel PDFs</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="card-box" style="text-align: center;">
                <h2>📄</h2>
                <b>TXT Docs</b>
                <p style="font-size: 0.8rem; color: #9CA3AF;">Notes, Scripts, Code files</p>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown("""
            <div class="card-box" style="text-align: center;">
                <h2>🔍</h2>
                <b>AI Search</b>
                <p style="font-size: 0.8rem; color: #9CA3AF;">Instant deep content lookup</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.info("👈 Upload your book/PDF on the left panel to launch the Interactive Book Reader!")
