import streamlit as st
from pypdf import PdfReader

# Page Configuration
st.set_page_config(
    page_title="BookVerse AI - Digital Library",
    page_icon="📚",
    layout="wide"
)

# Header
st.title("📚 BookVerse AI - Digital Library & Reader")
st.caption("Explore featured books or upload your own PDF/TXT to read and search!")
st.divider()

# Sample Featured Online Books Data
FEATURED_BOOKS = {
    "The Art of War": {
        "author": "Sun Tzu",
        "cover": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&q=80",
        "description": "An ancient Chinese military treatise dating from the Late Spring and Autumn Period.",
        "content": """The Art of War by Sun Tzu.
Chapter 1: Laying Plans
Sun Tzu said: The art of war is of vital importance to the State. It is a matter of life and death, a road either to safety or to ruin. Hence it is a subject ofAapki digital library ko ek realistic **Online E-Book Store & Reader** wala feel dene ke liye, hum script mein **Pre-loaded Sample E-Books** aur unki **Cover Images** add kar dete hain. 

Isse jab bhi koi aapki website open karega, use pehle se hi curated books, unke visual covers, aur reading material milenge—chahe unhone koi file upload na ki ho!

---

### **🛠️ GitHub Par Code Update Karo:**

1. **`github.com`** par apni repository open karo: **`Noorjahan228/AI-PDF-QA-Bot`**
2. **`app.py`** par click karke Pencil (Edit ✏️) icon par click karo.
3. Purana poora code mita kar niche wala code paste karke **Commit changes** kar do:

```python
import streamlit as st
from pypdf import PdfReader

# Page Configuration
st.set_page_config(
    page_title="BookVerse AI - Online Digital Library",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling for Sleek E-Commerce & Reader Theme
st.markdown("""
    <style>
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
        font-family: 'Inter', sans-serif;
    }
    .hero-banner {
        background: linear-gradient(135deg, #1E1B4B 0%, #311B92 50%, #4A148C 100%);
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        border: 1px solid #4C1D95;
        margin-bottom: 25px;
    }
    .card-box {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .search-card {
        background: #0F172A;
        border-left: 4px solid #A855F7;
        padding: 12px;
        border-radius: 8px;
        margin-top: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Top Banner
st.markdown("""
    <div class="hero-banner">
        <h1 style="color: white; margin: 0;">📚 BookVerse AI</h1>
        <p style="color: #C084FC; margin-top: 5px;">Explore Online Sample Books or Upload Your Own PDF</p>
    </div>
""", unsafe_allow_html=True)

# Pre-loaded Online Books Content
PRELOADED_BOOKS = {
    "Artificial Intelligence Handbook": {
        "author": "Dr. Alex Rivera",
        "category": "Technology",
        "cover": "[https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400&q=80](https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400&q=80)",
        "content": [
            "Chapter 1: Introduction to Modern AI\nArtificial Intelligence is transforming industries worldwide through machine learning models, neural networks, and automated decision engines.",
            "Chapter 2: Neural Networks & Deep Learning\nDeep neural networks simulate human brain functions to identify complex patterns within vast datasets.",
            "Chapter 3: Future Trends\nGenerative AI and automated agents represent the next milestone in global computing capabilities."
        ]
    },
    "The Digital Mindset": "The Digital Mindset",
    "Python Programming Essentials": "Python Programming Essentials"
}

PRELOADED_BOOKS["The Digital Mindset"] = {
    "author": "Sarah Jenkins",
    "category": "Business & Innovation",
    "cover": "[https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&q=80](https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&q=80)",
    "content": [
        "Chapter 1: Embracing Digital Transformation\nSuccess in the modern era requires a fundamental shift in how teams operate, analyze data, and adapt to rapid technological shifts.",
        "Chapter 2: Data-Driven Decisions\nOrganizations utilizing systematic data analysis outperform competitors by identifying emerging trends earlier."
    ]
}

PRELOADED_BOOKS["Python Programming Essentials"] = {
    "author": "Mark Techson",
    "category": "Software Engineering",
    "cover": "[https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=400&q=80](https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=400&q=80)",
    "content": [
        "Chapter 1: Python Basics\nPython provides clean syntax and versatile libraries for data science, web development, and automation scripts.",
        "Chapter 2: Data Structures\nUnderstanding lists, dictionaries, tuples, and custom classes forms the foundation of scalable software design."
    ]
}

# Main Layout Grid
col_left, col_right = st.columns([1, 2], gap="large")

with col_left:
    st.subheader("📥 Upload Custom Document")
    uploaded_file = st.file_uploader("Upload PDF or TXT file", type=["pdf", "txt"])
    st.divider()

    st.subheader("📖 Featured Online Library")
    selected_book_title = st.selectbox("Choose a pre-loaded book:", list(PRELOADED_BOOKS.keys()))
    
    # Display Cover Image and Metadata for Selected Pre-loaded Book
    book_meta = PRELOADED_BOOKS[selected_book_title]
    st.image(book_meta["cover"], caption=selected_book_title, use_column_width=True)
    st.write(f"**Author:** {book_meta['author']}")
    st.write(f"**Category:** {book_meta['category']}")

# Determine Active Document (Uploaded File OR Preloaded Online Content)
pages_content = []
full_text = ""
document_name = ""

if uploaded_file is not None:
    document_name = uploaded_file.name
    try:
        if uploaded_file.name.endswith('.pdf'):
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text = page.extract_text() or ""
                pages_content.append(text)
                full_text += text + "\n"
        else:
            raw_text = uploaded_file.read().decode("utf-8", errors="ignore")
            chunks = [raw_text[i:i+1000] for i in range(0, len(raw_text), 1000)]
            pages_content = chunks if chunks else [raw_text]
            full_text = raw_text
    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    document_name = selected_book_title
    pages_content = book_meta["content"]
    full_text = "\n".join(pages_content)

# Right Column - Interactive Reader and Search Engine
with col_right:
    st.subheader(f"📖 Active Book: {document_name}")
    
    tab_reader, tab_search = st.tabs(["📖 Interactive Page Reader", "🔍 Smart Search Engine"])

    with tab_reader:
        if pages_content:
            page_no = st.slider("Flip Pages", 1, len(pages_content), 1)
            st.markdown(f"### Page {page_no} of {len(pages_content)}")
            
            # Display Page Content inside container
            st.info(pages_content[page_no - 1] if pages_content[page_no - 1].strip() else "*(Empty or Image Page)*")

            # Document Statistics
            words_count = len(full_text.split())
            st.caption(f"📊 Total Word Count in Document: {words_count:,}")

    with tab_search:
        st.markdown("### 🔍 Search Inside Book")
        search_query = st.text_input("Type key phrases, chapter names, or terms to search:")

        if search_query:
            matches = [line.strip() for line in full_text.split('\n') if search_query.lower() in line.lower() and line.strip()]
            if matches:
                st.write(f"Found **{len(matches)}** relevant result(s):")
                for idx, match in enumerate(matches[:8], 1):
                    st.markdown(f'<div class="search-card"><b>Match {idx}:</b> {match}</div>', unsafe_allow_html=True)
            else:
                st.warning("No matches found for this keyword.")
        else:
            st.caption("Enter keywords to locate exact text passages instantly.")
