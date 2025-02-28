import streamlit as st
import requests

BACKEND_URL = "http://backend:8080/chat"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Initialize chat history list

if "current_url" not in st.session_state:
    st.session_state.current_url = ""  # Initialize current URL tracker

if "trigger_send" not in st.session_state:
    st.session_state.trigger_send = False  # Flag to track when to send message

# Set page title and layout
st.set_page_config(page_title="💬 DSA Chatbot", layout="wide")

# Sidebar for URL input and reset button
with st.sidebar:
    st.title("🔗 DSA Chat Assistant")
    url = st.text_input("Enter LeetCode Problem URL:", placeholder="https://leetcode.com/problems/example/")
    
    # Reset chat button
    if st.button("🔄 Reset Chat", use_container_width=True):
        response = requests.post(f"{BACKEND_URL}/reset")
        if response.status_code == 200:
            st.session_state.chat_history = [{"role": "assistant", "content": response.json()["messages"][0]["text"]}]
        else:
            st.error("⚠️ Error resetting chat.")
        st.session_state.current_url = ""
        st.experimental_rerun()  # Force UI refresh

# Chat messages container
st.title("💬 DSA Chatbot")
st.write("---")  # Divider for better UI separation
chat_container = st.container()

# Display chat history with auto-scrolling
with chat_container:
    for msg in st.session_state.get("chat_history", []):
        role = "user" if msg["role"] == "user" else "assistant"
        with st.chat_message(role):
            st.markdown(msg["content"])

    # Empty container for auto-scrolling to latest message
    auto_scroll = st.empty()

# Function to handle sending messages
def send_message():
    if not st.session_state.input_message.strip():
        return  # Ignore empty messages

    if not url:
        st.warning("⚠️ Please enter a LeetCode URL.")
        return

    with st.spinner("Thinking..."):
        message = st.session_state.input_message.strip()

        # Decide whether to start a new chat or continue existing
        endpoint = "/init" if st.session_state.current_url != url else "/continue"
        payload = {"url": url, "message": message} if endpoint == "/init" else {"message": message}
        
        # Send request
        response = requests.post(f"{BACKEND_URL}{endpoint}", json=payload)

        if response.status_code == 200:
            # Append user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": message})
            
            # Get AI response and append it
            ai_reply = response.json()["message"]
            st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})
            
            # Store current URL after first message
            st.session_state.current_url = url

            # ✅ Just trigger the send flag, don't clear the input
            st.session_state.trigger_send = False

            # ✅ Force UI update *immediately*
            st.experimental_rerun()

# Multi-line text area for user input
input_message = st.text_area(
    "💬 Ask a question:",
    placeholder="Type your question here...",
    key="input_message"
)

# Send message button
if st.button("🚀 Send", use_container_width=True):
    if input_message.strip():
        st.session_state["trigger_send"] = True  

# ✅ Trigger message send at the end of the script
if st.session_state.get("trigger_send", False):
    send_message()
    st.session_state["trigger_send"] = False  


st.write(" ")
st.write("---")
st.caption("⚡ Built with Streamlit & FastAPI | AI-powered DSA helper")
