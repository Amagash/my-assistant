import streamlit as st
from agent import BedrockAgent
import config
import os
import boto3

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Initialize S3 client
s3_client = boto3.client('s3', region_name=config.BEDROCK_CONFIG['region'])

# App title
st.title("My DevEx assistant")

# Initialize BedrockAgent (only once)
if 'agent' not in st.session_state:
    st.session_state.agent = BedrockAgent(
        region=config.BEDROCK_CONFIG['region'],
        agent_id=config.BEDROCK_CONFIG['agent_id'],
        agent_alias_id=config.BEDROCK_CONFIG['agent_alias_id']
    )

# File uploader
uploaded_file = st.file_uploader("Choose a file to upload", type=['pdf', 'txt', 'doc', 'docx'])

if uploaded_file is not None:
    if st.button('Upload to S3'):
        with st.spinner('Uploading...'):
            try:
                bucket_name = os.getenv('S3_BUCKET_NAME')
                s3_client.upload_fileobj(uploaded_file, bucket_name, uploaded_file.name)
                s3_path = f"s3://{bucket_name}/{uploaded_file.name}"
                st.success(f"File uploaded successfully! S3 path: {s3_path}")
            except Exception as e:
                st.error(f"Failed to upload file: {str(e)}")

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