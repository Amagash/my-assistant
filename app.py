import streamlit as st
from agent import BedrockAgent
import os
import boto3

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Initialize S3 client and Bedrock client
s3_client = boto3.client('s3', region_name=os.getenv('AWS_REGION'))
bedrock_client = boto3.client('bedrock-agent', region_name=os.getenv('AWS_REGION'))

# App title
st.title("My DevEx assistant")

# Initialize BedrockAgent (only once)
if 'agent' not in st.session_state:
    st.session_state.agent = BedrockAgent(
        region=os.getenv('AWS_REGION'),
        agent_id=os.getenv('BEDROCK_AGENT_ID'),
        agent_alias_id=os.getenv('BEDROCK_AGENT_ALIAS_ID')
    )

def sync_knowledge_base():
    """Trigger a sync of the knowledge base"""
    try:
        response = bedrock_client.start_ingestion_job(
            knowledgeBaseId=os.getenv('KNOWLEDGE_BASE_ID'),
            dataSourceId=os.getenv('DATA_SOURCE_ID')
        )
        return response['ingestionJob']['ingestionJobId']
    except Exception as e:
        st.error(f"Failed to sync knowledge base: {str(e)}")
        return None

# File uploader
uploaded_file = st.file_uploader("Choose a file to upload", type=['pdf', 'txt', 'doc', 'docx'])

if uploaded_file is not None:
    if st.button('Upload to S3'):
        with st.spinner('Uploading file and syncing knowledge base...'):
            try:
                # Upload to S3
                bucket_name = os.getenv('S3_BUCKET_NAME')
                s3_client.upload_fileobj(uploaded_file, bucket_name, uploaded_file.name)
                s3_path = f"s3://{bucket_name}/{uploaded_file.name}"
                
                # Trigger knowledge base sync
                sync_job_id = sync_knowledge_base()
                if sync_job_id:
                    st.success(f"""
                        File uploaded successfully! S3 path: {s3_path}
                        Knowledge base ingestion initiated with job ID: {sync_job_id}
                    """)
                else:
                    st.warning("File uploaded but knowledge base sync failed")
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