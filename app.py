import streamlit as st
import base64
import os
import shutil

# Optional: replace with your actual icon-github.png load logic if needed
github_icon_base64 = ""
try:
    with open("icon-github.png", "rb") as img_file:
        github_icon_base64 = base64.b64encode(img_file.read()).decode()
except FileNotFoundError:
    pass

st.set_page_config(page_title="RepoSage", layout="wide")

# CSS for UI styling
st.markdown("""
    <style>
    .sidebar-panel {
        background: #232323;
        color: #fff;
        padding: 20px 16px 20px 16px;
        border-radius: 18px;
        min-height: 92vh;
        margin-right: 0px;
        font-size: 16px;
    }
    .sidebar-panel button, .sidebar-panel input, .sidebar-panel .stTextInput {
        width: 100%;
        margin-bottom: 12px;
    }
    .sidebar-logo {
        display: flex; align-items: center; gap: 8px; margin-bottom: 24px;
    }
    .sidebar-logo img { height: 32px; }
    .sidebar-title { font-weight: bold; font-size: 26px; }
    .disclaimer-box {
        background-color: #fff3cd; color: #856404;
        padding: 10px 15px; border-radius: 8px; font-size: 15px;
        border: 1px solid #ffeeba; margin-top: 10px; margin-bottom: 16px;
    }
    .side-note {
        background-color: #fff3cd; color: #856404;
        padding: 10px 15px; border-radius: 8px; font-size: 15px;
        border: 1px solid #ffeeba;
        margin-top: auto;
    }
    /* Make chat messages readable */
    .chat-label { font-weight: bold; font-size: 18px; }
    .chat-content { font-size: 15px; margin-top: 5px; }
    </style>
""", unsafe_allow_html=True)

# Use columns for fixed sidebar and main content
col_sidebar, col_main = st.columns([1, 3])

with col_sidebar:
    st.markdown("<div class='sidebar-panel'>", unsafe_allow_html=True)
    # Logo and name
    if github_icon_base64:
        st.markdown(f"""
        <div class='sidebar-logo'>
            <img src="data:image/png;base64,{github_icon_base64}" />
            <span class='sidebar-title'>RepoSage</span>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown("<div class='sidebar-title'>RepoSage</div>", unsafe_allow_html=True)
    st.markdown("## 🔗 Upload GitHub Repo Link")
    github_url = st.text_input("Paste GitHub URL", key="github_url_input")
    analyze_btn = st.button("🔍 Analyze Repository")
    st.markdown("""
        <div class="disclaimer-box">
            🔐 <i><b>Disclaimer:</b><br>No data is stored. All processing is done locally and securely.</i>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🧹 Clear Chat"):
        if "chat_history" in st.session_state: st.session_state.chat_history = []
        st.success("Chat history cleared!")
    st.markdown("""
        <div class="side-note">
            ⚠️ <i><b>Note:</b><br>
            This project is for academic enhancement and learning purposes only. Recommended for small to medium-sized repositories.</i>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)  # End sidebar panel

with col_main:
    # Header/logo in main area as well, if you wish
    st.markdown("## RepoSage")
    st.markdown("### Your Personal GitHub Repository Assistant")
    st.markdown("#### 🧠 Ask about your Repo")
    # Example chat UI logic — replace with yours!
    chat_placeholder = st.empty()
    if analyze_btn:
        st.success("Repository analysis would start here.")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    # Simulate previous chat, for demonstration
    for msg in st.session_state.chat_history:
        label = "🧑‍💼 You:" if msg["role"] == "user" else "📘 RepoSage:"
        st.markdown(f"<div class='chat-label'>{label}</div><div class='chat-content'>{msg['content']}</div>", unsafe_allow_html=True)
    user_question = st.text_input("Type your question here...", key="chat_input")
    if user_question:
        st.session_state.chat_history.append({"role": "user", "content": user_question})
        st.session_state.chat_history.append({"role": "assistant", "content": "Sample reposage answer..."})
        st.experimental_rerun()
