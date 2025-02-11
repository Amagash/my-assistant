import streamlit as st
from agent import BedrockAgent
from config import BEDROCK_CONFIG

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# App title
st.title("My DevEx assistant")

# Initialize BedrockAgent (only once)
if 'agent' not in st.session_state:
    st.session_state.agent = BedrockAgent(
        region=BEDROCK_CONFIG['region'],
        agent_id=BEDROCK_CONFIG['agent_id'],
        agent_alias_id=BEDROCK_CONFIG['agent_alias_id']
    )

# Chat input
if prompt := st.chat_input("What would you like to ask?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get response from agent
    response = st.session_state.agent.get_response(prompt)
    
    # Add assistant response to chat history
    if response:
        st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"]) 