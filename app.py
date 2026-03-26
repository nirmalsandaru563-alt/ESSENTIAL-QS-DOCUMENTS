import streamlit as st

# The fix: change 'icon' to 'page_icon'
st.set_page_config(page_title="Essential QS Documents", page_icon="🏗️", layout="centered")

st.title("🏗️ Essential QS Documents")
st.info("Select a document below to download the official PDF.")


files = {
    "1. NRM 1: Order of cost estimating": "nrm1.pdf",
    "2. NRM 2: Detailed measurement": "nrm2.pdf",
    "3. NRM 1: Order of cost estimating": "nrm1.pdf"",
    "4. NRM 1: Order of cost estimating": "nrm1.pdf""
}


for label, file_path in files.items():
    try:
        with open(file_path, "rb") as f:
            st.download_button(
                label=f"📥 Download {label}",
                data=f,
                file_name=file_path,
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning(f"File '{file_path}' not found. Please upload it to Colab.")
