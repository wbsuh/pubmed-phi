from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
import streamlit as st

# Initialize Phi Assistant
assistant = Assistant(
    llm=OpenAIChat(model="gpt-3.5-turbo"),
    description="You are a friendly PubMed Assistant helping users find the right article they need.",
    debug=True
)

st.title("PubMed Chat Assistant")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I assist you with PubMed?"):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Use Phi Assistant to generate a response
    response_generator = assistant.run(prompt)
    response_text = ""
    for response in response_generator:
        response_text += response  
    
    with st.chat_message("assistant"):
        st.markdown(response_text)  
    
    st.session_state["messages"].append({"role": "assistant", "content": response_text})

