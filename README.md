# AWS Bedrock Assistant

A Streamlit-based chat interface for AWS Bedrock Agent with integrated file upload capabilities and knowledge base management.

## Features

- 💬 Interactive chat interface with AWS Bedrock Agent
- 📤 File upload functionality to S3
- 🔄 Automatic knowledge base synchronization
- 🌙 Dark mode interface
- 💾 Persistent chat history within session

## Prerequisites

- Python 3.8+
- AWS Account with access to:
  - Amazon Bedrock
  - Amazon S3
  - Bedrock Knowledge Base
- Appropriate AWS credentials configured

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/aws-bedrock-assistant.git
cd aws-bedrock-assistant
```

2. Install uv (if not already installed):
```bash
pip install uv
```

3. Create and activate a virtual environment:
```bash
# Create virtual environment
uv venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

4. Install dependencies:
```bash
uv pip install -r requirements.txt
```

5. Create a `.env` file in the root directory with your AWS configuration:
```env
AWS_REGION=us-west-2
BEDROCK_AGENT_ID=your-agent-id
BEDROCK_AGENT_ALIAS_ID=your-agent-alias-id
KNOWLEDGE_BASE_ID=your-knowledge-base-id
DATA_SOURCE_ID=your-data-source-id
S3_BUCKET_NAME=your-bucket-name
```
## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. You can:
   - Chat with the Bedrock Agent using the chat interface
   - Upload files (PDF, TXT, DOC, DOCX) to your S3 bucket
   - Files are automatically synced with your Bedrock Knowledge Base

## Project Structure

```
.
├── app.py               # Main Streamlit application
├── agent.py             # Bedrock Agent wrapper class
├── config.py            # Configuration management
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
└── .streamlit/          # Streamlit configuration
    └── config.toml      # Theme settings
```

## Key Components

### app.py
The main Streamlit application that provides:
- Interactive chat interface
- File upload functionality to S3
- Automatic knowledge base synchronization
- Session state management for chat history

### agent.py
A wrapper class for AWS Bedrock Agent that:
- Manages AWS Bedrock client connections
- Handles agent interactions and responses
- Provides methods for getting responses from the agent

### config.py
Manages configuration loading from environment variables:
- AWS Bedrock Agent settings
- Environment variable management using python-dotenv

### .streamlit/config.toml
Configures the Streamlit theme:
```toml
[theme]
base="dark"
primaryColor="#FF4B4B"
backgroundColor="#0E1117"
secondaryBackgroundColor="#262730"
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| AWS_REGION | AWS region (e.g., us-west-2) |
| BEDROCK_AGENT_ID | Your Bedrock Agent ID |
| BEDROCK_AGENT_ALIAS_ID | Your Bedrock Agent Alias ID |
| KNOWLEDGE_BASE_ID | Your Knowledge Base ID |
| DATA_SOURCE_ID | Your Data Source ID |
| S3_BUCKET_NAME | Your S3 bucket name |

## AWS Configuration

Ensure you have AWS credentials configured either through:
- AWS CLI (`aws configure`)
- Environment variables (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`)
- IAM role (if running on AWS infrastructure)

Required AWS permissions:
- `bedrock:InvokeAgent`
- `s3:PutObject`
- `bedrock-agent:StartIngestionJob`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [AWS Bedrock](https://aws.amazon.com/bedrock/)