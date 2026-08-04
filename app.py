import streamlit as st

st.set_page_config(page_title="AI PDF Q&A Bot", page_icon="🤖")
st.title("🤖 Smart PDF Q&A Bot")
st.write("Upload any Text/PDF file and search inside it!")

uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf"])

if uploaded_file is not None:
    try:
        text = uploaded_file.read().decode("utf-8", errors="ignore")
        st.success("✅ File Uploaded Successfully!")

        user_question = st.text_input("💬 Search key terms or questions:")

        if user_question:
            st.subheader("🔍 Matching Extract:")
            matching_lines = [line for line in text.split('\n') if any(word.lower() in line.lower() for word in user_question.split())]
            
            if matching_lines:
                st.info("\n".join(matching_lines[:5]))
            else:
                st.warning("No matching content found.")
    except Exception as e:
        st.error(f"Error reading file: {e}")